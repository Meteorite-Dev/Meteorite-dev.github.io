import PySimpleGUI as sg
import cv2
import numpy as np
from PIL import Image, ImageTk
def main():
    sg.theme('Black')
    menu_def = [['bitplane',],]
    row1=[sg.Image( key='image1', size=(150, 150)),
         sg.Image( key='image2', size=(150, 150)),
         sg.Image( key='image3', size=(150, 150))]
    row2=[sg.Image( key='image4', size=(150, 150)),
          sg.Image( key='image5', size=(150, 150)),
          sg.Image( key='image6', size=(150, 150))]
    row3=[sg.Image( key='image7', size=(150, 150)),
          sg.Image( key='image8', size=(150, 150)),
          sg.Image( key='image9', size=(150, 150))]
    browser=[sg.In(key='img_file') ,sg.FileBrowse('browse', initial_folder="./", file_types=(("Image Files", ".jpg .png"),))]

    # define the window layout
    layout = [  [sg.Text(key='title', text='', size=(40, 1), justification='center', font='Helvetica 20')],
                row1,
                row2,
                row3,
                browser,
                [sg.Button(button_text='showimg', size=(10, 1), font='Any 14')]  
            ]
    # create the window and show it
    window = sg.Window('HW2',layout)
    # define the photo base width in order to maintain Aspect ratio
    basewidth = 150
    img_list=['image9','image8','image7','image6','image5','image4',
    'image3','image2']
    while True:
        event, values = window.read(timeout=50)

        if event == 'showimg':
            window['title'].update('bitplane')
            if len(values['img_file']) == 0:
                continue
            img = Image.open(values['img_file']).convert('LA')
            # ratio
            wpercent = (basewidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((basewidth,hsize), Image.ANTIALIAS)
            window['image1'].update(data=ImageTk.PhotoImage(img))
            # bit plane 
            for i in reversed(range(8)):
                bw_img = img.point(lambda x:255 if x>=2**i else 0)
                img = img.point(lambda x: x-2**i if x>=2**i else x)
                window[str(img_list[i])].update(data=ImageTk.PhotoImage(bw_img))

        elif event == sg.WIN_CLOSED:
            return

if __name__ == '__main__':
    main()