import pylab as plt
import matplotlib.image as immat
import numpy as np
import cv2
# 0(also can use cv2.IMREAD_GRAYSCALE) for grayscale and 1 for RGB 
def hist_im(im):
  # calculates normalized histogram of an image
	m, n = im.shape
	h = [0.0] * 256
	for i in range(m):
		for j in range(n):
			h[im[i, j]] += 1
	print np.array(h)
	return np.array(h)/(m*n)

def cummulative_sum(h):
	# finds cumulative sum of a numpy array, list
	# print h
	summation = [0] * (len(h))
	summation[0] = h[0]
	for i in range(1, len(h)):
		summation[i] = summation[i - 1] + h[i]
	return summation
	

def eq_hist(im):
	#calculate Histogram
	h = hist_im(im)
	#a = (cummulative_sum(h))
	#print a[0]
	cdf = np.array(cummulative_sum(h)) 
	lookup = np.uint8(255 * cdf)
	s1, s2 = im.shape
	Y = np.zeros_like(im)
	
	for i in range(0, s1):
		for j in range(0, s2):
			Y[i, j] = lookup[im[i, j]]
	H = hist_im(Y)
	#return transformed image, original and new istogram, 
	# and transform function
	return Y , h, H, lookup





img = cv2.imread('laptop.png',cv2.IMREAD_GRAYSCALE)

#img = cv2.resize(img, (1000, 500))

new_img, h, new_h, lookup = eq_hist(img)

equ = cv2.equalizeHist(img)

opencv_h = hist_im(equ)

cv2.imshow('image',img)

cv2.imshow('new image',new_img)

cv2.imshow('OpenCV Hist Eq', equ)

cv2.waitKey(0)

cv2.destroyAllWindows()

plt.title('Original Image')

plt.plot(h)

plt.show()

plt.title('Created Image')

plt.plot(new_h)

plt.show()

plt.title('OpenCV Image')

plt.plot(opencv_h)

plt.show()
