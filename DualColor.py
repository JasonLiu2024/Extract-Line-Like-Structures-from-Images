from PIL import Image
import scipy
import numpy as np
def rgb_to_gray(rgb):
	""" 
        rgb: array of [R, G, B]
        turn rgb array into GRAY array"""
	r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
	gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
	return gray

def two_colors(filename, threshold, other_color):
	'''
		filename: name of png image
		threshold: 
		other_color: that, instead of white (for black-white img)
		RETURN: binary version
		import and then binarize data based on threshold
		'''
	im = Image.open(filename)
	imarray = np.array(im)
	# print(f"shape of image array: {np.shape(imarray)}")
	imarray = rgb_to_gray(imarray)
	# apply gaussian filter
	imarray = scipy.ndimage.gaussian_filter(imarray, 0.55)
	# print(f"shape of image array, through gaussian filter: {np.shape(imarray)}")
	x, y = imarray.shape
	data = np.zeros((x, y))
	for i in range(x):
		for j in range(y):
			data[i][j] = 1 - imarray[i][j]
	# normalize
	data += np.abs(np.min(data))
	data = data / np.max(data)
	# turn into binary, by threshold
	binary = np.ones((x, y, 3), dtype=int)
	for i in range(x):
		for j in range(y):
			if data[i][j] > threshold:
				binary[i][j] = other_color
	return binary