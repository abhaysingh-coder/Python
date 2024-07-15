#step 1 imort
import cv2

#step 2 read the image
#convert into grayscale image
a=input("enter the image with path")
img = cv2.imread(a)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#step 3 Invert the grayscale image
inverted_img = 255 - gray_img

#step 4 convert into pencil sketch   
blurr = cv2.GaussianBlur(inverted_img, (21, 21), 0)
inverted_blurr = 255 - blurr
pencil_sketch = cv2.divide(gray_img, inverted_blurr, scale=256.0)
cv2.imshow("Orignal Image", img)
cv2.imshow("Gray Image",gray_img)
cv2.imshow("Inverted Image",inverted_img)
cv2.imshow("Blurr Image",blurr)
cv2.imshow("Inverted Blurr Image",inverted_blurr)
cv2.imshow("Pencil Sketch", pencil_sketch)
cv2.waitKey(0)
