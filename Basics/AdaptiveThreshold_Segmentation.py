import cv2
import numpy as np
from matplotlib import pyplot as plt
#from HistEq import cummulative_sum, hist_im, eq_hist

def find_mean(img, t0):
	m, n = img.shape
	m1 = []
	m2 = []
	c1 = 0
	c2 = 0
	for i in range(0, m):
		for j in range(0, n):
			if img[i, j] <= t0 :
				#m1[c1] = img[i, j]
				m1.append(img[i, j])
				
			else:
				#m2[c2] = img[i, j]
				m2.append(img[i, j])
				c2 = c2 + 1


	mean1 = sum(m1) / len(m1)
	mean2 = sum(m2) / len(m2)


	ti = (mean1 + mean2) / 2

	return ti


img = cv2.imread('5.jpg', cv2.IMREAD_GRAYSCALE)
original = cv2.imread('5.jpg', cv2.IMREAD_GRAYSCALE)
m , n = img.shape
initial_threshold = 0
summation = 0
for i in range(0, m):
	for j in range(0, n):
		summation = summation + img[i,j]

initial_threshold = summation / (m*n)

t0 = initial_threshold


ti = find_mean(img, t0)
print t0
print ti
print '******'
while ti - t0 >= 2 :
	t0 = ti
	ti = find_mean(img, t0)

print ti
tf = ti

for i in range(0, m):
		for j in range(0, n):
			if img[i, j] >= tf:
				img[i, j] = 255

res = np.hstack((original, img))
cv2.imshow('image',res)
cv2.waitKey(0)
cv2.destroyAllWindows()



