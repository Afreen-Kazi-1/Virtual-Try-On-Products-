import cv2
import mediapipe as mp
import numpy as np

mp_pose = mp.solutions.pose

original_video_path = 'parent1.mp4'
simulation_video_path = 'child1.mp4'

cap_original = cv2.VideoCapture(original_video_path)
cap_simulation = cv2.VideoCapture(simulation_video_path)

fps = cap_original.get(cv2.CAP_PROP_FPS)
width = int(cap_original.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap_original.get(cv2.CAP_PROP_FRAME_HEIGHT))

max_display_height = 480 
display_height = min(height, max_display_height)
display_width = int(width * (display_height / height))

def remove_background(frame):
    mask = np.zeros(frame.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    
    rect = (10, 10, frame.shape[1]-20, frame.shape[0]-20)
    
    cv2.grabCut(frame, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    
    mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
    
    result = frame * mask2[:, :, np.newaxis]
    return result

with mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap_original.isOpened() and cap_simulation.isOpened():
        ret_orig, frame_orig = cap_original.read()
        ret_sim, frame_sim = cap_simulation.read()

        if not ret_orig or not ret_sim:
            break

        frame_sim_nobg = remove_background(frame_sim)

        # Convert the BGR frame to RGB for MediaPipe
        rgb_frame_orig = cv2.cvtColor(frame_orig, cv2.COLOR_BGR2RGB)

        results = pose.process(rgb_frame_orig)

        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark

            left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
            right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
            left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]

            def get_pixel_coords(landmark):
                return int(landmark.x * width), int(landmark.y * height)
            
            left_shoulder_px = get_pixel_coords(left_shoulder)
            right_shoulder_px = get_pixel_coords(right_shoulder)
            left_hip_px = get_pixel_coords(left_hip)

            shoulder_center_x = int((left_shoulder_px[0] + right_shoulder_px[0]) / 2)
            shoulder_center_y = int((left_shoulder_px[1] + right_shoulder_px[1]) / 2)

            body_height = int(np.linalg.norm(np.array(left_shoulder_px) - np.array(left_hip_px)))

            body_width = int(np.linalg.norm(np.array(left_shoulder_px) - np.array(right_shoulder_px)))

            cloth_height, cloth_width, _ = frame_sim_nobg.shape

            scale_x = body_width / cloth_width
            scale_y = body_height / cloth_height

            scale = max(scale_x, scale_y)*2

            new_cloth_width = int(cloth_width * scale)
            new_cloth_height = int(cloth_height * scale)

            resized_cloth = cv2.resize(frame_sim_nobg, (new_cloth_width, new_cloth_height))

            x_offset = shoulder_center_x - new_cloth_width // 2
            y_offset = shoulder_center_y - int(new_cloth_height * 0.19) 

            # Ensure the offsets are within the frame boundaries
            x_offset = max(0, min(x_offset, width - new_cloth_width))
            y_offset = max(0, min(y_offset, height - new_cloth_height))

            # Create a region of interest (ROI) in the original frame
            roi = frame_orig[y_offset:y_offset+new_cloth_height, x_offset:x_offset+new_cloth_width]

            cloth_gray = cv2.cvtColor(resized_cloth, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(cloth_gray, 5, 255, cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)
            roi_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

            # Take only region of cloth from cloth image
            cloth_fg = cv2.bitwise_and(resized_cloth, resized_cloth, mask=mask)

            # Put cloth in ROI and modify the original frame
            dst = cv2.add(roi_bg, cloth_fg)
            frame_orig[y_offset:y_offset+new_cloth_height, x_offset:x_offset+new_cloth_width] = dst

        display_frame = cv2.resize(frame_orig, (display_width, display_height))

        cv2.imshow('Superimposed Video', display_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap_original.release()
cap_simulation.release()
cv2.destroyAllWindows()