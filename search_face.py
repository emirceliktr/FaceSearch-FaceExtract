
from deepface import DeepFace
import matplotlib.pyplot as plt
import cv2
import os
import sys

if len(sys.argv) != 3:
    print(
         "Missing argument. Please provide a path to the\n"
         "tester_image and image_set taht you want to look.\n"
        "Usage example: python3 search_face.py ./test.jpg ./images\n"
    )
    exit()


def searchFace(path1,path2): 

    df = DeepFace.find(img_path = path1, db_path = path2, model_name = models[1])

searchFace(path1,path2)
