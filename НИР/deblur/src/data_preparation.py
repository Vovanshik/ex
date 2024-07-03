#data_preparation.py
import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from sklearn.model_selection import train_test_split

def load_images_from_folder(folder, target_size=(256, 256)):
    images = []
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        img = load_img(img_path, target_size=target_size)
        img_array = img_to_array(img) / 255.0
        images.append(img_array)
    return np.array(images)

def prepare_data(dataset_path):
    motion_blurred_path = os.path.join(dataset_path, 'blurry')
    sharp_path = os.path.join(dataset_path, 'sharp')

    motion_blurred_images = load_images_from_folder(motion_blurred_path)
    sharp_images = load_images_from_folder(sharp_path)

    motion_train, motion_test, sharp_train, sharp_test = train_test_split(motion_blurred_images, sharp_images, test_size=0.2, random_state=42)
    return motion_train, motion_test, sharp_train, sharp_test

