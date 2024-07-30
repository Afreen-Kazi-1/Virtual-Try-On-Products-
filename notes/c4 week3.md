# Object detection
  - Localization means locating the object in the given image
  - The output is
      - ```Y = [
  		Pc				# Probability of an object
  		bx				# Bounding box
  		by				# Bounding box
  		bh				# Bounding box
  		bw				# Bounding box
  		c1				# The classes
  		c2 ...
  - Pointing out to particular points is called landmark detection

---

# Sliding window
  - Algorithm
      - Decide rectangle size.
      - Split image into rectangles of the size picked. Each region should be covered.
      - Feed each rectangle into the Conv net and decide if its a car or not.
      - Store the rectangles that contains the cars.
      - If two or more rectangles intersects choose the rectangle with the best Intersection over Union
  - Requires too much computation

---

# Non max suppression
  - Algorithm
    - Y shape should be [Pc, bx, by, bh, hw]
    - Discard all boxes with Pc < 0.6
    - While there are any remaining boxes:
        - Pick the box with the largest Pc, output that as a prediction
        - Discard any remaining box with IoU > 0.5 with that box output in the previous step
    - If there are multiple classes, run the suppression once for every output class.

---

# Anchor boxes
  - Helps a grid cell to detect multiple boxes

---

# YOLO
  - You only look once
  - Better speed
