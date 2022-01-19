import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 5)
fps = cap.get(5)
print "Frame Per Seconds : {}".format(fps)

def get_rect(cnts):

	final_cnts = []
	for c in cnts:
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.02*peri, True)
		
		if len(approx) == 4:
			final_cnts.append(c)
			
		#print len(final_cnts)
	return final_cnts

while True:
	ret, img = cap.read()
	
	if not ret:
		break
	
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gblur = cv2.GaussianBlur(gray, (3,3),0)
	canny = cv2.Canny(gblur, 75, 100)
	sobelx= cv2.Sobel(src=gblur,ddepth=cv2.CV_64F,dx=1,dy=0,ksize=5)

	_, cnts , _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		
	contours = get_rect(cnts)
	cv2.drawContours(img, contours, -1, (0,0,255), 8)
	
	cv2.imshow("Blur", gblur)
	cv2.imshow("Canny", canny)
	cv2.imshow("Sobel Axis X",sobelx)
	cv2.imshow("Contours", img)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
	
	
