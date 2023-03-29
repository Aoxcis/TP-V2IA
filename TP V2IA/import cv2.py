import cv2
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
test = []
img1 = cv2.imread(r"C:\Users\grego\Downloads\V2IA\images\bankvid.bmp", cv2.IMREAD_GRAYSCALE)
print("img1 shape : ",img1.shape)

img1_equalized = cv2.equalizeHist(img1)
cv2.imshow('test_rec', img1_equalized)
cv2.waitKey()
hist_equalized = cv2.calcHist([img1_equalized],[0],None,[256],[0,256])
plt.plot(hist_equalized)

cv2.imshow('test' ,img1)
cv2.waitKey()