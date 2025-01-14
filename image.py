import cv2
import numpy as np

# Read the grayscale image (ensure it's in 0-1 range)
image = cv2.imread('/Users/hoangnamvu/Downloads/a/hold/targets/img1.png', cv2.IMREAD_GRAYSCALE)

# Convert the image so that 1 becomes 255
image[image == 1] = 255

# Save or display the updated image
cv2.imwrite('updated_image.png', image)