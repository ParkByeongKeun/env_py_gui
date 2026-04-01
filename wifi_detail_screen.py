import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import wifi_func as wf
import subprocess
from time import sleep
# 와이파이 하나 클릭하면 비번치고...등등등 하는 화면

class WifiDetailScreen(ttk.Frame):
    def __init__(self, parent, controller, show_wifi_list_screen, show_keyboard_screen):
        super().__init__(parent)
        
        self.controller = controller
        self.show_wifi_list_screen = show_wifi_list_screen
        self.show_keyboard_screen = show_keyboard_screen
        self.pw_visible_state = False            # True - Visible

        self.rowconfigure(0,weight=1)   # status
        self.rowconfigure(1,weight=6)
        self.columnconfigure(0, weight=1)
        
        
        pw_part = Frame(self, bg='black')
        pw_part.grid(row=1, column=0, sticky='NEWS')

        pw_part.rowconfigure(0,weight=1)   # 비밀번호
        pw_part.rowconfigure(1,weight=2)   # type PW
        pw_part.rowconfigure(2,weight=2)   # auto connection
        pw_part.rowconfigure(3,weight=1)   # connect
        pw_part.columnconfigure(0, weight=1)
        
        
        status_part = tk.Frame(self, bg='black')
        status_part.grid(row=0, column=0, sticky="NEWS")
        
        status_part.rowconfigure(0, weight=1)
        status_part.columnconfigure(0, weight=1)
        status_part.columnconfigure(1, weight=10)
        status_part.columnconfigure(2, weight=1)
        
        back_button_part = tk.Frame(status_part, bg='black')
        back_button_part.grid(row=0, column=0, sticky="NEWS", pady=0,ipadx=0, ipady=0)
        back_button_part.place(relx=0.1, rely=0.5, anchor='c')          # 안맞으면...그냥 해야함... 나도 이유 모름... 그냥.... 그냥 함...  아니면 골 때려짐
        back_button_part.rowconfigure(0, weight=1)
        back_button_part.columnconfigure(0, weight=1)
        back_button_part.columnconfigure(1, weight=1)
        # back_button_part.bind("<Button-1>", show_wifi_list_screen)
        back_button_part.bind("<Button-1>", self.back_to_wifi_list_screen)
        # self.get_image(back_button_part, '/home/stella/env_sensor/env_py_gui/img/parts/back_button.png', 30, 30,0, 0, 'E', command=show_wifi_list_screen)
        self.get_image(back_button_part, '/home/stella/env_sensor/env_py_gui/img/parts/back_button.png', 30, 30,0, 0, 'E', command=self.back_to_wifi_list_screen)
        back_label = Label(back_button_part, text='BACK', font=('Arial', 30), fg='white', bg='black', pady=3)
        back_label.grid(row=0, column=1, sticky='NW')
        # 나중에 정리....

        def back_click(event):
            # show_wifi_list_screen()
            self.back_to_wifi_list_screen()
        back_label.bind("<Button-1>", back_click)
        pw_label = Label(pw_part, text='비밀번호', fg='white', bg='black', font=('Arial', 30))
        pw_label.grid(row=0, column=0, sticky="W")

        self.pw_core_frame = Frame(pw_part, bg='black')
        self.pw_core_frame.grid(row=1, column=0)
        self.pw_core_frame.rowconfigure(0, weight=1)
        self.pw_core_frame.columnconfigure(0, weight=10)
        self.pw_core_frame.columnconfigure(1, weight=1)
        

        def entry_click(event):
            show_keyboard_screen()

        self.password_entry = Entry(self.pw_core_frame, highlightthickness=2.4, bd=2.4, bg='white', fg='black', relief=FLAT, show='*', font=('Arial', 16))
        self.password_entry.grid(row=0, column=0, sticky='WNS')
        self.password_entry.config(show='*')
        self.password_entry.bind('<Button-1>', entry_click)
        show_img = Image.open('/home/stella/env_sensor/env_py_gui/img/parts/visible_on.png')
        resized_show_img = show_img.resize((45,35), Image.ANTIALIAS)
        self.show_image = ImageTk.PhotoImage(resized_show_img)
        hide_img = Image.open('/home/stella/env_sensor/env_py_gui/img/parts/visible_off.png')
        resized_hide_img = hide_img.resize((45,35), Image.ANTIALIAS)
        self.hide_image = ImageTk.PhotoImage(resized_hide_img)
        
        # self.show_image = ImageTk.PhotoImage(file='/home/stella/env_sensor/env_py_gui/img/parts/visible_on.png')
        # self.hide_image = ImageTk.PhotoImage(file='/home/stella/env_sensor/env_py_gui/img/parts/visible_off.png')
        
        self.show_button = Button(self.pw_core_frame, image=self.hide_image, highlightthickness=0,command=self.show, relief=FLAT, activebackground='black', bd=0, background='black')
        self.show_button.grid(row=0, column=1, padx=20)
        
        self.auto_connection_frame = Frame(pw_part, bg='black')
        self.auto_connection_frame.grid(row=2, column=0)
        self.auto_connection_frame.rowconfigure(0, weight=1)
        self.auto_connection_frame.columnconfigure(0, weight=6)
        self.auto_connection_frame.columnconfigure(1, weight=1)

        Label(self.auto_connection_frame, text='자동으로 연결', fg='white', bg='black',font=('Arial',30)).grid(row=0, column=0, sticky='WNS')
            
        on_img = Image.open('/home/stella/env_sensor/env_py_gui/img/parts/toggle_on.png')
        resized_on_img = on_img.resize((45,35), Image.ANTIALIAS)
        self.on = ImageTk.PhotoImage(resized_on_img)
        off_img = Image.open('/home/stella/env_sensor/env_py_gui/img/parts/toggle_off.png')
        resized_off_img = off_img.resize((45,35), Image.ANTIALIAS)
        self.off = ImageTk.PhotoImage(resized_off_img)
        
        # self.on = PhotoImage(file='/home/stella/env_sensor/env_py_gui/img/parts/toggle_on.png')
        # self.off = PhotoImage(file='/home/stella/env_sensor/env_py_gui/img/parts/toggle_off.png')
        self.auto_btn = Button(self.auto_connection_frame, image=self.on, bd=0, command=self.switch, highlightthickness=0,activebackground='black', bg='black', border=0, borderwidth=0)
        self.auto_btn.grid(row=0, column=1, padx=20)
############################################################################################################################################################################################################################################
############################################################################################################################################################################################################################################
############################################################################################################################################################################################################################################
        connect_button = Button(pw_part, text='Connect', command=self.wifi_connect, fg='white', bg='black', font=('Arial', 30))
        connect_button.grid(row=3, column=0, sticky='ES', padx=(0,10), pady=(0,10))
##################################################################################################################
    def wifi_connect(self):
        subprocess.check_output('nmcli dev wifi list', shell=True)
        cmd = 'nmcli device wifi connect {} password {}'.format(self.controller.wifi_ssid, self.password_entry.get())
        subprocess.call(cmd, shell=True)
        sleep(1)
        self.show_wifi_list_screen()
        
##################################################################################################################
    def switch(self):
        if self.pw_visible_state:
            self.auto_btn.config(image=self.off)
            self.pw_visible_state = False
        else:
            self.auto_btn.config(image=self.on)
            self.pw_visible_state = True
            
        
    def show(self):
        # print(self.pw_visible_state)
        if self.pw_visible_state:           # visible 상태일 때
            self.show_button.config(image=self.hide_image)
            self.password_entry.config(show='*')
            self.pw_visible_state = False
            
        else:
            self.show_button.config(image=self.show_image)
            self.password_entry.config(show='')
            self.pw_visible_state = True
    
        
        
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
    
    def get_image_instance(self, frame, path, width, height, row, column,sticky, command=None):
        img = Image.open(path)
        resized_img = img.resize((width,height), Image.ANTIALIAS)
        photo_img = ImageTk.PhotoImage(resized_img)
        img_label = Label(frame, image=photo_img, bg='black')
        img_label.image = photo_img
        img_label.grid(row=row, column=column, sticky=sticky)
        def local_click(event):
            command()
        img_label.bind("<Button-1>", local_click)
    
    def back_to_wifi_list_screen(self):
        self.password_entry.delete(0, END)
        self.show_wifi_list_screen()