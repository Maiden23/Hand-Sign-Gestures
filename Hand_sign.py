import glob
import nltk
import os
import numpy as np

for files in os.listdir("C:/Users/angel/OneDrive/Documents/3rd year/sem2/NLP/Hand-Sign-Gestures/Dataset of Common phrases in Indian Sign Language/MP_Data"):
    print(files)

import matplotlib

from pathlib import Path

#Reading All the Folders 
all_folders = Path("C:/Users/angel/OneDrive/Documents/3rd year/sem2/NLP/Hand-Sign-Gestures/Dataset of Common phrases in Indian Sign Language/MP_Data")
all_files = list(all_folders.rglob(".*npy"))
for file in all_files:
    all_folder = np.load(file)
    print(all_folder)
