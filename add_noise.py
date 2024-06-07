import cv2
import numpy as np
import os

"""Gaussian noise"""
# # Define the directory with the original images and the directory for the noisy images
# input_dir = "/home/danica01/raid1-data1/dan/dataset/nerf_synthetic/lego/train"
# output_dir = '/home/danica01/raid1-data1/dan/dataset/nerf_synthetic/lego/train-30noise'

# # Create the output directory if it doesn't exist
# os.makedirs(output_dir, exist_ok=True)

# # Get a list of all image files in the input directory
# image_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

# # Loop over each image file
# for image_file in image_files:
#     # Load the image
#     image = cv2.imread(os.path.join(input_dir, image_file))

#     # Generate a binary mask that has True for 20% of the pixels
#     mask = np.random.choice([False, True], size=image.shape[:2], p=[0.7, 0.3])

#     # Add Gaussian noise to the image
#     mean = 0
#     std_dev = 0.005 * 255  # 1% of the pixel value range (0-255)
#     noise = np.random.normal(mean, std_dev, image.shape).astype(np.uint8)
#     noisy_image = cv2.add(image, noise * np.dstack([mask, mask, mask]))

#     # Save the noisy image
#     cv2.imwrite(os.path.join(output_dir, image_file), noisy_image)


"""white block noise"""
# # Define the directory with the original images and the directory for the noisy images
# input_dir = "/home/danica01/raid1-data1/dan/dataset/nerf_synthetic/lego/train"
# output_dir = '/home/danica01/raid1-data1/dan/dataset/nerf_synthetic/lego/train-blocknoise'

# # Create the output directory if it doesn't exist
# os.makedirs(output_dir, exist_ok=True)

# # Get a list of all image files in the input directory
# image_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

# # Define the size of the noise block
# block_size = 80

# # Loop over each image file
# for image_file in image_files:
#     # Load the image
#     image = cv2.imread(os.path.join(input_dir, image_file))

#     # Define the central region
#     central_region = image[image.shape[0]//4:3*image.shape[0]//4, image.shape[1]//4:3*image.shape[1]//4]

#     # Generate a random position within the central region
#     x = np.random.randint(0, central_region.shape[1] - block_size)
#     y = np.random.randint(0, central_region.shape[0] - block_size)

#     # Add white block noise to the image
#     noisy_image = image.copy()
#     noisy_image[y:y+block_size, x:x+block_size] = 255

#     # Save the noisy image
#     cv2.imwrite(os.path.join(output_dir, image_file), noisy_image)


"""evenly distributed white blocks (block size 40x40, gap 10)"""
# Define the directory with the original images and the directory for the noisy images
input_dir = "/home/danica01/raid1-data1/dan/dataset/nerf_synthetic/lego/train"
output_dir = '/home/danica01/raid1-data1/dan/dataset/nerf_synthetic/lego/train-8block32gap-noise'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Get a list of all image files in the input directory
image_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

# Define the size of the white blocks and the gap between blocks
block_size = 8
gap_size = 32

# Loop over each image file
for image_file in image_files:
    # Load the image
    image = cv2.imread(os.path.join(input_dir, image_file))

    # Add white blocks to evenly distributed positions across the image
    for i in range(block_size, image.shape[0], block_size + gap_size):
        for j in range(block_size, image.shape[1], block_size + gap_size):
            image[i-block_size:i, j-block_size:j] = 255

    # Save the noisy image
    cv2.imwrite(os.path.join(output_dir, image_file), image)