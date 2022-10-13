# importing modules
from skimage.io import imread
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt
import numpy as np
import math

# reading images
image1 = imread("animals\crab\c1.JPG")
image2 = imread("animals\crab\c2.JPG")
image3 = imread("animals\crab\c3.JPG")
image4 = imread("animals\crab\c4.JPG")
image5 = imread("animals\crab\c5.JPG")
image6 = imread("animals\crab\c6.JPG")
image7 = imread("animals\crab\c7.JPG")
image8 = imread("animals\crab\c8.JPG")
image9 = imread("animals\crab\c9.JPG")
image10 = imread("animals\crab\c10.JPG")
image11 = imread("animals\dolphin\d1.JPG")
image12 = imread("animals\dolphin\d2.JPG")
image13 = imread("animals\dolphin\d3.JPG")
image14 = imread("animals\dolphin\d4.JPG")
image15 = imread("animals\dolphin\d5.JPG")
image16 = imread("animals\dolphin\d6.JPG")
image17 = imread("animals\dolphin\d7.JPG")
image18 = imread("animals\dolphin\d8.JPG")
image19 = imread("animals\dolphin\d9.JPG")
image20 = imread("animals\dolphin\d10.JPG")

# resizing original images and visualizing images
print("Image 1 original size= ", image1.shape)
resize_image1 = resize(image1, (128,64))
print("Image 1 new size= ", resize_image1.shape)
figure1, (x1, x2) = plt.subplots(1, 2)
x1.imshow(image1, cmap=plt.cm.gray)
x1.set_title('Input image1')
x2.imshow(resize_image1, cmap=plt.cm.gray)
x2.set_title('Resized Image 1')
plt.show()

print("Image 2 original size= ", image2.shape)
resize_image2 = resize(image2, (128,64))
print("Image 2 new size= ", resize_image2.shape)
figure2, (x1, x2) = plt.subplots(1, 2)
x1.imshow(image2, cmap=plt.cm.gray)
x1.set_title('Input image2')
x2.imshow(resize_image2, cmap=plt.cm.gray)
x2.set_title('Resized Image 2')
plt.show()

print("Image 3 original size= ", image3.shape)
resize_image3 = resize(image3, (128,64))
print("Image 3 new size= ", resize_image3.shape)
figure3, (x1, x2) = plt.subplots(1, 2)
x1.imshow(image3, cmap=plt.cm.gray)
x1.set_title('Input image3')
x2.imshow(resize_image3, cmap=plt.cm.gray)
x2.set_title('Resized Image 3')
plt.show()

print("Image 4 original size= ", image4.shape)
resize_image4 = resize(image4, (128,64))
print("Image 4 new size= ", resize_image4.shape)
figure4, (x1, x2) = plt.subplots(1, 2)
x1.imshow(image4, cmap=plt.cm.gray)
x1.set_title('Input image4')
x2.imshow(resize_image4, cmap=plt.cm.gray)
x2.set_title('Resized Image 4')
plt.show()

print("Image 5 original size= ", image5.shape)
resize_image5 = resize(image5, (128,64))
print("Image 5 new size= ", resize_image5.shape)
figure5, (x1, x2) = plt.subplots(1, 2)
x1.imshow(image5, cmap=plt.cm.gray)
x1.set_title('Input image5')
x2.imshow(resize_image5, cmap=plt.cm.gray)
x2.set_title('Resized Image 5')
plt.show()

print("Image 6 original size= ", image6.shape)
resize_image6 = resize(image6, (128,64))
print("Image 6 new size= ", resize_image6.shape)
figure6, (x1, x2) = plt.subplots(1, 2)
x1.imshow(image6, cmap=plt.cm.gray)
x1.set_title('Input image6')
x2.imshow(resize_image6, cmap=plt.cm.gray)
x2.set_title('Resized Image 6')
plt.show()

print("Image 7 original size= ", image7.shape)
resize_image7 = resize(image7, (128,64))
print("Image 7 new size= ", resize_image7.shape)
figure7, (x1, x2) = plt.subplots(1, 2)
x1.imshow(image7, cmap=plt.cm.gray)
x1.set_title('Input image7')
x2.imshow(resize_image7, cmap=plt.cm.gray)
x2.set_title('Resized Image 7')
plt.show()

print("Image 8 original size= ", image8.shape)
resize_image8 = resize(image8, (128,64))
print("Image 8 new size= ", resize_image8.shape)
figure8, (x1, x2) = plt.subplots(1, 2)
x1.imshow(image8, cmap=plt.cm.gray)
x1.set_title('Input image8')
x2.imshow(resize_image8, cmap=plt.cm.gray)
x2.set_title('Resized Image 8')
plt.show()

print("Image 9 original size= ", image9.shape)
resize_image9 = resize(image9, (128,64))
print("Image 9 new size= ", resize_image9.shape)
figure9, (x1, x2) = plt.subplots(1, 2)
x1.imshow(image9, cmap=plt.cm.gray)
x1.set_title('Input image9')
x2.imshow(resize_image9, cmap=plt.cm.gray)
x2.set_title('Resized Image 9')
plt.show()

print("Image 10 original size= ", image10.shape)
resize_image10 = resize(image10, (128,64))
print("Image 10 new size= ", resize_image10.shape)
figure10, (x1, x2) = plt.subplots(1, 2)
x1.imshow(image10, cmap=plt.cm.gray)
x1.set_title('Input image10')
x2.imshow(resize_image10, cmap=plt.cm.gray)
x2.set_title('Resized Image 10')
plt.show()

print("Image 11 original size= ", image11.shape)
resize_image11 = resize(image11, (128,64))
print("Image 11 new size= ", resize_image11.shape)
figure11, (x1, x2) = plt.subplots(1, 2)
x1.imshow(image11, cmap=plt.cm.gray)
x1.set_title('Input image11')
x2.imshow(resize_image11, cmap=plt.cm.gray)
x2.set_title('Resized Image 11')
plt.show()

print("Image 12 original size= ", image12.shape)
resize_image12 = resize(image12, (128,64))
print("Image 12 new size= ", resize_image12.shape)
figure12, (x1, x2) = plt.subplots(1, 2)
x1.imshow(image12, cmap=plt.cm.gray)
x1.set_title('Input image12')
x2.imshow(resize_image12, cmap=plt.cm.gray)
x2.set_title('Resized Image 12')
plt.show()

print("Image 13 original size= ", image13.shape)
resize_image13 = resize(image13, (128,64))
print("Image 13 new size= ", resize_image13.shape)
figure13, (x1, x2) = plt.subplots(1, 2)
x1.imshow(image13, cmap=plt.cm.gray)
x1.set_title('Input image13')
x2.imshow(resize_image13, cmap=plt.cm.gray)
x2.set_title('Resized Image 13')
plt.show()

print("Image 14 original size= ", image14.shape)
resize_image14 = resize(image14, (128,64))
print("Image 14 new size= ", resize_image14.shape)
figure14, (x1, x2) = plt.subplots(1, 2)
x1.imshow(image14, cmap=plt.cm.gray)
x1.set_title('Input image14')
x2.imshow(resize_image14, cmap=plt.cm.gray)
x2.set_title('Resized Image 14')
plt.show()

print("Image 15 original size= ", image15.shape)
resize_image15 = resize(image15, (128,64))
print("Image 15 new size= ", resize_image15.shape)
figure15, (x1, x2) = plt.subplots(1, 2)
x1.imshow(image15, cmap=plt.cm.gray)
x1.set_title('Input image15')
x2.imshow(resize_image15, cmap=plt.cm.gray)
x2.set_title('Resized Image 15')
plt.show()

print("Image 16 original size= ", image16.shape)
resize_image16 = resize(image16, (128,64))
print("Image 16 new size= ", resize_image16.shape)
figure16, (x1, x2) = plt.subplots(1, 2)
x1.imshow(image16, cmap=plt.cm.gray)
x1.set_title('Input image16')
x2.imshow(resize_image16, cmap=plt.cm.gray)
x2.set_title('Resized Image 16')
plt.show()

print("Image 17 original size= ", image17.shape)
resize_image17 = resize(image17, (128,64))
print("Image 17 new size= ", resize_image17.shape)
figure17, (x1, x2) = plt.subplots(1, 2)
x1.imshow(image17, cmap=plt.cm.gray)
x1.set_title('Input image17')
x2.imshow(resize_image17, cmap=plt.cm.gray)
x2.set_title('Resized Image 17')
plt.show()

print("Image 18 original size= ", image18.shape)
resize_image18 = resize(image18, (128,64))
print("Image 18 new size= ", resize_image18.shape)
figure18, (x1, x2) = plt.subplots(1, 2)
x1.imshow(image18, cmap=plt.cm.gray)
x1.set_title('Input image18')
x2.imshow(resize_image18, cmap=plt.cm.gray)
x2.set_title('Resized Image 18')
plt.show()

print("Image 19 original size= ", image19.shape)
resize_image19 = resize(image19, (128,64))
print("Image 19 new size= ", resize_image19.shape)
figure19, (x1, x2) = plt.subplots(1, 2)
x1.imshow(image19, cmap=plt.cm.gray)
x1.set_title('Input image19')
x2.imshow(resize_image19, cmap=plt.cm.gray)
x2.set_title('Resized Image 19')
plt.show()

print("Image 20 original size= ", image20.shape)
resize_image20 = resize(image20, (128,64))
print("Image 20 new size= ", resize_image20.shape)
figure20, (x1, x2) = plt.subplots(1, 2)
x1.imshow(image20, cmap=plt.cm.gray)
x1.set_title('Input image20')
x2.imshow(resize_image20, cmap=plt.cm.gray)
x2.set_title('Resized Image 20')
plt.show()

feature_matrix1, HOG_image1 = hog(resize_image1, orientations=9, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, channel_axis=2)
print("Total extracted features for Image 1= ", feature_matrix1.shape)


feature_matrix2, HOG_image2 = hog(resize_image2, orientations=9, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, channel_axis=2)
print("Total extracted features for Image 2= ", feature_matrix2.shape)


feature_matrix3, HOG_image3 = hog(resize_image3, orientations=9, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, channel_axis=2)
print("Total extracted features for Image 3= ", feature_matrix3.shape)


feature_matrix4, HOG_image4 = hog(resize_image4, orientations=9, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, channel_axis=2)
print("Total extracted features for Image 4= ", feature_matrix4.shape)


feature_matrix5, HOG_image5 = hog(resize_image5, orientations=9, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, channel_axis=2)
print("Total extracted features for Image 5= ", feature_matrix5.shape)


feature_matrix6, HOG_image6 = hog(resize_image6, orientations=9, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, channel_axis=2)
print("Total extracted features for Image 6= ", feature_matrix6.shape)


feature_matrix7, HOG_image7 = hog(resize_image7, orientations=9, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, channel_axis=2)
print("Total extracted features for Image 7= ", feature_matrix7.shape)


feature_matrix8, HOG_image8 = hog(resize_image8, orientations=9, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, channel_axis=2)
print("Total extracted features for Image 8= ", feature_matrix8.shape)


feature_matrix9, HOG_image9 = hog(resize_image9, orientations=9, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, channel_axis=2)
print("Total extracted features for Image 9= ", feature_matrix9.shape)


feature_matrix10, HOG_image10 = hog(resize_image10, orientations=9, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, channel_axis=2)
print("Total extracted features for Image 10= ", feature_matrix10.shape)


feature_matrix11, HOG_image11 = hog(resize_image11, orientations=9, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, channel_axis=2)
print("Total extracted features for Image 11= ", feature_matrix11.shape)


feature_matrix12, HOG_image12 = hog(resize_image12, orientations=9, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, channel_axis=2)
print("Total extracted features for Image 12= ", feature_matrix12.shape)


feature_matrix13, HOG_image13 = hog(resize_image13, orientations=9, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, channel_axis=2)
print("Total extracted features for Image 13= ", feature_matrix13.shape)


feature_matrix14, HOG_image14 = hog(resize_image14, orientations=9, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, channel_axis=2)
print("Total extracted features for Image 14= ", feature_matrix14.shape)


feature_matrix15, HOG_image15 = hog(resize_image15, orientations=9, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, channel_axis=2)
print("Total extracted features for Image 15= ", feature_matrix15.shape)


feature_matrix16, HOG_image16 = hog(resize_image16, orientations=9, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, channel_axis=2)
print("Total extracted features for Image 16= ", feature_matrix16.shape)


feature_matrix17, HOG_image17 = hog(resize_image17, orientations=9, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, channel_axis=2)
print("Total extracted features for Image 17= ", feature_matrix17.shape)


feature_matrix18, HOG_image18 = hog(resize_image18, orientations=9, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, channel_axis=2)
print("Total extracted features for Image 18= ", feature_matrix18.shape)


feature_matrix19, HOG_image19 = hog(resize_image19, orientations=9, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, channel_axis=2)
print("Total extracted features for Image 19= ", feature_matrix19.shape)


feature_matrix20, HOG_image20 = hog(resize_image20, orientations=9, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, channel_axis=2)
print("Total extracted features for Image 20= ", feature_matrix20.shape)

figure21, (x1, x2) = plt.subplots(1, 2)
x1.imshow(resize_image1, cmap=plt.cm.gray)
x1.set_title('Image 1')
# Rescale histogram for better display
HOG_feature_image1_rescale = exposure.rescale_intensity(HOG_image1, in_range=(0, 10))
x2.imshow(HOG_feature_image1_rescale, cmap=plt.cm.gray)
x2.set_title('(HOG) Histogram of Oriented Gradients for Image 1')
plt.show()

figure22, (x1, x2) = plt.subplots(1, 2)
x1.imshow(resize_image2, cmap=plt.cm.gray)
x1.set_title('Image 2')
# Rescale histogram for better display
HOG_feature_image2_rescale = exposure.rescale_intensity(HOG_image2, in_range=(0, 10))
x2.imshow(HOG_feature_image2_rescale, cmap=plt.cm.gray)
x2.set_title('(HOG) Histogram of Oriented Gradients for Image 2')
plt.show()

figure23, (x1, x2) = plt.subplots(1, 2)
x1.imshow(resize_image3, cmap=plt.cm.gray)
x1.set_title('Image 3')
# Rescale histogram for better display
HOG_feature_image3_rescale = exposure.rescale_intensity(HOG_image3, in_range=(0, 10))
x2.imshow(HOG_feature_image3_rescale, cmap=plt.cm.gray)
x2.set_title('(HOG) Histogram of Oriented Gradients for Image 3')
plt.show()

figure24, (x1, x2) = plt.subplots(1, 2)
x1.imshow(resize_image4, cmap=plt.cm.gray)
x1.set_title('Image 4')
# Rescale histogram for better display
HOG_feature_image4_rescale = exposure.rescale_intensity(HOG_image4, in_range=(0, 10))
x2.imshow(HOG_feature_image4_rescale, cmap=plt.cm.gray)
x2.set_title('(HOG) Histogram of Oriented Gradients for Image 4')
plt.show()

figure25, (x1, x2) = plt.subplots(1, 2)
x1.imshow(resize_image5, cmap=plt.cm.gray)
x1.set_title('Image 5')
# Rescale histogram for better display
HOG_feature_image5_rescale = exposure.rescale_intensity(HOG_image5, in_range=(0, 10))
x2.imshow(HOG_feature_image5_rescale, cmap=plt.cm.gray)
x2.set_title('(HOG) Histogram of Oriented Gradients for Image 5')
plt.show()

figure26, (x1, x2) = plt.subplots(1, 2)
x1.imshow(resize_image6, cmap=plt.cm.gray)
x1.set_title('Image 6')
# Rescale histogram for better display
HOG_feature_image6_rescale = exposure.rescale_intensity(HOG_image6, in_range=(0, 10))
x2.imshow(HOG_feature_image6_rescale, cmap=plt.cm.gray)
x2.set_title('(HOG) Histogram of Oriented Gradients for Image 6')
plt.show()

figure27, (x1, x2) = plt.subplots(1, 2)
x1.imshow(resize_image7, cmap=plt.cm.gray)
x1.set_title('Image 7')
# Rescale histogram for better display
HOG_feature_image7_rescale = exposure.rescale_intensity(HOG_image7, in_range=(0, 10))
x2.imshow(HOG_feature_image7_rescale, cmap=plt.cm.gray)
x2.set_title('(HOG) Histogram of Oriented Gradients for Image 7')
plt.show()

figure28, (x1, x2) = plt.subplots(1, 2)
x1.imshow(resize_image8, cmap=plt.cm.gray)
x1.set_title('Image 8')
# Rescale histogram for better display
HOG_feature_image8_rescale = exposure.rescale_intensity(HOG_image8, in_range=(0, 10))
x2.imshow(HOG_feature_image8_rescale, cmap=plt.cm.gray)
x2.set_title('(HOG) Histogram of Oriented Gradients for Image 8')
plt.show()

figure29, (x1, x2) = plt.subplots(1, 2)
x1.imshow(resize_image9, cmap=plt.cm.gray)
x1.set_title('Image 9')
# Rescale histogram for better display
HOG_feature_image9_rescale = exposure.rescale_intensity(HOG_image9, in_range=(0, 10))
x2.imshow(HOG_feature_image9_rescale, cmap=plt.cm.gray)
x2.set_title('(HOG) Histogram of Oriented Gradients for Image 9')
plt.show()

figure30, (x1, x2) = plt.subplots(1, 2)
x1.imshow(resize_image10, cmap=plt.cm.gray)
x1.set_title('Image 10')
# Rescale histogram for better display
HOG_feature_image10_rescale = exposure.rescale_intensity(HOG_image10, in_range=(0, 10))
x2.imshow(HOG_feature_image10_rescale, cmap=plt.cm.gray)
x2.set_title('(HOG) Histogram of Oriented Gradients for Image 10')
plt.show()

figure31, (x1, x2) = plt.subplots(1, 2)
x1.imshow(resize_image11, cmap=plt.cm.gray)
x1.set_title('Image 11')
# Rescale histogram for better display
HOG_feature_image11_rescale = exposure.rescale_intensity(HOG_image11, in_range=(0, 10))
x2.imshow(HOG_feature_image11_rescale, cmap=plt.cm.gray)
x2.set_title('(HOG) Histogram of Oriented Gradients for Image 11')
plt.show()

figure32, (x1, x2) = plt.subplots(1, 2)
x1.imshow(resize_image12, cmap=plt.cm.gray)
x1.set_title('Image 12')
# Rescale histogram for better display
HOG_feature_image12_rescale = exposure.rescale_intensity(HOG_image12, in_range=(0, 10))
x2.imshow(HOG_feature_image12_rescale, cmap=plt.cm.gray)
x2.set_title('(HOG) Histogram of Oriented Gradients for Image 12')
plt.show()

figure33, (x1, x2) = plt.subplots(1, 2)
x1.imshow(resize_image13, cmap=plt.cm.gray)
x1.set_title('Image 13')
# Rescale histogram for better display
HOG_feature_image13_rescale = exposure.rescale_intensity(HOG_image13, in_range=(0, 10))
x2.imshow(HOG_feature_image13_rescale, cmap=plt.cm.gray)
x2.set_title('(HOG) Histogram of Oriented Gradients for Image 13')
plt.show()

figure34, (x1, x2) = plt.subplots(1, 2)
x1.imshow(resize_image14, cmap=plt.cm.gray)
x1.set_title('Image 14')
# Rescale histogram for better display
HOG_feature_image14_rescale = exposure.rescale_intensity(HOG_image14, in_range=(0, 10))
x2.imshow(HOG_feature_image14_rescale, cmap=plt.cm.gray)
x2.set_title('(HOG) Histogram of Oriented Gradients for Image 14')
plt.show()

figure35, (x1, x2) = plt.subplots(1, 2)
x1.imshow(resize_image15, cmap=plt.cm.gray)
x1.set_title('Image 15')
# Rescale histogram for better display
HOG_feature_image15_rescale = exposure.rescale_intensity(HOG_image15, in_range=(0, 10))
x2.imshow(HOG_feature_image15_rescale, cmap=plt.cm.gray)
x2.set_title('(HOG) Histogram of Oriented Gradients for Image 15')
plt.show()

figure36, (x1, x2) = plt.subplots(1, 2)
x1.imshow(resize_image16, cmap=plt.cm.gray)
x1.set_title('Image 16')
# Rescale histogram for better display
HOG_feature_image16_rescale = exposure.rescale_intensity(HOG_image16, in_range=(0, 10))
x2.imshow(HOG_feature_image16_rescale, cmap=plt.cm.gray)
x2.set_title('(HOG) Histogram of Oriented Gradients for Image 16')
plt.show()

figure37, (x1, x2) = plt.subplots(1, 2)
x1.imshow(resize_image17, cmap=plt.cm.gray)
x1.set_title('Image 17')
# Rescale histogram for better display
HOG_feature_image17_rescale = exposure.rescale_intensity(HOG_image17, in_range=(0, 10))
x2.imshow(HOG_feature_image17_rescale, cmap=plt.cm.gray)
x2.set_title('(HOG) Histogram of Oriented Gradients for Image 17')
plt.show()

figure38, (x1, x2) = plt.subplots(1, 2)
x1.imshow(resize_image18, cmap=plt.cm.gray)
x1.set_title('Image 18')
# Rescale histogram for better display
HOG_feature_image18_rescale = exposure.rescale_intensity(HOG_image18, in_range=(0, 10))
x2.imshow(HOG_feature_image18_rescale, cmap=plt.cm.gray)
x2.set_title('(HOG) Histogram of Oriented Gradients for Image 18')
plt.show()

figure39, (x1, x2) = plt.subplots(1, 2)
x1.imshow(resize_image19, cmap=plt.cm.gray)
x1.set_title('Image 19')
# Rescale histogram for better display
HOG_feature_image19_rescale = exposure.rescale_intensity(HOG_image19, in_range=(0, 10))
x2.imshow(HOG_feature_image19_rescale, cmap=plt.cm.gray)
x2.set_title('(HOG) Histogram of Oriented Gradients for Image 19')
plt.show()

figure40, (x1, x2) = plt.subplots(1, 2)
x1.imshow(resize_image20, cmap=plt.cm.gray)
x1.set_title('Image 20')
# Rescale histogram for better display
HOG_feature_image20_rescale = exposure.rescale_intensity(HOG_image20, in_range=(0, 10))
x2.imshow(HOG_feature_image20_rescale, cmap=plt.cm.gray)
x2.set_title('(HOG) Histogram of Oriented Gradients for Image 20')
plt.show()


# Dataset
features = ([feature_matrix1], [feature_matrix2], [feature_matrix3], [feature_matrix4], [feature_matrix5],
            [feature_matrix6], [feature_matrix7], [feature_matrix8], [feature_matrix9], [feature_matrix10],
            [feature_matrix11], [feature_matrix12], [feature_matrix13], [feature_matrix14], [feature_matrix15],
            [feature_matrix16], [feature_matrix17], [feature_matrix18], [feature_matrix19], [feature_matrix20])
features = np.array(features)
print(features)
print("Features data shape = ", features.shape)

C1 = "Class1"; C2 = "Class1"; C3 = "Class1"; C4= "Class1"; C5 = "Class1";
C6 = "Class1"; C7 = "Class1"; C8 = "Class1"; C9 = "Class1"; C10 = "Class1";
D1 = "Class2"; D2 = "Class2"; D3 = "Class2"; D4 = "Class2"; D5 = "Class2";
D6 = "Class2"; D7 = "Class2"; D8 = "Class2"; D9 = "Class2"; D10 = "Class2";

labels = ([C1], [C2], [C3], [C4], [C5], [C6], [C7], [C8], [C9], [C10],
          [D1], [D2], [D3], [D4], [D5], [D6], [D7], [D8], [D9], [D10])
labels = np.array(labels).reshape(len(labels),1)
print("Labels data shape = ", labels.shape)

from sklearn.preprocessing import LabelEncoder
obj = LabelEncoder()
labels = obj.fit_transform(labels)

print(labels)

#  features and lable
X = features
Y = labels
from sklearn.model_selection import train_test_split
# splitting X and y into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, random_state=0)


def L2_norm(X_train,X_test):
    d = 0
    for i in range(len(X_train)):
        Eucledian_Distance = math.sqrt(d + math.pow((X_train[i] - X_test[i]),2))
    return Eucledian_Distance


def Train(X_train, y_train):
    for i in range(20):
        Training = L2_norm((X_train,y_train))
    return Training

def Test(X_test, y_test):
    for i in range(20):
        Testing = L2_norm((X_test, y_test))
    return Testing