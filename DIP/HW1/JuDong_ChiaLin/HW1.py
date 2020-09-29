import PySimpleGUI as sg
import cv2
import numpy as np
from PIL import Image, ImageTk

def main():
    sg.theme('Black')
    menu_def = [['Source', ['file', 'Webcam',]],]
    # define the window layout
    layout = [  [sg.Text(key='title', text='Welcome user', size=(40, 1), justification='center', font='Helvetica 20')],
                [sg.Menu(menu_def)],
                [sg.Image( key='image1', size=(400, 300)),
                sg.Image( key='image2', size=(400, 300)),
                sg.Image( key='image3', size=(400, 300))],
                [sg.In(key='img_file') ,sg.FileBrowse('browse', initial_folder="./", file_types=(("Image Files", "*.*"),))],
                [sg.Button('Webcam', size=(10, 1), font='Any 14'),
                sg.Button('showfile', size=(10, 1), font='Any 14'),
                sg.Button('Exit', size=(10, 1), font='Any 14')]  ]
    # create the window and show it
    window = sg.Window('Homework1',layout)
    # ---===--- Event LOOP Read and display frames, operate the GUI --- #
    cap = cv2.VideoCapture(0)
    recording = False
    # define the photo base width in order to maintain Aspect ratio
    basewidth = 300

    while True:
        event, values = window.read(timeout=50)

        if event == 'showfile':
            window['title'].update('ImageFile')
            recording = False
            if len(values['img_file']) == 0:
                continue
            img = Image.open(values['img_file'])
            # ratio
            wpercent = (basewidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((basewidth,hsize), Image.ANTIALIAS)
            gray_img = img.convert('LA')
            bw_img = gray_img.point(lambda x: 0 if x<100 else 255)
            window['image1'].update(data=ImageTk.PhotoImage(img))
            window['image2'].update(data=ImageTk.PhotoImage(gray_img))
            window['image3'].update(data=ImageTk.PhotoImage(bw_img))
            

        elif event == 'Webcam':
            recording = True
            window['title'].update('')

        elif event == 'Exit' or event == sg.WIN_CLOSED:
            window.close()
            return

        if recording:
            ret, frame = cap.read() # original webcam
            org_resize = cv2.resize(frame,(400,300))
            gray_resize = cv2.cvtColor(org_resize, cv2.COLOR_BGR2GRAY) # to grayscale
            (thresh, blackAndWhiteImage) = cv2.threshold(gray_resize, 150, 255, cv2.THRESH_BINARY)
            org_img = cv2.imencode('.png', org_resize)[1].tobytes()  
            gray_img = cv2.imencode('.png', gray_resize)[1].tobytes()  
            bw_img = cv2.imencode('.png', blackAndWhiteImage )[1].tobytes()  
            window['image1'].update(data=org_img)
            window['image2'].update(data=gray_img)
            window['image3'].update(data=bw_img)

if __name__ == '__main__':
    main()