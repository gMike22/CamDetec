import urllib
import urllib.request
import cv2
import numpy as np
from tkinter import *

link="http://192.168.0.16:8080/shot.jpg"
    
class drone_camera():
    def opt1(self):
        while True:
            with urllib.request.urlopen(link) as url:
                r = url.read()
            imgNp = np.array(bytearray(r),dtype=np.uint8)
            img=cv2.imdecode(imgNp,-1)

            kernel=np.ones((5,5),np.uint8)
            rangomax=np.array([50,255,50])
            rangomin=np.array([0,51,0])
            mascara=cv2.inRange(img,rangomin,rangomax)
            opening=cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
            x,y,w,h=cv2.boundingRect(opening)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
            cv2.circle(img,(int(x+w/2),int(y+h/2)),int(5),(0,0,255),int(1))
            
            cv2.imshow('Video',img)
            if ord('q')==cv2.waitKey(10):
                exit(0)    
    def opt2(self):
        with urllib.request.urlopen(link) as url:
            r = url.read()
        imgNp = np.array(bytearray(r),dtype=np.uint8)
        img=cv2.imdecode(imgNp,-1)

        kernel=np.ones((5,5),np.uint8)
        rangomax=np.array([50,255,50])
        rangomin=np.array([0,51,0])
        mascara=cv2.inRange(img,rangomin,rangomax)
        opening=cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
        x,y,w,h=cv2.boundingRect(opening)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
        cv2.circle(img,(int(x+w/2),int(y+h/2)),int(5),(0,0,255),int(1))
        
        cv2.imshow('Video',img)
        if ord('q')==cv2.waitKey(10):
            exit(0)
d___c = drone_camera()

root = Tk()
root.geometry("300x300+0+0")
root.title("Drone")
Lbl1 = Label(root, text = "Interfaz para cámara de drone", font=('arial',13,'bold'), background="white")
Lbl1.place(relx=0.5, rely=0.2, anchor=CENTER)
btn1 = Button(root, text="Vídeo", command=d___c.opt1, background="black", font=('arial',13,'bold'),foreground="snow")
btn1.place(relx=0.2, rely=0.5, anchor=CENTER, height=50, width=100)
btn2 = Button(root, text="Foto", command=d___c.opt2, background="black", font=('arial',13,'bold'),foreground="snow")
btn2.place(relx=0.8, rely=0.5, anchor=CENTER, height=50, width=100)
root.configure(background="white")
root.mainloop()


