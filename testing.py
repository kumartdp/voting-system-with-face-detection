from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from decimal import *
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
import sqlite3
import cv2
import time
import face_recognition
from decimal import Decimal

class KivyCamera(Image):
    def __init__(self, capture, fps, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.capture = capture
        self.count=0
        self.wait=0
        print("init")
        Clock.schedule_interval(self.update, 1.0/fps)
        
        
           
       

    def update(self, dt):
       


        face_locations = []

        while True:
           
            ret, frame =  self.capture.read()

           
            rgb_frame = frame[:, :, ::-1]

            face_locations = face_recognition.face_locations(rgb_frame)
            face_encoding = face_recognition.face_encodings(rgb_frame)
         

            for top, right, bottom, left in face_locations:
                
                img=cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)


                cv2.imshow('Video', frame)

            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            print(face_locations)
            print(face_encoding)
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
           
            self.texture = image_texture
    

    def on_stop(self,arr):
        self.capture.release()
        Clock.unschedule(self.update)
        self.validate(arr,"uid1")

class CamApp(App):
    def build(self):
        self.capture = cv2.VideoCapture(0)
        self.my_camera = KivyCamera(capture=self.capture, fps=30)
        
        return self.my_camera

    
        
        


if __name__ == '__main__':
    CamApp().run()
