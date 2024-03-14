import glob
import nltk
import os
import numpy as np

for files in os.listdir("C:/Users/angel/OneDrive/Documents/3rd year/sem2/NLP/Hand-Sign-Gestures/Dataset of Common phrases in Indian Sign Language/MP_Data"):
    print(files)

import matplotlib.pyplot as plt

from pathlib import Path
from PIL import Image
import cv2

#Checking with an individual file
bad_file = Path("C:/Users/angel/OneDrive/Documents/3rd year/sem2/NLP/Hand-Sign-Gestures/Dataset of Common phrases in Indian Sign Language/MP_Data/car/0/0.npy")
bad = np.load(bad_file)
print(len(bad))
#cv2.imwrite("bad.png",bad)
#cv2.imshow("Image",bad)
img_w , img_h = 512,512
img = Image.fromarray(bad,"RGB")
img.show()

#Sample checking
'''car_folder = Path("C:/Users/angel/OneDrive/Documents/3rd year/sem2/NLP/Hand-Sign-Gestures/Dataset of Common phrases in Indian Sign Language/MP_Data/car/0")
car_files = list(car_folder.rglob("*.npy"))
for file in car_files:
    car = np.load(file)
    print(car)'''
    #cv2.imwrite()
    #img.save("car.png")
    #img.show()
    #print(car)

#Reading All the Folders
'''
all_folders = Path("C:/Users/angel/OneDrive/Documents/3rd year/sem2/NLP/Hand-Sign-Gestures/Dataset of Common phrases in Indian Sign Language/MP_Data")
all_files = list(all_folders.rglob("*.npy"))
for file in all_files:
   all_folder = np.load(file)
   print(all_folder)
'''


