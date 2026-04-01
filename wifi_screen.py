import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import network
import subprocess
import wifi_func as wf

# 현재 어떠한 와이파이가 있고 다른 와이파이들을 검색해주는 화면

# class name을 Wifi로 지으면 안된다.
class WifiScreen(ttk.Frame):
    def __init__(self, parent, controller, show_home, show_wifi_detail):
        super().__init__(parent)
        
        
        self.show_home = show_home
        self.show_wifi_detail = show_wifi_detail
        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=4)
        self.rowconfigure(1, weight=17)
        
        # 꼭 풀어줘야함 519
        self.available_wifi_list = [' ', ' ', ' ']
        # self.available_wifi_list = ['aaaa', 'bbbb']
        # if len(self.available_wifi_list) > 3:
        #     for wifi in self.available_wifi_list:
        #         self.showing_wifi_list.append(wifi)
        self.current_available_wifi_list = []           # wifi_search_new_ver -> [current_wifi, available_wifilist]
        
        self.showing_wifi_list = self.available_wifi_list[0:3]
        self.last_num = len(self.available_wifi_list) - 1
        self.current_start_num = 0
        self.current_end_num = 2
        good_img = Image.open('/home/stella/env_sensor/env_py_gui/img/wifi/strength/wifi_strength_4.png').resize((40,40), Image.ANTIALIAS)
        self.good_wifi_signal = ImageTk.PhotoImage(good_img)
        
        soso_img = Image.open('/home/stella/env_sensor/env_py_gui/img/wifi/strength/wifi_strength_3.png').resize((40,40), Image.ANTIALIAS)
        self.soso_wifi_signal = ImageTk.PhotoImage(soso_img)
        
        bad_img = Image.open('/home/stella/env_sensor/env_py_gui/img/wifi/strength/wifi_strength_2.png').resize((40,40), Image.ANTIALIAS)
        self.bad_wifi_signal = ImageTk.PhotoImage(bad_img)

        non_conncetion_img = Image.open('/home/stella/env_sensor/env_py_gui/img/wifi/strength/wifi_strength_0.png').resize((40,40), Image.ANTIALIAS)
        self.non_connection_signal = ImageTk.PhotoImage(non_conncetion_img)
        
        
        self.current_wifi_list = ['','']     # list가 여러가지 wifi가 아니고 ssid & signal strength
        
        status_part = tk.Frame(self, bg="black")
        status_part.grid(row=0, column=0, sticky="NEWS")
        
        
        status_part.rowconfigure(0, weight=1)

        status_part.columnconfigure(0, weight=1)
        status_part.columnconfigure(1, weight=10)
        # status_part.columnconfigure(2, weight=1)
        
        back_button_part = tk.Frame(status_part, bg='black')
        back_button_part.grid(row=0, column=0, sticky="NEWS", pady=(0,20),ipadx=0, ipady=0)
        back_button_part.place(relx=0.1, rely=0.5, anchor='c')          # 안맞으면...그냥 해야함... 나도 이유 모름... 그냥.... 그냥 함...  아니면 골 때려짐
        back_button_part.rowconfigure(0, weight=1)
        back_button_part.columnconfigure(0, weight=1)
        back_button_part.columnconfigure(1, weight=1)
        back_button_part.bind("<Button-1>", show_home)
        
        # self.get_button(back_button_part, show_home, '/home/stella/env_sensor/env_py_gui/img/parts/back_button.png', 25, 25,0, 0, 'NE')
        self.get_image(back_button_part, '/home/stella/env_sensor/env_py_gui/img/parts/back_button.png', 30, 30,0, 0, 'E', command=show_home)
        back_label = Label(back_button_part, text='BACK', font=('Arial', 30), fg='white', bg='black', pady=3)
        back_label.grid(row=0, column=1, sticky='NW')
        
        # 나중에 정리....
        def back_click(event):
            show_home()
        
        back_label.bind("<Button-1>", back_click)
        
        def get_wifi(event):
            self.new_ver_wifi_func()
            
        # get_wifi_label = Label(status_part, text='get wifi!', fg='white', bg='black')
        # get_wifi_label.grid(row=0, column=2)
        # get_wifi_label.bind("<Button-1>", get_wifi)
        
        
        
        ##################################################################
        # main part
        main_part = tk.Frame(self, bg='black')
        main_part.grid(row=1, column=0, sticky="NEWS")
        # main_part - column configure
        main_part.columnconfigure(0, weight=1)
        # main_part - row configure
        main_part.rowconfigure(0,weight=8)      # 2     6
        main_part.rowconfigure(1,weight=1)      # 1     3
        main_part.rowconfigure(2,weight=4)      # 1     3
        main_part.rowconfigure(3,weight=4)      # 1     3
        main_part.rowconfigure(4,weight=48)     # 12    36
        
        
        wifi_title_part = tk.Frame(main_part, bg='black')
        wifi_title_part.grid(row=0, column=0,sticky='NEWS')
        wifi_title_part.columnconfigure(0, weight=1)
        wifi_title_part.columnconfigure(1, weight=5)
        wifi_title_part.columnconfigure(2, weight=2)
        
        wifi_title_part.rowconfigure(0, weight=1)
        
        # add_wifi_title_part.place(relx=0.1, rely=0.5, anchor='c')
        
        wifi_title_label = Label(wifi_title_part, text='Wi-Fi', font=('Arial',22), fg='blue', bg='black')
        wifi_title_label.grid(row=0, column=0,sticky="W", padx=20)
        
        current_wifi_title_part = tk.Frame(main_part, bg='black')
        current_wifi_title_part.grid(row=1, column=0,sticky='NEWS')
        
        current_wifi_title_label = Label(current_wifi_title_part, text='현재 네트워크',fg='white', bg='black', font=('Arial',25), padx=30)
        current_wifi_title_label.grid(row=0, column=0)

        current_wifi_part = tk.Frame(main_part, bg='black')
        current_wifi_part.grid(row=2, column=0,sticky='NEWS', pady=(10,0))
        current_wifi_part.rowconfigure(0,weight=1)
        current_wifi_part.columnconfigure(0, weight=1)
        current_wifi_part.columnconfigure(1, weight=12)
        
        def nothing_func():
            pass
        # 이것도 빼줘야하네..
        # self.get_image(current_wifi_part, '/home/stella/env_sensor/env_py_gui/img/wifi/Wi-Fi-01.png', 40, 40, 0 ,0, 'E', command=nothing_func)
        self.current_wifi_image = self.get_image_instance(current_wifi_part, '/home/stella/env_sensor/env_py_gui/img/wifi/Wi-Fi-01.png', 40, 40, 0 ,0, 'E', command=nothing_func)
        
        self.current_wifi_label = Label(current_wifi_part, text= 'Sangsanglab 5G', font=('Arial', 18), padx=14, fg='white', bg='black')
        self.current_wifi_label.grid(row=0, column=1, sticky='W', pady=(10,0))

        available_wifi_title_part = tk.Frame(main_part, bg='black')
        available_wifi_title_part.grid(row=3, column=0,sticky='NEWS')
        available_wifi_title_part.rowconfigure(0, weight=1)
        available_wifi_title_part.columnconfigure(0, weight=10)
        available_wifi_title_part.columnconfigure(1, weight=1)

        available_wifi_title_label = Label(available_wifi_title_part, text='사용 가능한 네트워크',fg='white', bg='black', font=('Arial',25), padx=30)
        available_wifi_title_label.grid(row=0, column=0, sticky='W', pady=(20,0))
        
        # self.get_image(available_wifi_title_part, '/home/stella/env_sensor/env_py_gui/img/wifi/refresh_wifi.png', 25, 25, 0, 1, "NEWS",self.get_wifi_list)
        self.get_image(available_wifi_title_part, '/home/stella/env_sensor/env_py_gui/img/wifi/refresh_wifi.png', 25, 25, 0, 1, "NEWS",self.new_ver_wifi_func)
        
        
        # available_wifi_title_label = Label(available_wifi_title_part, text='available_wifi_title_part')
        # available_wifi_title_label.grid(row=0, column=0)

        available_wifi_part = tk.Frame(main_part, bg='black')
        available_wifi_part.grid(row=4, column=0,sticky='NEWS')
        available_wifi_part.rowconfigure(0, weight=1)
        available_wifi_part.rowconfigure(1, weight=1)
        available_wifi_part.columnconfigure(0, weight=1)
        available_wifi_part.columnconfigure(1, weight=11)
        available_wifi_part.columnconfigure(2, weight=1)
        
        
        
        up_btn_img = Image.open('/home/stella/env_sensor/env_py_gui/img/parts/btn_up.png')
        resized_up_btn_img = up_btn_img.resize((20, 20), Image.ANTIALIAS)
        photo_up_btn = ImageTk.PhotoImage(resized_up_btn_img)
        up_button = Button(available_wifi_part, command=self.press_up_button, bg='black', image = photo_up_btn)
        up_button.image = photo_up_btn
        up_button.grid(row=0, column=2,sticky='NEWS')

        down_btn_img = Image.open('/home/stella/env_sensor/env_py_gui/img/parts/btn_down.png')
        resized_down_btn_img = down_btn_img.resize((20, 20), Image.ANTIALIAS)
        photo_down_btn = ImageTk.PhotoImage(resized_down_btn_img)
        down_button = Button(available_wifi_part, command=self.press_down_button, bg='black', image = photo_down_btn)
        down_button.image = photo_down_btn
        down_button.grid(row=1, column=2, sticky='NEWS')
        
        available_wifi_list_part = tk.Frame(available_wifi_part, bg='black')
        # available_wifi_list_part.grid(row=0, column=1, rowspan=2, sticky='NEWS')
        available_wifi_list_part.grid(row=0, column=1, rowspan=2, sticky='NWS')
        available_wifi_list_part.columnconfigure(0, weight=1)
        available_wifi_list_part.columnconfigure(1, weight=15)
        available_wifi_list_part.rowconfigure(0, weight=1)
        available_wifi_list_part.rowconfigure(1, weight=1)
        available_wifi_list_part.rowconfigure(2, weight=1)
        # available_wifi_list_part.rowconfigure(3, weight=1)
        
        # first_label = Label(available_wifi_list_part, text='first!!', font=('Arial', 20))
        # second_label = Label(available_wifi_list_part, text='first!!', font=('Arial', 20))
        # third_label = Label(available_wifi_list_part, text='first!!', font=('Arial', 20))
        # first_label.grid(row=0)
        # second_label.grid(row=1)
        # third_label.grid(row=2)
        
        # def aaa(self):
        #     pass
                ############### available wifi list ###############
        
# command=lambda: self.show_wifi_detail_with_ssid(0)    
        self.first_image_label = self.get_image_instance(available_wifi_list_part, '/home/stella/env_sensor/env_py_gui/img/wifi/strength/wifi_strength_4.png', 40, 40, 0 ,0, 'E', command=lambda: self.show_wifi_detail_with_ssid(0))
        self.first_label = Label(available_wifi_list_part, text=self.showing_wifi_list[0], font=('Arial', 20), padx=14, fg='white', bg='black')
        self.first_label.grid(row=0, column=1, sticky='W')
        self.first_label.bind("<Button-1>", lambda event: self.event_func(event, num=0))
        
        self.second_image_label = self.get_image_instance(available_wifi_list_part, '/home/stella/env_sensor/env_py_gui/img/wifi/strength/wifi_strength_4.png', 40, 40, 1 ,0, 'E', command=lambda: self.show_wifi_detail_with_ssid(1))
        self.second_label = Label(available_wifi_list_part, text=self.showing_wifi_list[1], font=('Arial', 20), padx=14, fg='white', bg='black')
        self.second_label.grid(row=1, column=1, sticky='W')
        self.second_label.bind("<Button-1>", lambda event: self.event_func(event, num=1))
        
        self.third_image_label = self.get_image_instance(available_wifi_list_part, '/home/stella/env_sensor/env_py_gui/img/wifi/strength/wifi_strength_4.png', 40, 40, 2 ,0, 'E', command=lambda: self.show_wifi_detail_with_ssid(2))
        self.third_label = Label(available_wifi_list_part, text=self.showing_wifi_list[2], font=('Arial', 20), padx=14, fg='white', bg='black')
        self.third_label.grid(row=2, column=1, sticky='W')
        self.third_label.bind("<Button-1>", lambda event: self.event_func(event, num=2))
        
                
        available_wifi_label = Label(available_wifi_part, text=' ', bg='black')
        available_wifi_label.grid(row=0, column=0)

    def event_func(self,event, num):    
        self.show_wifi_detail_with_ssid(num)


    def show_wifi_detail_with_ssid(self, num):
        # print('@@@@@@@@@@@@@@@@@@@@@@@@@available wifi list@@@@@@@@@@@@@@@@@@@@@@@@@')
        # print(self.available_wifi_list)
        for wifi_info in self.available_wifi_list:
            # print(wifi_info[0], self.showing_wifi_list[num])
            if wifi_info[0] == self.showing_wifi_list[num][0]:
                # print('여기론 안들어온다고..?')
                # 같은 것을 클릭한 showing_wifi_list의 name인 wifi info
                if wifi_info[2] == '--':
                    wf.connect_non_pw_wifi(self.showing_wifi_list[num][0])
                    print('비밀번호가 없다!! ')
                    break
                else:
                    # print('else로 들어왔다.')
                    self.controller.wifi_ssid = self.showing_wifi_list[num][0]
                    print(self.controller.wifi_ssid)
                    self.show_wifi_detail()
                    break
            else:
                pass
                # print('왜 여기로 들어오는 거야..?')
        # for test
        # print(self.showing_wifi_list[num][0])



    def press_up_button(self):
        if self.current_start_num > 0:
            self.current_start_num -= 1
            self.current_end_num -= 1
            
            self.showing_wifi_list = self.available_wifi_list[self.current_start_num:self.current_end_num+1]
            # 나중에 list로 뺴서 for로 돌리자... 일단 급한대로 하드코딩
            self.first_label.config(text=self.showing_wifi_list[0][0])
            self.second_label.config(text=self.showing_wifi_list[1][0])
            self.third_label.config(text=self.showing_wifi_list[2][0])

            # 여기서의 a, b, c는 signal의 강도를 임의로 잡음 a: good, b: soso, c: bad
            if self.showing_wifi_list[0][1] == 'a':
                self.first_image_label.config(image=self.good_wifi_signal)
                self.first_image_label.image = self.good_wifi_signal
            elif self.showing_wifi_list[0][1] == 'b':
                self.first_image_label.config(image=self.soso_wifi_signal)
                self.first_image_label.image = self.soso_wifi_signal
            else:
                self.first_image_label.config(image=self.bad_wifi_signal)
                self.first_image_label.image = self.bad_wifi_signal

            if self.showing_wifi_list[1][1] == 'a':
                self.second_image_label.config(image=self.good_wifi_signal)
                self.second_image_label.image = self.good_wifi_signal
            elif self.showing_wifi_list[1][1] == 'b':
                self.second_image_label.config(image=self.soso_wifi_signal)
                self.second_image_label.image = self.soso_wifi_signal
            else:
                self.second_image_label.config(image=self.bad_wifi_signal)
                self.second_image_label.image = self.bad_wifi_signal

            if self.showing_wifi_list[2][1] == 'a':
                self.third_image_label.config(image=self.good_wifi_signal)
                self.third_image_label.image = self.good_wifi_signal
            elif self.showing_wifi_list[2][1] == 'b':
                self.third_image_label.config(image=self.soso_wifi_signal)
                self.third_image_label.image = self.soso_wifi_signal
            else:
                self.third_image_label.config(image=self.bad_wifi_signal)
                self.third_image_label.image = self.bad_wifi_signal
            
            
            
    
    def press_down_button(self):
        if self.current_end_num < len(self.available_wifi_list)-1:
            self.current_start_num += 1
            self.current_end_num += 1
            
            self.showing_wifi_list = self.available_wifi_list[self.current_start_num:self.current_end_num+1]
            self.first_label.config(text=self.showing_wifi_list[0][0])
            self.second_label.config(text=self.showing_wifi_list[1][0])
            self.third_label.config(text=self.showing_wifi_list[2][0])
            # what the... test code인데 나중에 다 고쳐줘야지
            if self.showing_wifi_list[0][1] == 'a':
                self.first_image_label.config(image=self.good_wifi_signal)
                self.first_image_label.image = self.good_wifi_signal
            elif self.showing_wifi_list[0][1] == 'b':
                self.first_image_label.config(image=self.soso_wifi_signal)
                self.first_image_label.image = self.soso_wifi_signal
            else:
                self.first_image_label.config(image=self.bad_wifi_signal)
                self.first_image_label.image = self.bad_wifi_signal

            if self.showing_wifi_list[1][1] == 'a':
                self.second_image_label.config(image=self.good_wifi_signal)
                self.second_image_label.image = self.good_wifi_signal
            elif self.showing_wifi_list[1][1] == 'b':
                self.second_image_label.config(image=self.soso_wifi_signal)
                self.second_image_label.image = self.soso_wifi_signal
            else:
                self.second_image_label.config(image=self.bad_wifi_signal)
                self.second_image_label.image = self.bad_wifi_signal

            if self.showing_wifi_list[2][1] == 'a':
                self.third_image_label.config(image=self.good_wifi_signal)
                self.third_image_label.image = self.good_wifi_signal
            elif self.showing_wifi_list[2][1] == 'b':
                self.third_image_label.config(image=self.soso_wifi_signal)
                self.third_image_label.image = self.soso_wifi_signal
            else:
                self.third_image_label.config(image=self.bad_wifi_signal)
                self.third_image_label.image = self.bad_wifi_signal
            
    # def open(self):
    #     top = Toplevel(self)
    #     top.geometry("800x480")
    #     top.attributes('-fullscreen', False)
    #     top.title('My Second Window')
    #     connecting_frame = tk.Frame(top, bg='black')
    #     connecting_frame.grid(row=0, column=0, sticky='NEWS')
    #     connecting_frame.rowconfigure(0, weight=1)
    #     connecting_frame.columnconfigure(0, weight=1)
        
    #     my_label = Label(connecting_frame, text='Second Window')
    #     my_label.grid(row=0, column=0, sticky='NEWS')
        
    # def time_update(self):
    #     time_string = strftime('%Y-%m-%d %H:%M:%S')
    #     self.time_label.config(text=time_string)
    #     self.time_label.after(1000, self.time_update)
    #     # print(uart_data_thread.TVOC)

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
        return img_label
    

    def get_button(self, frame,command, path, width, height, row, column,sticky):
        img = Image.open(path)
        resized_img = img.resize((width,height), Image.ANTIALIAS)
        photo_img = ImageTk.PhotoImage(resized_img)
        img_label = Button(frame, image=photo_img, bg='black', command=command,bd=0)        # bd = border
        img_label.image = photo_img
        img_label.grid(row=row, column=column, sticky=sticky)
        
    
    
    
    
    # 무조건 이걸로 바꿔야해 -> 비번이 없는 것을 알기 위해서 다른 방법이 없다...
    # 후........ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
    def new_ver_wifi_func(self):

        # self.current_wifi_list = wf.get_current_wifi_info() # ssid & signal strength
        # 생각해보니 wf.wifi_search_new_ver 안에서 현재 연결된 와이파이를 뺴준다.
        self.current_available_wifi_list = wf.wifi_search_new_ver()     # [current_wifi, available_wifilist]
        # print(self.current_available_wifi_list[1])  # <- available_wifilist
        self.available_wifi_list = self.current_available_wifi_list[1]
        self.available_wifi_list.sort(key= lambda x:x[1])
        # todo 나중에 3개보다 작을 때를 고려해야 한다.
        self.showing_wifi_list = self.available_wifi_list[0:3]
        # print('len : ')
        # print(len(self.available_wifi_list))
        self.last_num = len(self.available_wifi_list) - 1
        self.current_start_num = 0
        self.current_end_num = 2
        
        
        # print('first : ')
        # print(self.available_wifi_list[0][0])
        # print('second : ')
        # print(self.available_wifi_list[1][0])
        # print('third : ')
        # print(self.available_wifi_list[2][0])
        # print('what\'s error from here?')
        # print(self.available_wifi_list[0][0])
        if len(self.available_wifi_list) == 0:
            print('여기 들어옴')
            self.first_label.config(text='')
            self.second_label.config(text='')
            self.third_label.config(text='')
        else:
            self.first_label.config(text=self.available_wifi_list[0][0])
            self.second_label.config(text=self.available_wifi_list[1][0])
            self.third_label.config(text=self.available_wifi_list[2][0])
    

    
    
#     def get_wifi_list(self):
#         self.available_wifi_list = wf.wifi_Search()         # ex) available_wifi_list = [['sangsang', 'a'],['iptime', 'c']]
#         self.current_wifi_list = wf.get_current_wifi_info()
        
#         self.available_wifi_list = [i for i in self.available_wifi_list if i[0] != self.current_wifi_list[0]]           # 연결중인 와이파이는 제외시킨다.
#         # self.available_wifi_list.remove
# #####################################################################################################################
#         self.available_wifi_list.sort(key = lambda x:x[1])
#         self.showing_wifi_list = self.available_wifi_list[0:3]              # 여기서 2 ele로 바꿔주는구나...    # 근데 3개보다 많았다가 refresh했는데 그보다 작은 경우 문제가 된다.
#         self.last_num = len(self.available_wifi_list) -1
#         self.current_start_num = 0
#         self.current_end_num = 2
        
#         # 여기서 계속 에러가 떠서 실행이 안되는 때가 있는데 한번 확인해보자
#         print('available_wifi_list[0][0] : ', end=' ')
#         print(self.available_wifi_list[0][0])
#         # print('available_wifi_list[0][0] signal : ', end=' ')
#         # print(self.available_wifi_list[0][2])

#         print('available_wifi_list[1][0] : ', end=' ')
#         print(self.available_wifi_list[1][0])
#         # print('available_wifi_list[1][0] signal : ', end=' ')
#         # print(self.available_wifi_list[1][2])

#         print('available_wifi_list[2][0] : ', end=' ')
#         print(self.available_wifi_list[2][0])
#         # print('available_wifi_list[2][0] signal : ', end=' ')
#         # print(self.available_wifi_list[2][2])


#         self.first_label.config(text=self.available_wifi_list[0][0])
#         self.second_label.config(text=self.available_wifi_list[1][0])
#         self.third_label.config(text=self.available_wifi_list[2][0])
        
    
    
    
    def get_current_wifi(self):
        
        self.current_wifi_list = wf.get_current_wifi_info()
        
        
        if self.current_wifi_list == None:
            self.current_wifi_label.config(text='No Wifi...')
            self.current_wifi_image.config(image=self.non_connection_signal)
            self.current_wifi_image.image = self.non_connection_signal
        else:
            self.current_wifi_image.config(image=self.good_wifi_signal)
            self.current_wifi_image.image = self.good_wifi_signal
            self.current_wifi_label.config(text=self.current_wifi_list[0]) 
    
        # 꼭 고쳐줘야 한다.         self.current_wifi_list[1] 이 신호 세기(str값)니깐 그에 따라 고쳐줘야한다. 
        # self.current_wifi_image.config()
        # print('self.current wifi list')
        # print(self.current_wifi_list)
        
        self.current_wifi_label.after(3000, self.get_current_wifi)
        

