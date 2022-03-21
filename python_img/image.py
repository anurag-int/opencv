import cv2
import imutils
img = cv2.imread("13fb012e-7aff-e911-80cd-fa7ca2e6058b-original.jpg")
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("grayImg.jpg",grayImg)
resize = imutils.resize(img, width = 500, height=1000)
cv2.imshow("resize",resize)
cv2.imshow("grayImg.jpg",grayImg)
cv2.imshow("13fb012e-7aff-e911-80cd-fa7ca2e6058b-original.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#write a program read image and resize it and also change it in grey color
