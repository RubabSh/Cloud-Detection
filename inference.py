import os
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from losses import jaccard_loss
from glob import glob
import shutil

# Parameters
INPUT_SHAPE = (192, 192, 3)
THRESHOLD = 0.5
CLOUD_PERCENT_THRESHOLD = 0.2
TEST_IMG_DIR = 'dataset/Test'
MODEL_PATH = 'model.h5'

# Output folders
CLOUD_DIR = 'dataset/Cloud'
NO_CLOUD_DIR = 'dataset/No_Cloud'

os.makedirs(CLOUD_DIR, exist_ok=True)
os.makedirs(NO_CLOUD_DIR, exist_ok=True)


# Load model
model = load_model(MODEL_PATH, custom_objects={'dice_loss': jaccard_loss})
print(f"Model loaded from {MODEL_PATH}")

# Supported image extensions
image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tif', '.webp')

# Get image file names for all supported extensions
image_paths = []
for ext in image_extensions:
    image_paths.extend(glob(os.path.join(TEST_IMG_DIR, f'*{ext}')))

# Sort image paths
image_paths = sorted(image_paths)

# Print the number of images found
print(f"Found {len(image_paths)} test images")


# Loop through and classify based on cloud coverage
for img_path in image_paths:
    img_name = os.path.basename(img_path)
    # Load and preprocess image
    img = load_img(img_path, target_size=INPUT_SHAPE)
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict mask
    pred_mask = model.predict(img_array)[0, :, :, 0]
    binary_mask = (pred_mask > THRESHOLD).astype(np.uint8)

    # Compute cloud percentage
    cloud_pixels = np.sum(binary_mask)
    total_pixels = binary_mask.size
    cloud_percentage = cloud_pixels / total_pixels

    # Move original image based on cloud coverage
    if cloud_percentage > CLOUD_PERCENT_THRESHOLD:
        dest_path = os.path.join(CLOUD_DIR, img_name)
        category = "Cloud"
    else:
        dest_path = os.path.join(NO_CLOUD_DIR, img_name)
        category = "No Cloud"

    shutil.copy(img_path, dest_path)
    print(f"{category} → {dest_path}")

print("All images classified based on cloud coverage.")