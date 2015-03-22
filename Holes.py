import cv2
import cv2.cv
import numpy as np

pic= cv2.imread('test_picture1.jpg', 0)
blur = cv2.GaussianBlur(pic,(3,3),0)
th1 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,30)

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(th1,kernel,iterations = 1)

img = cv2.medianBlur(erosion,7)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,1,20,param1=200,param2=10,minRadius=0,maxRadius=30)

for i in circles[0,:]:
	# draw the outer circle
	cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
	# draw the center of the circle
	cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imwrite('Hole.jpg',cimg)

print("Holes are detected")
print("The Disease is Septoria Leaf Spot")
print("The solution is apply Chlorothalonil")
cv2.waitKey(0) % 0xFF
cv2.destroyAllWindows()
