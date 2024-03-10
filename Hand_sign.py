import glob
import nltk
import os

for files in os.listdir("C:/Users/angel/OneDrive/Documents/3rd year/sem2/NLP/Hand-Sign-Gestures\Dataset of Common phrases in Indian Sign Language/MP_Data"):
    print(files)

filenames = glob.glob("*.npy")