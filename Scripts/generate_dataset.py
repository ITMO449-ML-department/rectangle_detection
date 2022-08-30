import cv2
import numpy as np
from pathlib import Path
import sys


PICTURES_AMMOUNT = 500
DATASET_NAME = "Squares_test"


if __name__ == "__main__":
    try:
        DATASET_NAME = str(sys.argv[1])
        PICTURES_AMMOUNT = int(sys.argv[2])
    except:
        print("Invalid arguments (1st: Dataset name, 2d: Pictures ammount)")
        quit()

Path(f"Datasets/{DATASET_NAME}").mkdir(parents=True, exist_ok=True)

colors = [[0, 0, 0]]
f = open(f"Datasets/{DATASET_NAME}/labels.txt", "w")
for i in range(PICTURES_AMMOUNT):
    x, y = np.random.randint(20,235,size=(2))
    center = [x, y]
    max_R = min(x, 255-x,y,255-y)
    angle = np.random.randint(0, 180)
    a = np.random.randint(10,int(1.6*max_R))
    b = int(np.sqrt(4 * max_R**2 - a**2))
    size = np.array([a, b])

    rect = ((int(center[0]), int(center[1])), (int(size[0]), int(size[1])), int(angle))
    box = cv2.boxPoints(rect)  # cv2.boxPoints(rect) for OpenCV 3.x
    box = np.int0(box)
    whiteblankimage = 255 * np.ones(shape=[256, 256, 3], dtype=np.uint8)
    cv2.drawContours(whiteblankimage, [box], 0, (0, 0, 0), thickness=cv2.FILLED)
    cv2.imwrite(f"Datasets/{DATASET_NAME}/{center[0]}_{center[1]}_{size[0]}_{size[1]}_{angle}.jpeg", whiteblankimage)
    f.write(f"{center[0]}_{center[1]}_{size[0]}_{size[1]}_{angle}.jpeg {center[0]}_{center[1]}_{size[0]}_{size[1]}_{angle}\n")

f.close()