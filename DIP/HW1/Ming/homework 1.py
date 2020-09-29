import cv2 as cv

# print(cv.__version__)

img = cv.imread("love_0.jpg")
resize_img = cv.resize(img, (433,616), interpolation=cv.INTER_AREA)
# cv.imshow("test1",resize_img)
gray_img = cv.cvtColor(resize_img , cv.COLOR_BGR2GRAY)
print(gray_img.shape)
print(img.shape)

cv.imshow("gray_img"  , gray_img )
cv.imshow("resize_img" , resize_img)

img_gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

cv.waitKey()
cv.destroyAllWindows()

cv.imwrite("love.jpg", img_gray)
