import cv2 as cv
import numpy as np


vid=cv.VideoCapture(0)
vid.set(cv.CAP_PROP_FPS, 5)
fps = vid.get(5)

print "Frame Per Seconds : {}".format(fps)
while True:
    	ret , vidImage= vid.read()

    	if not ret:
		break
	kernel = np.ones((5,5), np.uint8)  
    	gray=cv.cvtColor(vidImage, cv.COLOR_BGR2GRAY)
	ret, thresh = cv.threshold(gray, 0, 128, cv.THRESH_TOZERO)	
    	gblur=cv.GaussianBlur(thresh, (3,3), 0)
	erosion = cv.erode(gblur,kernel,iterations=1)
	edges = cv.Canny(image=erosion, threshold1=50, threshold2=200)
	sobelxy = cv.Sobel(src=edges, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)
	
	#gabung= cv.Canny(image=sobelxy, threshold1=100, threshold2=200)
	#cv.imshow('Binary Image',thresh)    	
	cv.imshow('Sobel',sobelxy)
	cv.imshow('Canny', edges)
	#cv.imshow('Gabung', gabung)
	cv.imshow('Erosion',erosion)
	
    	if cv.waitKey(1) & 0xFF == ord('q'):
      		break

vid.release()
cv.destroyAllWindows()

