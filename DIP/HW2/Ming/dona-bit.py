import cv2
import numpy as np

# print(cv.__version__)

img = cv2.imread("love_0.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

resize_img = cv2.resize(img, (433, 616), interpolation=cv2.INTER_AREA)

ret, bk = cv2.threshold(resize_img, 190, 255, cv2.THRESH_BINARY)
bk = np.array(bk)
bk = bk / 255

print(bk)

# cv2.imshow("d-b" , bk)


cv2.waitKey()
cv2.destroyAllWindows()

# cv2.imwrite("lokayu-b.jpg", bk)
