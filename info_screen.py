import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import os, sys
import subprocess
from time import sleep
# import os, sys

def execute_cmd(cmd):
    os.system(cmd)

# # execute_cmd('rm terminal_cmd.py')
# import subprocess
# def firmware_update():
#     execute_cmd('rm -r /home/stella/python/core/521pyinstaller')
#     print('rm 완료')
    
#     repo_url = "https://github.com/kimvjgd/521pyinstaller.git"
#     destination_folder = '/home/stella/python/core/521pyinstaller'
    
#     try:
#         subprocess.check_output(["git", "clone", repo_url, destination_folder], cwd='/tmp')
#         print('Process well done')
#     except subprocess.CalledProcessError as e:
#         print(e)
#     # execute_cmd('cd /home/stella/python/core')
#     # print('cd 완료')
#     # execute_cmd('mkdir temp_test')
#     # print('mkdir 완료')
#     # execute_cmd('git clone "https://github.com/kimvjgd/521pyinstaller"')
#     # print('git clone 완료')

class InfoScreen(ttk.Frame):
    def __init__(self, parent, controller, show_home):
        self.mac_address = controller.mac_address                                  
        super().__init__(parent)
        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=6)
        # self.rowconfigure(1,weight=4)
        # self.rowconfigure(2,weight=5)
        # self.rowconfigure(3,weight=4)
        # self.rowconfigure(4,weight=5)
        
        
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
        back_button_part.bind("<Button-1>", show_home)
        self.get_image(back_button_part, '/home/stella/env_sensor/env_py_gui/img/parts/back_button.png', 30, 30,0, 0, 'E', command=show_home)
        back_label = Label(back_button_part, text='BACK', font=('Arial', 30), fg='white', bg='black', pady=3)
        back_label.grid(row=0, column=1, sticky='NW')
        # 나중에 정리....
        def back_click(event):
            show_home()
        back_label.bind("<Button-1>", back_click)
        

        value_part = Frame(self, bg='black')
        value_part.grid(row=1, column=0, sticky='NEWS')
        value_part.rowconfigure(0, weight=4)
        value_part.rowconfigure(1, weight=4)    
        value_part.rowconfigure(2, weight=4)
        value_part.rowconfigure(3, weight=4)
        # value_part.rowconfigure(4, weight=3)
        

        ## value_part
        device_number_label = Label(value_part, text='Device Number', font=('Arial',30), fg='white', bg='black', padx=15)
        device_number_label.grid(row=0, column=0,padx=20, sticky='WNS')
        
        device_number_value_label = Label(value_part, text=controller.device_number, font=('Arial',25), fg='white', bg='black', padx=30)
        device_number_value_label.grid(row=1, column=0, padx=50, sticky='NWS')
        
        mac_address_label = Label(value_part, text='Mac Address', font=('Arial',30), fg='white', bg='black', padx=15)
        mac_address_label.grid(row=2, column=0,padx=20, sticky='WNS')
        
        mac_address_value_label = Label(value_part, text=self.mac_address, font=('Arial',25), fg='white', bg='black', padx=30)
        mac_address_value_label.grid(row=3, column=0, padx=50, sticky='NWS')

            
        def fw_upd_click(event):
            self.firmware_update()
            
        
        # firmware_update_button = Label(value_part, text='개발용 펌웨어 업데이트',font=('Arial',25), fg='white', bg='black')
        # firmware_update_button.grid(row=4, column=0, padx=30, sticky='NEWS')
        # firmware_update_button.bind("<Button-1>", fw_upd_click)
        
    def execute_cmd(self, cmd):
        os.system(cmd)
        
    def firmware_update(self):
        print('firmware_update')
        execute_cmd('rm -r /home/stella/env_sensor/env_py_gui')
        print('rm 완료')
        repo_url = 'https://github.com/env-manager/env_py_gui.git'
        destination_folder = '/home/stella/env_sensor/env_py_gui'
        try:
            subprocess.check_output(["git", "clone", repo_url, destination_folder], cwd='/tmp')
            print('Process well done')
            sleep(5)
            execute_cmd('reboot')
        except subprocess.CalledProcessError as e:
            print(e)
        
        # os.system('rm -r 경로 적고')
        # 이후의 프로세스는
        # 밑에 코드 참조해서 할 것 (확인 다 되었다.)
# import os, sys

# def execute_cmd(cmd):
#     os.system(cmd)

# # execute_cmd('rm terminal_cmd.py')
# import subprocess
# def firmware_update():
#     execute_cmd('rm -r /home/stella/python/core/521pyinstaller')
#     print('rm 완료')
    
#     repo_url = "https://github.com/kimvjgd/521pyinstaller.git"
#     destination_folder = '/home/stella/python/core/521pyinstaller'
    
#     try:
#         subprocess.check_output(["git", "clone", repo_url, destination_folder], cwd='/tmp')
#         print('Process well done')
#     except subprocess.CalledProcessError as e:
#         print(e)
#     # execute_cmd('cd /home/stella/python/core')
#     # print('cd 완료')
#     # execute_cmd('mkdir temp_test')
#     # print('mkdir 완료')
#     # execute_cmd('git clone "https://github.com/kimvjgd/521pyinstaller"')
#     # print('git clone 완료')



        
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


        