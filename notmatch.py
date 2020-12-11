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







class Container4(Widget):
    print("okkk")
    
        
        


class MyApp(App):

    def build(self):
        return  Container4()


def check(a):
    if(a==1):
        
        
        MyApp().run()
