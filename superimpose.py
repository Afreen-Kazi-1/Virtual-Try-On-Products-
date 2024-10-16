import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose

# Video paths (replace with your video file paths)
original_video_path = 'parent.mp4'
simulation_video_path = 'child.mp4'
output_video_path = 'superimposed_output.mp4'

# Open the original and simulation videos
cap_original = cv2.VideoCapture(original_video_path)
cap_simulation = cv2.VideoCapture(simulation_video_path)

# Get properties of the original video
fps = cap_original.get(cv2.CAP_PROP_FPS)
width = int(cap_original.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap_original.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Video writer to save the final output
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

# Initialize pose estimation
with mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap_original.isOpened() and cap_simulation.isOpened():
        ret_orig, frame_orig = cap_original.read()
        ret_sim, frame_sim = cap_simulation.read()

        if not ret_orig or not ret_sim:
            break

        # Convert the BGR frame to RGB for MediaPipe
        rgb_frame_orig = cv2.cvtColor(frame_orig, cv2.COLOR_BGR2RGB)

        # Process the frame to extract pose landmarks
        results = pose.process(rgb_frame_orig)

        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark

            # Get key landmarks for positioning the cloth
            left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
            right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
            left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
            right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]

            # Convert landmarks to pixel coordinates
            def get_pixel_coords(landmark):
                return int(landmark.x * width), int(landmark.y * height)
            
            left_shoulder_px = get_pixel_coords(left_shoulder)
            right_shoulder_px = get_pixel_coords(right_shoulder)
            left_hip_px = get_pixel_coords(left_hip)
            right_hip_px = get_pixel_coords(right_hip)

            # Calculate the center of the shoulders and hips for positioning
            shoulder_center_x = int((left_shoulder_px[0] + right_shoulder_px[0]) / 2)
            shoulder_center_y = int((left_shoulder_px[1] + right_shoulder_px[1]) / 2)

            hip_center_x = int((left_hip_px[0] + right_hip_px[0]) / 2)
            hip_center_y = int((left_hip_px[1] + right_hip_px[1]) / 2)

            # Calculate the body height (distance from shoulders to hips)
            body_height = np.linalg.norm(np.array([shoulder_center_x, shoulder_center_y]) - np.array([hip_center_x, hip_center_y]))

            # Calculate the body width (distance between shoulders)
            body_width = np.linalg.norm(np.array(left_shoulder_px) - np.array(right_shoulder_px))

            # Get the cloth video dimensions
            cloth_height, cloth_width, _ = frame_sim.shape

            # Calculate scaling factors for cloth
            scale_x = body_width / cloth_width
            scale_y = body_height / cloth_height

            # Calculate the affine transformation matrix for scaling and translation
            scale_matrix = np.float32([
                [scale_x, 0, shoulder_center_x - (cloth_width * scale_x) / 2],
                [0, scale_y, shoulder_center_y - (cloth_height * scale_y) / 2]
            ])

            # Apply the transformation to the cloth video (scaling and translation)
            transformed_cloth = cv2.warpAffine(frame_sim, scale_matrix, (width, height))

            # Create a mask for the cloth
            gray_cloth = cv2.cvtColor(transformed_cloth, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(gray_cloth, 1, 255, cv2.THRESH_BINARY)

            # Invert the mask for blending
            mask_inv = cv2.bitwise_not(mask)

            # Remove the cloth region from the original frame
            frame_bg = cv2.bitwise_and(frame_orig, frame_orig, mask=mask_inv)

            # Isolate the cloth region
            cloth_fg = cv2.bitwise_and(transformed_cloth, transformed_cloth, mask=mask)

            # Combine the background and the cloth
            blended_frame = cv2.add(frame_bg, cloth_fg)

            # Write the result frame to the output video
            out.write(blended_frame)

# Release resources
cap_original.release()
cap_simulation.release()
out.release()

print("Superimposed video created:", output_video_path)
