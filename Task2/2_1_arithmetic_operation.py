#import necessary libraries
import numpy as np
import cv2

#read value of brightness_factor from user 
brightness_factor= int(input(" Enter the brightness_factor : "))

#read an image 
img= cv2.imread("1.jpg")

#size of input image
h,w,c=img.shape

#create brightness_matrix with same size of readed image 
brightness_matrix= np.ones((h,w,c), dtype="uint8")* abs(brightness_factor)


#To increase brightness of an image
if brightness_factor > 0 :
  add_image=cv2.add(img , brightness_matrix)
  cv2.imshow("adjusted_image",add_image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

#To decrease brightness of an image 
elif brightness_factor <0 :
  subtract_image= cv2.subtract(img ,brightness_matrix)
  cv2.imshow("adjusted_image",subtract_image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
