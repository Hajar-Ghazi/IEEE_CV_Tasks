import numpy as np
import cv2

img = cv2.imread('IEEE.jpg')


rimg = cv2.resize(img, (600,600))

cv2.imwrite('IEEE_600x600.jpg',rimg)
