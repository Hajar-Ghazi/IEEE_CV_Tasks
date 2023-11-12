#import necessary libraries
import os
import zipfile
import cv2

# Path to the ZIP file
zip_file = 'folders.zip'

# Extract the contents of the ZIP file to a temporary directory
temp_dir = ''
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(temp_dir)


subfolders = [f.path for f in os.scandir(temp_dir) if f.is_dir()]
print(subfolders)
# Iterate over the subfolders
for subfolder in subfolders:

    # Create a new folder for the output images
    output_folder = os.path.join(subfolder, 'output')
    os.makedirs(output_folder, exist_ok=True)
    

    # Get a list of image files in the subfolder
    image_files = [f.path for f in os.scandir(subfolder) if f.is_file() and f.name.endswith(('.jpg', '.png'))]


    # Iterate over the image files
    for image_file in image_files:
        # Load the image
        image = cv2.imread(image_file,cv2.IMREAD_UNCHANGED)
        cv2.imshow(' original image',image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        #ask user to enter the blurring method  that he prefers
        print('Which blurring method do you prefer for the image shown previously? ')
        blur_method= int(input('Enter 1 for Blur method  and 2 for MedianBlur method and 3 for GaussianBlur method and 4 for Bilateral method'))

        if  blur_method == 1 :
          blurred_image= cv2.blur(image, ksize = (5,5))
        elif  blur_method == 2 :
          blurred_image= cv2.medianBlur(image, 5)
        elif  blur_method == 3 :
          blurred_image= cv2.GaussianBlur(image, ksize = (5,5), sigmaX = 0)
        elif  blur_method == 4 : 
          blurred_image= cv2.bilateralFilter(image, 5, sigmaSpace = 75, sigmaColor =75)

        #display blurred image before saving 
        cv2.imshow('blurred image', blurred_image )
        cv2.waitKey(0)
        cv2.destroyAllWindows()

         # Save the blurred image
        output_file = os.path.join(output_folder, os.path.basename(image_file))
        cv2.imwrite(output_file, blurred_image)
