import cv2
import numpy as np
import json
from scipy.interpolate import Rbf

def generate_source_points_from_edges(image, num_points):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Canny Edge Detection
    edges = cv2.Canny(gray, 50, 150)
    
    # Find contours (i.e., continuous edges) in the image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Flatten all contour points into a single list
    edge_points = np.vstack(contours).squeeze()

    # If there are fewer edge points than needed, duplicate some points
    if len(edge_points) < num_points:
        multiplier = int(np.ceil(num_points / len(edge_points)))
        edge_points = np.tile(edge_points, (multiplier, 1))

    # Randomly select `num_points` from the edge points
    selected_indices = np.random.choice(len(edge_points), num_points, replace=False)
    source_points = edge_points[selected_indices]
    
    return np.array(source_points, dtype=np.float32)

def load_keypoints(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Extract the pose keypoints
    pose_keypoints = np.array(data['people'][0]['pose_keypoints'], dtype=np.float32)
    
    # Reshape to get pairs of (x, y) coordinates
    target_points = pose_keypoints.reshape(-1, 3)[:, :2]  # Ignore the confidence scores
    
    return target_points

def tps_transform(source_points, target_points, shape):
    rbf_x = Rbf(source_points[:, 0], source_points[:, 1], target_points[:, 0], function='thin_plate')
    rbf_y = Rbf(source_points[:, 0], source_points[:, 1], target_points[:, 1], function='thin_plate')
    
    grid_x, grid_y = np.meshgrid(np.arange(shape[1]), np.arange(shape[0]))
    map_x = rbf_x(grid_x, grid_y).astype(np.float32)
    map_y = rbf_y(grid_x, grid_y).astype(np.float32)
    
    return map_x, map_y

def warp_image(image, source_points, target_points):
    map_x, map_y = tps_transform(source_points, target_points, image.shape[:2])
    warped_image = cv2.remap(image, map_x, map_y, interpolation=cv2.INTER_LINEAR)
    return warped_image

# Load the cloth image
image_path = "cloth.jpg"
image = cv2.imread(image_path)

# Generate source points directly from the cloth image using edge detection
num_points = 8  # Match the number of target points
source_points = generate_source_points_from_edges(image, num_points)

# Load target keypoints from JSON file
json_file = "keypoints.json"
target_points = load_keypoints(json_file)

# Ensure that the number of points matches
if len(source_points) > len(target_points):
    source_points = source_points[:len(target_points)]
elif len(source_points) < len(target_points):
    target_points = target_points[:len(source_points)]

# Warp the image using TPS
warped_image = warp_image(image, source_points, target_points)

# Save or display the warped image
output_path = "warped_cloth_pose.jpg"
cv2.imwrite(output_path, warped_image)
cv2.imshow("Warped Cloth to Pose", warped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
