import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess

class Ipv4Screen(ttk.Frame):
    def __init__(self, parent, controller, show_ethernet_screen, show_home_screen):
        super().__init__(parent)
        self.selection = 'ipv4'     #ipv4, sub_net, gateway
        self.show_home_screen = show_home_screen
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=4)
        self.rowconfigure(2, weight=4)
        self.rowconfigure(3, weight=4)
        self.rowconfigure(4, weight=1)
        
        status_part = Frame(self, bg='black')
        status_part.grid(row=0, column=0, columnspan=2, sticky='NEWS')
        status_part.rowconfigure(0, weight=1)
        status_part.columnconfigure(0, weight=1)
        status_part.columnconfigure(1, weight=10)
        status_part.columnconfigure(2, weight=1)

        back_button_part = tk.Frame(status_part, bg='black')
        back_button_part.grid(row=0, column=0, sticky='NEWS')
        back_button_part.place(relx=0.1, rely=0.5, anchor='c')
        back_button_part.rowconfigure(0, weight=1)
        back_button_part.columnconfigure(0, weight=1)
        back_button_part.columnconfigure(1, weight=1)

        back_button_part.bind("<Button-1>", show_ethernet_screen)
        back_button_part.rowconfigure(0,weight=1)
        back_button_part.columnconfigure(0, weight=1)
        back_button_part.columnconfigure(1, weight=1)
        
        self.get_image(back_button_part, '/home/stella/env_sensor/env_py_gui/img/parts/back_button.png', 30, 30,0, 0, 'E', command=show_ethernet_screen)
        back_label = Label(back_button_part, text='BACK', font=('Arial', 30), fg='white', bg='black', pady=3)
        back_label.grid(row=0, column=1, sticky='NW')
        def back_click(event):
            show_ethernet_screen()
        back_label.bind("<Button-1>", back_click)

################################################################################################
        ipv4_frame = Frame(self, bg='black')
        ipv4_frame.grid(row=1, column=0, sticky='NEWS')
        ipv4_frame.rowconfigure(0, weight=1)
        ipv4_frame.rowconfigure(1, weight=1)
        ipv4_frame.columnconfigure(0,weight=1)
        ipv4_label = Label(ipv4_frame, text='ipv4 address', font=('Arial', 18), fg='white', bg='black')
        ipv4_label.grid(row=0, column=0, sticky='NSW', padx=20)
        self.ipv4_entry = Entry(ipv4_frame, font=('Arial',20))
        self.ipv4_entry.grid(row=1, column=0, sticky='NESW', padx=20)
        # self.ipv4_entry.focus()
        def ipv4_clicked(event):
            self.selection = 'ipv4'
            print('ipv4 clicked')
        self.ipv4_entry.bind('<FocusIn>', ipv4_clicked)

        sub_net_frame = Frame(self, bg='black')
        sub_net_frame.grid(row=2, column=0, sticky='NEWS')
        sub_net_frame.rowconfigure(0, weight=1)
        sub_net_frame.rowconfigure(1, weight=1)
        sub_net_frame.columnconfigure(0,weight=1)
        sub_net_label = Label(sub_net_frame, text='sub_net address', font=('Arial', 18), fg='white', bg='black')
        sub_net_label.grid(row=0, column=0, sticky='NSW', padx=20)
        self.sub_net_entry = Entry(sub_net_frame, font=('Arial',20))
        self.sub_net_entry.grid(row=1, column=0, sticky='NESW', padx=20)
        def sub_net_clicked(event):
            self.selection = 'sub_net'
            print('sub_net clicked')
        self.sub_net_entry.bind('<FocusIn>', sub_net_clicked)


        gateway_frame = Frame(self, bg='black')
        gateway_frame.grid(row=3, column=0, sticky='NEWS')
        gateway_frame.rowconfigure(0, weight=1)
        gateway_frame.rowconfigure(1, weight=1)
        gateway_frame.columnconfigure(0,weight=1)
        gateway_label = Label(gateway_frame, text='gateway address', font=('Arial', 18), fg='white', bg='black')
        gateway_label.grid(row=0, column=0, sticky='NSW', padx=20)
        self.gateway_entry = Entry(gateway_frame, font=('Arial',20))
        self.gateway_entry.grid(row=1, column=0, sticky='NESW', padx=20)
        def gateway_clicked(event):
            self.selection = 'gateway'
            print('gateway clicked')
        self.gateway_entry.bind('<FocusIn>', gateway_clicked)
        

#######################################################################################
        number_pad_frame = Frame(self, bg='black')
        number_pad_frame.grid(row=1, rowspan=3, column=1, sticky='NEWS')
        number_pad_frame.columnconfigure(0, weight=1)
        number_pad_frame.columnconfigure(1, weight=1)
        number_pad_frame.columnconfigure(2, weight=1)
        number_pad_frame.rowconfigure(0, weight=1)
        number_pad_frame.rowconfigure(1, weight=1)
        number_pad_frame.rowconfigure(2, weight=1)
        number_pad_frame.rowconfigure(3, weight=1)
        label_1 = self.number_label(number_pad_frame, '1', 0, 0, lambda: self.Btn_click('1'))
        label_2 = self.number_label(number_pad_frame, '2', 0, 1, lambda: self.Btn_click('2'))
        label_3 = self.number_label(number_pad_frame, '3', 0, 2, lambda: self.Btn_click('3'))
        label_4 = self.number_label(number_pad_frame, '4', 1, 0, lambda: self.Btn_click('4'))
        label_5 = self.number_label(number_pad_frame, '5', 1, 1, lambda: self.Btn_click('5'))
        label_6 = self.number_label(number_pad_frame, '6', 1, 2, lambda: self.Btn_click('6'))
        label_7 = self.number_label(number_pad_frame, '7', 2, 0, lambda: self.Btn_click('7'))
        label_8 = self.number_label(number_pad_frame, '8', 2, 1, lambda: self.Btn_click('8'))
        label_9 = self.number_label(number_pad_frame, '9', 2, 2, lambda: self.Btn_click('9'))
        label_dot = self.number_label(number_pad_frame, '.', 3, 0, lambda: self.Btn_click('.'))
        label_0 = self.number_label(number_pad_frame, '0', 3, 1, lambda: self.Btn_click('0'))
        label_delete = self.number_label(number_pad_frame, 'Del', 3, 2, lambda: self.delete_one_word())
        
        complete_frame = Frame(self, bg='black')
        complete_frame.grid(row=4, column=0,columnspan=2, sticky='NEWS')
        complete_frame.rowconfigure(0, weight=1)
        complete_frame.rowconfigure(0, weight=10)
        complete_frame.columnconfigure(0, weight=1)
        
        self.validate_label = Label(complete_frame, text='', bg='black', fg='white', font=('Arial', 16))
        self.validate_label.grid(row=0, column=0, sticky='NWS',padx=10)
        
        complete_label = Label(complete_frame, text='Complete', font=('Arial', 20), fg='white', bg='black')
        complete_label.grid(row=1,column=0, sticky='NES', pady=5)
        def complete_click(event):
            self.check_ip_availability(self.ipv4_entry.get(), self.sub_net_entry.get(), self.gateway_entry.get())
        complete_label.bind("<Button-1>", complete_click)
        
        
        
        
        
# IPv4 주소
# 서브넷 마스크
# 기본 게이트웨이
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
    
    def number_label(self,frame, text, row, column, command):
        label = Label(frame, text=text, font=('Arial bold',15), fg='white', bg='black')
        label.grid(row=row, column=column, sticky='NEWS')
        def temp_command(event):
            command()
        label.bind('<Button-1>', temp_command)
        return label

    def Btn_click(self, character):
        print(character)
        if self.selection == 'ipv4':
            current = self.ipv4_entry.get()
            self.ipv4_entry.delete(0, END)
            self.ipv4_entry.insert(0, str(current)+character)
        elif self.selection == 'sub_net':
            current = self.sub_net_entry.get()
            self.sub_net_entry.delete(0, END)
            self.sub_net_entry.insert(0, str(current)+character)
        elif self.selection == 'gateway':
            current = self.gateway_entry.get()
            self.gateway_entry.delete(0, END)
            self.gateway_entry.insert(0, str(current)+character)
        else:
            print('ipv4 screen error')
        # current = self.pw_entry.get()
        # self.pw_entry.delete(0, END)
        # self.pw_entry.insert(0, str(current)+str(character))
    def delete_one_word(self):
        if self.selection == 'ipv4':
            current = self.ipv4_entry.get()
            self.ipv4_entry.delete(0, END)
            self.ipv4_entry.insert(0, str(current)[0:-1])
        elif self.selection == 'sub_net':
            current = self.sub_net_entry.get()
            self.sub_net_entry.delete(0, END)
            self.sub_net_entry.insert(0, str(current)[0:-1])
        elif self.selection == 'gateway':
            current = self.gateway_entry.get()
            self.gateway_entry.delete(0, END)
            self.gateway_entry.insert(0, str(current)[0:-1])
        else:
            print('ipv4 screen error')
        # current = self.pw_entry.get()
        # self.pw_entry.delete(0, END)
        # self.pw_entry.insert(0, str(current)+str(character))
    def check_ip_availability(self, ipv4_adress, sub_net_address, gateway_address):
        result = subprocess.run(['ping', '-c', '1', '-W', '1', ipv4_adress], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if result.returncode == 0:      # 이미 존재한다.
            print(f"The IP address  is already in use.")
            self.validate_label.config(text='이미 사용 중인 IP 주소입니다.', fg='red')
            pass
        else:                           # 사용되는 ip가 없다.
            if '.' in ipv4_adress and '.' in sub_net_address and '.' in gateway_address:
                try:
                    ipv4_list = ipv4_adress.split('.')
                    sub_net_list = sub_net_address.split('.')
                    gateway_list = gateway_address.split('.')
                    if self.check_each_element(ipv4_list) and self.check_each_element(sub_net_list) and self.check_each_element(gateway_list):
                        print('이떄부터 ㄱㄱㄱ')
                        self.set_ethernet_ip('eth0', self.ipv4_entry.get(), self.sub_net_entry.get(), self.gateway_entry.get())
                        self.validate_label.config(text='                           ', fg='black')
                        ####################### 설정 완료##############################
                        self.show_home_screen()
                    else:
                        self.validate_label.config(text='올바른 양식을 입력해주세요.  ', fg='red')
                except:                                                        
                    self.validate_label.config(text='올바른 양식을 입력해주세요.  ', fg='red')
                    print('err')
            # print(f"The IP address {ip_address} is available.")
            else:
                self.validate_label.config(text='올바른 양식을 입력해주세요.  ', fg='red')

    def check_each_element(self, list):
        state = True
        if len(list) == 4:
            for i in list:
                if int(i) >= 0 and int(i) < 256:
                    pass
                else:
                    state = False
            return state
        else:
            
            return False
    
    def set_ethernet_ip(self, interface, ip_v4, sub_net, gateway):
        disable_dhcp_cmd = ['sudo', 'dhclient', '-r', interface]
        subprocess.run(disable_dhcp_cmd, check=True)

        # Set the static IP address
        set_ip_cmd = ['sudo', 'ifconfig', interface, ip_v4, 'netmask', sub_net]
        subprocess.run(set_ip_cmd, check=True)

        # Set the default gateway
        set_gateway_cmd = ['sudo', 'route', 'add', 'default', 'gw', gateway]
        subprocess.run(set_gateway_cmd, check=True)