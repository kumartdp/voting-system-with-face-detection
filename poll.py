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
import database
import mock
import facematch
import duplicate
import notmatch

flag1=0
class Container1(Widget):

    uid=ObjectProperty(None)
    
    def btn1(self):
        uid1=self.uid.text
        flag=database.check(uid1)
        if(not flag):
            flag1=1
            print("valid")
            App.get_running_app().stop()
            if(facematch.video(uid1)):
                mock.check(1)
            else:
                notmatch.check(1)
                
                
            
            
            
            
        else:
            duplicate.check(1)
            
            
            
        return
        
        

    

    

class MyApp(App):

    def build(self):
        return  Container1()
    
  


if __name__ == '__main__':
    MyApp().run()
    
