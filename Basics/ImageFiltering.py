import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('ckt.png')
blur1 = cv2.blur(img,(5,5))
blur2 = cv2.medianBlur(img, 5)
res = np.hstack((img,blur1,blur2))
cv2.imshow('Compare', res)

plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(blur1),plt.title('Mean')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(blur2),plt.title('Median')
plt.xticks([]), plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
