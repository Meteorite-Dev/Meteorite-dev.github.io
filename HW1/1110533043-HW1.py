import cv2


# import numpy as np
# import os

def show_img():
    img = cv2.imread("gl.jpg")
    img = cv2.resize(img, (300, 600))
    # grayscale 2 channel
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # to 3 channel
    gray_3 = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
    # to black and white
    (thresh, bw_img) = cv2.threshold(gray_3, 80, 255, cv2.THRESH_BINARY)
    # blurred
    blur_img = cv2.GaussianBlur(img, (99, 11), 500)
    # concatenate must correspond to height,width,dimension(channel)
    image_h = cv2.hconcat([img, gray_3, bw_img, blur_img])

    cv2.imshow('lenna!!!', image_h)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# def ShowCam(source):

if __name__ == '__main__':
    show_img()
