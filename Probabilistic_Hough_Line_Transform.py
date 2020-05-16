import cv2
import numpy as np
img = cv2.imread('data_set.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
cv2.imshow('edges', edges)
cv2.imwrite('P_edges.jpg', edges)
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
cnt=0
for line in lines:
    cnt=cnt+1
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

print(len(lines))
cv2.imshow('image', img)
cv2.imwrite('P_lines.jpg', img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
