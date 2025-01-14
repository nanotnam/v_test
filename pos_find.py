import os
from PIL import Image
import numpy as np

# Path to your image folder
folder_path = '/Users/hoangnamvu/Downloads/test/targets'

# Initialize counters
total_zeros = 0
total_ones = 0
total_pixels = 0

# Iterate through the images in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".png") or filename.endswith(".jpg"):  # Adjust extensions if needed
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path).convert('L')  # Convert to greyscale (if not already)
        
        # Convert image to a numpy array
        img_array = np.array(img)
        
        # Count pixels with value 0 and 1
        total_zeros += np.sum(img_array == 0)
        total_ones += np.sum(img_array == 1)
        total_pixels += img_array.size

# Calculate proportions
zero_proportion = total_zeros / total_pixels
one_proportion = total_ones / total_pixels

print(f"Proportion of 0s: {zero_proportion}")
print(f"Proportion of 1s: {one_proportion}")

pos = zero_proportion/one_proportion

print(f"pos is: {pos}")