import pickle
import numpy as np
from PIL import Image
from tensorflow import keras

#Needs TensorFlow

with open("Projects\ML\CNNModel.pkl", "rb") as f:
    model = pickle.load(f)
with open("Projects\ML\img.pkl", "rb") as f:
    img = np.load(f, allow_pickle=True)

print(img.shape)
