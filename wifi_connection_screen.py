import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import network
import subprocess

class WifiConnectionScreen(ttk.Frame):
    def __init__(self, parent, controller, show_wifi_list_screen, wifi_name='temp_wifi_name'):
        super().__init__(parent)
        self.controller = controller
        self.wifi_name = wifi_name
        self.rowconfigure(0,weight=3)
        self.rowconfigure(1,weight=2)
        self.rowconfigure(2,weight=4)
        self.rowconfigure(3,weight=2)
        self.rowconfigure(4,weight=4)
        self.rowconfigure(5,weight=4)
        
        status_part = tk.Frame(self, bg='blue')
        
        
        self.get_image(status_part, '/home/stella/env_sensor/env_py_gui/img/parts/back_button.png', 30, 30,0, 0, 'E', command=show_wifi_list_screen)
        back_label = Label(status_part, text='BACK', font=('Arial', 30), fg='white', bg='black', pady=3)
        back_label.grid(row=0, column=1, sticky='NW')
        
        
    def get_image(self, frame, path, width, height, row, column,sticky, command=None):
        img = Image.open(path)
        resized_img = img.resize((width,height), Image.ANTIALIAS)
        photo_img = ImageTk.PhotoImage(resized_img)
        img_label = Label(frame, image=photo_img, bg='black')
        img_label.image = photo_img
        img_label.grid(row=row, column=column, sticky=sticky)
        def local_click(event):
            command()
        img_label.bind("<Button-1>", local_click)
        
        