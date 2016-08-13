import cv2


img = cv2.imread('motivational.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.imwrite('mot.png',img)
print img
cv2.waitKey(0)
cv2.destroyAllWindows()
