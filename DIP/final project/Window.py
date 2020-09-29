import tkinter as tk
from PIL import ImageTk , Image 
import os

def window_origin():

    window = tk.Tk()
    window.geometry("800x600")
    window.resizable(True , True)
    window.title("DIP")
    # window.iconbitmap("okayu.png")

    canvas = tk.Canvas(window, bg='white', height=768, width=1024)
    image1 =tk.PhotoImage(file="fubuki.gif")
    image2 =tk.PhotoImage(file="okayu.png")
    

    #定义图片1的位置
    i1 = canvas.create_image(260, 100, anchor='nw', image=image1)
    #定义图片2的位置
    i5 = canvas.create_image(415, 258, anchor='nw', image=image2)
    canvas.pack()

    window.mainloop()
    

if __name__ == "__main__":
    window_origin()
