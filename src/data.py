import os

from PIL import Image
import matplotlib.pyplot as plt
import random

import tensorflow as tf
from tensorflow.keras import layers, models

data_dir = "data"

categories = os.listdir(data_dir)
print("Categories:", categories)

for category in categories:
    path = os.path.join(data_dir, category)
    print(f"{category} has {len(os.listdir(path))} images")


def show_sample_images(data_dir, categories, samples_per_category=3):
    plt.figure(figsize=(10, 5))
    
    for i, category in enumerate(categories):
        path = os.path.join(data_dir, category)
        images = os.listdir(path)
        sample_images = random.sample(images, samples_per_category)
        
        for j, img_name in enumerate(sample_images):
            img_path = os.path.join(path, img_name)
            img = Image.open(img_path)
            plt.subplot(len(categories), samples_per_category, i*samples_per_category + j + 1)
            plt.imshow(img)
            plt.axis("off")
            plt.title(category)
    plt.show()

show_sample_images(data_dir, categories)