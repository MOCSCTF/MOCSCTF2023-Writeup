import cv2

src = cv2.imread("miku.png")
out = cv2.medianBlur(src, 3)
cv2.imwrite("median.png",out)