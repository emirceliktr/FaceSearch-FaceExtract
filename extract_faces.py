
from retinaface import RetinaFace
import matplotlib.pyplot as plt
import cv2
import os
import sys

if len(sys.argv) != 2:
    print(
        "Missing argument. Please provide a path to the\n"
        "image or images that you want to extract faces.\n"
        "Usage example: python3 extract_faces.py images\n"
    )
    exit()


def extractFace(path):
    img_path = path
    IMG_DIR = img_path+"_extracted_faces"

    #çıkarılan yüzleri yeni bir klasör oluşturarak kaydediyoruz
    if not os.path.exists(IMG_DIR):
            os.makedirs(IMG_DIR)
            
    #resimleri for döngüsü ile teker teker okuyoruz
    for filePath in (os.listdir(img_path)):
        if filePath.endswith(".jpg") or filePath.endswith("jpeg") or filePath.endswith("png"):

            #resimlerden yüzleri çıkarıyoruz
            resp = RetinaFace.extract_faces(img_path = os.path.join(img_path,filePath), align = True)
            
            #her resimde tek yüz olmayabilir
            #birden fazla yüz varsa onları ayrı ayrı kaydetmek için
            #isimlerini sayac kullanarak ardışık olarak tanımlayalım            
            if len(resp)>1:
                sayac = 1
                for img in resp:
                    #plt.imshow(img)
                    #plt.axis('off')
                    #plt.show()
                    name = 'face_'+sayac+filePath
                    sayac =+1
                    cv2.imwrite(os.path.join(IMG_DIR,name), img[:, :, ::-1])
                    print(f'resim {name} başarili bir sekilde kaydedildi.')
            else:
                cv2.imwrite(os.path.join(IMG_DIR,filePath), resp[0][:, :, ::-1])
                print(f'resim {filePath} başarili bir sekilde kaydedildi.')
            


extractFace(sys.argv[1])
