import glob
import os
import numpy as np
from PIL import Image

images = glob.glob('./images/*.tif')

print("Found "+str(len(images))+" images to darken.")

for imageName in images:
	image = Image.open(imageName)
	print(imageName)
	data = np.asarray(image)

	image = Image.fromarray(data//4)
	name = "./darkened_images/"+imageName.split('.')[1].split("\\")[-1]+'.jpg'

	image.save(name)

print("Done.")

# image = Image.open('./r3_3001.tif')
# data = np.asarray(image)

# print(data.shape)

# maxVal = 0
# for row in data:
# 	for element in row:
# 		if element > maxVal:
# 			maxVal = element
# print(maxVal)