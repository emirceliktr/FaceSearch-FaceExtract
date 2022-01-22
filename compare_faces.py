from deepface import DeepFace
import cv2
import os
import sys

if len(sys.argv) != 3:
    print(
        "Missing argument. Please provide pathes for two images to compare"
        "Usage example: python3 extract_faces.py ./image1.jpg image2.jpg\n"
    )
    exit()


def compareFaces(path1,path2):
    img1 = path1
    img2 = path2
    
    obj = DeepFace.verify(img1, img2
          , model_name = 'ArcFace', detector_backend = 'retinaface')
    #print(obj["verified"])

    if obj["verified"]:
        print(f'ayni kisiye ait oldugu doğrulandi. Benzerlik icin distance: {obj["distance"]}')
        
    else:
        print(f'ayni kisiye ait oldugu doğrulanamadi. Benzerlik icin distance: {obj["distance"]}')

compareFaces(sys.argv[1],sys.argv[2])
