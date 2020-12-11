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

import face_recognition
from decimal import Decimal
import database
import sqlite3



class Container(Widget):
    name=ObjectProperty(None)
    add=ObjectProperty(None)
    def btn(self):
        
        id=self.video(self.name.text,self.add.text)
        print(id)
            
            
            
    def video(self,name,address):
        video_capture = cv2.VideoCapture(0)


        face_locations = []
        flag=0

        while True:
           
            ret, frame = video_capture.read()

           
            rgb_frame = frame[:, :, ::-1]

            face_locations = face_recognition.face_locations(rgb_frame)
            face_encoding = face_recognition.face_encodings(rgb_frame)
         

            for top, right, bottom, left in face_locations:
                
                img=cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)


            cv2.imshow('Video', frame)

            
            if cv2.waitKey(33)==ord('a'):
                cv2.destroyAllWindows()
                video_capture.release();
    
                flag=1
                break
            if(flag):
                break
                

        print(face_locations)
        print(face_encoding)
        enc=face_encoding[0]
        con=sqlite3.connect("mysql.db")
        obj=con.cursor()
        obj.execute("select * from facepoll")
        row=obj.fetchall()
        count=len(row)
        count+=1
        uid=str(count)
        uid="uid"+uid
        t=(uid,name,address,"no")
        t1=(uid,enc)
        database.insert(t)
        database.insert1(t1)
        return uid
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
     
        
        
        
        
        
       
       
      
        
      
        
    

        
    

    





        
      
        
    

        
    

    




class MyApp(App):

    def build(self):
        return  Container()


if __name__ == '__main__':
    MyApp().run()
