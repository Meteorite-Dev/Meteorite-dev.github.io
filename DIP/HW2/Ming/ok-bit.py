import cv2
import numpy as np

# print(cv.__version__)

img = cv2.imread("okayu-color.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

resize_img = cv2.resize(img, (433, 616), interpolation=cv2.INTER_AREA)

ret, bk = cv2.threshold(resize_img, 190, 255, cv2.THRESH_BINARY)

image_arr = np.array(bk)
print(image_arr.shape)

# cv2.imshow("bit-plan-before", bk)

bit1 = np.array(image_arr % 2, dtype=np.int16)
bit2 = np.array(image_arr % 4, dtype=np.int16)
bit3 = np.array(image_arr % 8, dtype=np.int16)
bit4 = np.array(image_arr % 16, dtype=np.int16)
bit5 = np.array(image_arr % 32, dtype=np.int16)
bit6 = np.array(image_arr % 64, dtype=np.int16)
bit7 = np.array(image_arr % 128, dtype=np.int16)
bit8 = np.array(image_arr % 255, dtype=np.int16)

after_bit = (bit8*256+bit7*128+bit6*64+bit5 *
             32+bit4*16+bit3*8+bit2*4+bit1*2)/255
# print(bk[10][10])
# print(after_bit[10][10])
for i in bit1:
    print(i)

# cv2.imshow("bit-plan", bit1)

# print(bit1)
# cv2.imshow("black" , bk)

cv2.waitKey()
cv2.destroyAllWindows()

# cv2.imwrite("lokayu-b.jpg", bk)
