# Following imports based on ChatGPT recommendations to accomplish tasks in project
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import requests
import io

# Following functions based on multiple requests to ChatGPT to import the csv files
# Function to download and load CSV files
def load_csv_from_github(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Read the CSV from the content
        return pd.read_csv(io.StringIO(response.text), header=None).values
    else:
        raise Exception(f"Failed to download file from {url}, status code: {response.status_code}")
        
# Load the bands
red_band = load_csv_from_github("https://raw.githubusercontent.com/bcunningham40/SS1100_FinalProject_Group4/refs/heads/main/Payload/red.csv")
green_band = load_csv_from_github('https://raw.githubusercontent.com/bcunningham40/SS1100_FinalProject_Group4/refs/heads/main/Payload/green.csv')
blue_band = load_csv_from_github('https://raw.githubusercontent.com/bcunningham40/SS1100_FinalProject_Group4/refs/heads/main/Payload/blue.csv')

# Replace 'not a number' with a specific value (adapted from ChatGPT recommendation for correcting all while image)
red_band = np.nan_to_num(red_band, nan=0)
green_band = np.nan_to_num(green_band, nan=0)
blue_band = np.nan_to_num(blue_band, nan=0)

# Following function based on multiple requests to ChatGPT to help plot the proper image and arrange the code correctly
def visualize_rgb_bands(red_csv, green_csv, blue_csv):
    """Process R, G, and B band CSV files and visualize a single RGB image."""
   
    # Ensure that all bands have the same dimensions
    if not (red_band.shape == green_band.shape == blue_band.shape):
        raise ValueError("All bands must have the same dimensions.")

    # Combine the bands into a single RGB image
    rgb_image = np.stack((red_band, green_band, blue_band), axis=-1)

    # Normalize the data for visualization (assuming radiance values are not in 0-255 range)
    rgb_image_normalized = (rgb_image - rgb_image.min()) / (rgb_image.max() - rgb_image.min())
    rgb_image_normalized = np.clip(rgb_image_normalized, 0, 1)  # Ensure the values are within [0, 1]

    # Visualize the RGB image
    plt.figure(figsize=(10, 10))  # Increased figure size for better visualization
    plt.imshow(rgb_image_normalized)
    plt.title("RGB Image", fontsize=16)
    plt.axis('off')  # Turn off axes for a cleaner look
    plt.tight_layout()
    plt.show()
    
    return rgb_image_normalized

# Following function based on multiple requests to ChatGPT to help plot the proper image and arrange the code correctly
def convert_to_reflectance(rgb_image, k=0.8, b=0.1):
    """Convert radiance values in the RGB image to reflectance values.
    
    Parameters:
    rgb_image (numpy.ndarray): The RGB image array created earlier.
    k (float): Multiplicative scaling factor (default: 0.8).
    b (float): Additive scaling factor (default: 0.1).
    
    Returns:
    numpy.ndarray: Rescaled image where each pixel is in the range [0, 1].
    """
    # Apply the scaling factors
    reflectance_image = k * rgb_image + b

    # Rescale the image to the range [0, 1]
    reflectance_image = np.clip(reflectance_image, 0, 1)  # Ensure no values fall outside the range [0, 1]
    
    return reflectance_image

rgb_image_normalized = visualize_rgb_bands(red_band, green_band, blue_band)

# Assuming `rgb_image_normalized` is the RGB image created in the previous task
reflectance_image = convert_to_reflectance(rgb_image_normalized)

# Visualize the converted image
plt.figure(figsize=(10, 10))
plt.imshow(reflectance_image)
plt.title("Reflectance Image", fontsize=16)
plt.axis('off')  # Turn off axes for a cleaner look
plt.tight_layout()
plt.show()

# Following functions based on multiple requests to ChatGPT to help plot the proper image and arrange the code correctly
def reflectance_convert_to_8bit(reflectance_image):
    """
    Convert a reflectance image to an 8-bit digital number (DN) representation.

    Parameters:
    reflectance_image (numpy.ndarray): The reflectance image with values in the range [0, 1].

    Returns:
    numpy.ndarray: An image with values scaled to the range [0, 255] as integers.
    """
    # Scale the reflectance values to the range [0, 255]
    image_8bit = reflectance_image * 255

    # Convert the scaled values to integers
    image_8bit = image_8bit.astype(np.uint8)

    return image_8bit

# Convert the reflectance image to 8-bit DN values
image_8bit = reflectance_convert_to_8bit(reflectance_image)

# Visualize the 8-bit image
plt.figure(figsize=(10, 10))
plt.imshow(image_8bit)
plt.title("8-bit Digital Number Image", fontsize=16)
plt.axis('off')
plt.tight_layout()
plt.show()

import os
from PIL import Image

# Following function based on multiple requests to ChatGPT to help use os to save the file
def save_image(image, file_name, folder_location, file_format="png"):
    """Save an image to a file in the specified format and location.

    Parameters:
    image (numpy.ndarray): The image to save (expected in 8-bit format).
    file_name (str): Name of the file (without extension).
    folder_location (str): Path to the folder where the file will be saved.
    file_format (str): The file format to use (e.g., "png" or "jpeg"). Default is "png".

    Returns:
    str: Full path to the saved image file.
    """
    # Ensure the folder exists
    os.makedirs(folder_location, exist_ok=True)

    # Construct the full file path
    file_path = os.path.join(folder_location, f"{file_name}.{file_format}")

    # Convert the image to PIL format and save
    image_to_save = Image.fromarray(image)
    image_to_save.save(file_path, format=file_format.upper())

    print(f"Image saved successfully to: {file_path}")
    return file_path

# Save the 8-bit image
file_name = "reflectance_image_8bit"
folder_location = "./output_images"
save_image(image_8bit, file_name, folder_location)

# Save the 8-bit image
file_name = "reflectance_image_8bit"
folder_location = "./output_images"
save_image(image_8bit, file_name, folder_location)
