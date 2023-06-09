import cv2
import sys

# Check if the image path is provided as a command line argument
if len(sys.argv) < 2:
    print("Please provide the image path as a command line argument")
    exit()

# Get the image path from command line argument
image_path = sys.argv[1]

# Load the image
image = cv2.imread(image_path)
print("Original Size:", sys.getsizeof(image))

# Check if the image is loaded successfully
if image is None:
    print("Failed to load the image")
    exit()

# Define the desired width and height
desired_width = 640
desired_height = 480

# Resize the image to the desired dimensions
resized_image = cv2.resize(image, (desired_width, desired_height))

# Compress the resized image and save it with reduced quality
compressed_image_path = "compressed_resized_image.jpg"
compression_params = [cv2.IMWRITE_JPEG_QUALITY, 30]  # Adjust the quality value as per your requirement
cv2.imwrite(compressed_image_path, resized_image, compression_params)

print("Image compressed and saved as" +  compressed_image_path)
print("Compressed Size:", sys.getsizeof(image))
