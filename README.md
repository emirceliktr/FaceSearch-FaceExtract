## Installation

The easiest way to install retinaface is to download it from [PyPI](https://pypi.org/project/retina-face/). It's going to install the library itself and its prerequisites as well.

```
pip install retina-face
```

Then, you will be able to import the library and use its functionalities.

```
from retinaface import RetinaFace
```

**Face Detection**

RetinaFace offers a face detection function. It expects an exact path of an image as input.

```python
resp = RetinaFace.detect_faces("img1.jpg")
```

Then, it will return the facial area coordinates and some landmarks (eyes, nose and mouth) with a confidence score.

```json
{
    "face_1": {
        "score": 0.9993440508842468,
        "facial_area": [155, 81, 434, 443],
        "landmarks": {
          "right_eye": [257.82974, 209.64787],
          "left_eye": [374.93427, 251.78687],
          "nose": [303.4773, 299.91144],
          "mouth_right": [228.37329, 338.73193],
          "mouth_left": [320.21982, 374.58798]
        }
  }
}
```
**Face Extraction**

```python
import matplotlib.pyplot as plt
faces = RetinaFace.extract_faces(img_path = "img.jpg", align = True)
for face in faces:
  plt.imshow(face)
  plt.show()
```

**Face Recognition** 

##Installation 
The easiest way to install deepface is to download it from [PyPI](https://pypi.org/project/retina-face/). It's going to install the library itself and its prerequisites as well.


To install deepface pakage
```
#!pip install deepface
```

To use deepface in order to recognise a face
```
from deepface import DeepFace
obj = DeepFace.verify("img1.jpg", "img2.jpg"
          , model_name = 'ArcFace', detector_backend = 'retinaface')
print(obj["verified"])
```

To use deep face in order to search a face in a database

```
from deepface import DeepFace
import pandas


df = DeepFace.find(img_path = "img1.jpg", db_path = "C:/workspace/my_db")

print(df.head())

```
