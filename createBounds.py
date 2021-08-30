import glob
import os
import numpy as np
from PIL import Image
import random

boxSize = [11, 11, 12]

images = glob.glob('./darkened_images/*.jpg')

print('Number of images detected: '+str(len(images)))

if len(glob.glob('labels/')) == 0:
	os.mkdir('labels/')

for imageName in images:

	temp = imageName.split('/')[-1]
	temp = temp.split('\\')[-1].split('.')[-2]
	
	labelName = './labels/' + temp + '.txt'
	print(labelName)
	output = open(labelName, "w")

	image = Image.open(imageName)
	data = np.asarray(image)

	shape = data.shape

	tVal = 2*255

	for i in range(shape[0]):

		for j in range(shape[1]):

			element = np.sum(data[i][j])

			if element >= tVal:

				v1 = str(j/shape[1])
				v2 = str(i/shape[0])

				size = random.choice(boxSize)

				toWrite = '0 ' + v1 + ' ' + v2 + ' ' + str(size/shape[1]) + ' ' + str(size/shape[0]) + '\n'
				output.write(toWrite)

	name = imageName.split('.')[1]+'.jpg'

	image.save('.'+name)
	output.close()