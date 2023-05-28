import cv2
import sys
import numpy as np

def find_interesting_area(img_src):
    # Load the image
    image = cv2.imread(img_src)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray, 50, 150)

    # Find contours of the edges
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Determine the bounding box of the largest contour (most interesting area)
    largest_contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(largest_contour)

    # Set the desired fixed size for cropping
    fixed_size = (200, 200)  # Example: 200x200 pixels

    # Calculate the center coordinates of the bounding box
    center_x = x + w // 2
    center_y = y + h // 2

    # Calculate the crop coordinates based on the fixed size and center
    crop_x = max(0, center_x - fixed_size[0] // 2)
    crop_y = max(0, center_y - fixed_size[1] // 2)
    crop_width = fixed_size[0]
    crop_height = fixed_size[1]

    # Crop the most interesting area with the fixed size
    cropped_image = image[crop_y:crop_y+crop_height, crop_x:crop_x+crop_width]
    img_dst = "cropped_img.jpg"

    cv2.imwrite(img_dst, cropped_image)

    return img_dst

def print_sharp(image_path):
  image = cv2.imread(image_path)
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
  sharpness = np.var(laplacian)
  print("Sharpness:", sharpness)

# Check if the image path is provided as a command line argument
if len(sys.argv) < 2:
    print("Please provide the image path as a command line argument")
    exit()

# Get the image path from command line argument
image_path = sys.argv[1]

# image_path = "/content/drive/MyDrive/Vision/moon.jpg"

# Load the image
image = cv2.imread(image_path)
print("Original Size:", sys.getsizeof(image))
print_sharp(image_path)

# Check if the image is loaded successfully
if image is None:
    print("Failed to load the image")
    exit()

# Define the desired width and height
desired_width = (640/3)*2
desired_height = (480/3)*2

# Resize the image to the desired dimensions
resized_image = cv2.resize(image, (desired_width, desired_height))

# Compress the resized image and save it with reduced quality
compressed_image_path = "compressed_resized_image.jpg"
compression_params = [cv2.IMWRITE_JPEG_QUALITY, 30]  # Adjust the quality value as per your requirement
cv2.imwrite(compressed_image_path, resized_image, compression_params)

print("Image compressed and saved as" + compressed_image_path)
print("Compressed Size:", sys.getsizeof(compressed_image_path))
print_sharp(compressed_image_path)

find_interesting_area(compressed_image_path)
