from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import cv2,time
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
import sqlite3
import opencv1
import face_recognition
from decimal import Decimal




class Container(Widget):
    name=ObjectProperty(None)
    add=ObjectProperty(None)
    def btn(self):
        
        id=self.video(self.name.text,self.add.text)
        print(id)
            
            
            
    def video(self,name,address):
        video_capture = cv2.VideoCapture(0)


        face_locations = []

        while True:
           
            ret, frame = video_capture.read()

           
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
        res=""
        for ind in face_encoding[0]:
            res=res+str(Decimal(ind))
            res=res+":"
        l1=res.split(":")
        print(type(l1))
        print(Decimal(l1[0]))
        video_capture.release()
        
        return 1
        
        
    
        
        
        
        
        
        
        
        
        
        
        
     
        
        
        
        
        
       
       
      
        
      
        
    

        
    

    





        
      
        
    

        
    

    




class MyApp(App):

    def build(self):
        return  Container()


if __name__ == '__main__':
    MyApp().run()
