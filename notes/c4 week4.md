# One shot learning
  - Able to recognise a person with training on one image
  - Similarity function is used

---

# Triplet loss
  - Used in Siamese network
  - Get difference between anchor and positive or negative image
  - Loss:
      `L(A, P, N) = max (||f(A) - f(P)||^2  - ||f(A) - f(N)||^2 + alpha , 0)`

---

# Neural style transfer
  - Application of conv nets
  - Takes an image and style and fuses these inputs to create an image with given style
