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

def video(uid):
    
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
    enc=face_encoding[0]
    con=sqlite3.connect("mysql.db")
    obj=con.cursor()
    obj.execute("select * from faceid")
    row=obj.fetchall()
    l1=[]
    for i in row:
        if(i[0]==uid):
            l1.append(float(i[1]))
    sc_encodings=np.array(l1)
    res=face_recognition.compare_faces([enc],sc_encodings)
    dis=face_recognition.face_distance([enc],sc_encodings)
    print(dis)
    print(type(res))
    res=res[0]
    if(res==True):
        return 1
    else:
        return 0
    
 
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
     
        
        
        
        
        
       
       
      
        
      
        
    

        
    

    





        
      
        
    

        
    

    





