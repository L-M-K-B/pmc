import os

import cv2

folder = os.listdir('images')

for item in folder:
    img = cv2.imread(os.path.join('images', item), 0)
    re_img = cv2.resize(img, (100, 100))
    cv2.imshow('resized_image', re_img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

