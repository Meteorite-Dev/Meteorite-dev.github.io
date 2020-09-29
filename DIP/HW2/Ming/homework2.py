import cv2 
import numpy as np

# print(cv.__version__)


def show(sfile):
    cv2.imshow("show", sfile)
    cv2.waitKey()
    cv2.destroyAllWindows()

def show_bit_plan(bit_plan):
    num = bit_plan.shape[0]
    muti = 1
    after_bit = np.zeros([616,433] , dtype=np.int8)
    
    for i in range(0,num):
        after_bit = bit_plan[i]*muti + after_bit
        muti *=2


    # for i in after_bit : 
    #     print(i)



    # print(show_file.shape)    
    show(after_bit/255)
    
    # return after_bi
    
    # cv2.imwrite("oky-bit.png" , after_bit)




def okayu_bit():

    img = cv2.imread("okayu-color.png")
    img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

    resize_img = cv2.resize(img, (433,616), interpolation=cv2.INTER_AREA)

    # ret , bk = cv2.threshold(resize_img,190,255,cv2.THRESH_BINARY)

    image_arr = np.array(resize_img)
    show(image_arr)
    bit_plan = np.empty([1,616,433] , dtype=np.int)

    bit1 = np.array(image_arr /2 % 2 , dtype=np.int)
    # bit_plan = np.append(bit_plan, np.expand_dims(bit1 , axis=0) , axis=0)
    bit_plan = np.expand_dims(bit1, axis=0)

    bit2 = np.array(image_arr /4 %2, dtype=np.int)
    bit_plan = np.append(bit_plan, np.expand_dims(bit2 , axis=0) , axis=0)

    bit3 = np.array(image_arr /8 %2, dtype=np.int)
    bit_plan = np.append(bit_plan, np.expand_dims(bit3, axis=0) , axis=0)
    
    bit4 = np.array(image_arr /16 %2, dtype=np.int)
    bit_plan = np.append(bit_plan, np.expand_dims(bit4 , axis=0) , axis=0)
    
    bit5 = np.array(image_arr /32 %2, dtype=np.int)
    bit_plan = np.append(bit_plan, np.expand_dims(bit5 , axis=0) , axis=0)

    bit6 = np.array(image_arr /64 %2, dtype=np.int)
    bit_plan = np.append(bit_plan, np.expand_dims(bit6 , axis=0) , axis=0)

    bit7 = np.array(image_arr /128 %2, dtype=np.int)
    bit_plan = np.append(bit_plan, np.expand_dims(bit7 , axis=0) , axis=0)
    
    bit8 = np.array(image_arr /256 %2 , dtype=np.int)
    bit_plan = np.append(bit_plan, np.expand_dims(bit8 , axis=0) , axis=0)
    
    # print(bit8)
    
    after_bit = (bit8*256+bit7*128+bit6*64+bit5 *
             32+bit4*16+bit3*8+bit2*4+bit1*2)/255
    show(after_bit)

    return bit_plan    


def dona_bit():
    img = cv2.imread("love_0.jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    resize_img = cv2.resize(img, (433, 616), interpolation=cv2.INTER_AREA)

    ret, bk = cv2.threshold(resize_img, 170, 255, cv2.THRESH_BINARY)

    # print(bk)
    # bk = np.array(bk)
    bk = bk /255

    print(bk)
    # print(bk.shape)
    # show(bk)

    return bk




if __name__ =="__main__":
    oky = okayu_bit()
    d= dona_bit()
    oky[1] =  d 
    print((oky[0] == d).all())
    show_bit_plan(oky)
    
