import tkinter as tk
from tkinter import ttk
from sensor_list import SENSOR_DICT
from tkinter import *
from PIL import Image, ImageTk

class Element(ttk.Frame):
    def __init__(self,parent, controller, show_home, sensor, sensor_range):
        super().__init__(parent)
        self.controller = controller
        self.sensor_name = sensor

        self.columnconfigure(0, weight=1)
        
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=6)
        
        status_part = tk.Frame(self, bg="black")
        status_part.grid(row=0, column=0, sticky="NEWS")
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-01.png')
        temp_gauge_01_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_01_img = ImageTk.PhotoImage(temp_gauge_01_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-02.png')
        temp_gauge_02_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_02_img = ImageTk.PhotoImage(temp_gauge_02_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-03.png')
        temp_gauge_03_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_03_img = ImageTk.PhotoImage(temp_gauge_03_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-04.png')
        temp_gauge_04_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_04_img = ImageTk.PhotoImage(temp_gauge_04_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-05.png')
        temp_gauge_05_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_05_img = ImageTk.PhotoImage(temp_gauge_05_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-06.png')
        temp_gauge_06_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_06_img = ImageTk.PhotoImage(temp_gauge_06_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-07.png')
        temp_gauge_07_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_07_img = ImageTk.PhotoImage(temp_gauge_07_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-08.png')
        temp_gauge_08_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_08_img = ImageTk.PhotoImage(temp_gauge_08_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-09.png')
        temp_gauge_09_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_09_img = ImageTk.PhotoImage(temp_gauge_09_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-10.png')
        temp_gauge_10_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_10_img = ImageTk.PhotoImage(temp_gauge_10_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-11.png')
        temp_gauge_11_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_11_img = ImageTk.PhotoImage(temp_gauge_11_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-12.png')
        temp_gauge_12_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_12_img = ImageTk.PhotoImage(temp_gauge_12_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-13.png')
        temp_gauge_13_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_13_img = ImageTk.PhotoImage(temp_gauge_13_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-14.png')
        temp_gauge_14_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_14_img = ImageTk.PhotoImage(temp_gauge_14_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-15.png')
        temp_gauge_15_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_15_img = ImageTk.PhotoImage(temp_gauge_15_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-16.png')
        temp_gauge_16_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_16_img = ImageTk.PhotoImage(temp_gauge_16_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-17.png')
        temp_gauge_17_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_17_img = ImageTk.PhotoImage(temp_gauge_17_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-18.png')
        temp_gauge_18_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_18_img = ImageTk.PhotoImage(temp_gauge_18_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-19.png')
        temp_gauge_19_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_19_img = ImageTk.PhotoImage(temp_gauge_19_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-20.png')
        temp_gauge_20_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_20_img = ImageTk.PhotoImage(temp_gauge_20_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-21.png')
        temp_gauge_21_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_21_img = ImageTk.PhotoImage(temp_gauge_21_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-22.png')
        temp_gauge_22_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_22_img = ImageTk.PhotoImage(temp_gauge_22_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-23.png')
        temp_gauge_23_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_23_img = ImageTk.PhotoImage(temp_gauge_23_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-24.png')
        temp_gauge_24_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_24_img = ImageTk.PhotoImage(temp_gauge_24_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/gauge/gage-25.png')
        temp_gauge_25_img = img.resize((700,50), Image.ANTIALIAS)
        self.gauge_25_img = ImageTk.PhotoImage(temp_gauge_25_img)
        
        
        

        
        
        status_part.rowconfigure(0, weight=1)

        status_part.columnconfigure(0, weight=3)
        status_part.columnconfigure(1, weight=20)
        status_part.columnconfigure(2, weight=2)
        
        back_button_part = tk.Frame(status_part, bg='black')
        back_button_part.grid(row=0, column=0, sticky="NEWS", pady=10,ipadx=0, ipady=0)
        back_button_part.place(relx=0.1, rely=0.5, anchor='c')          # 안맞으면...그냥 해야함... 나도 이유 모름... 그냥.... 그냥 함...  아니면 골 때려짐
        back_button_part.rowconfigure(0, weight=1)
        back_button_part.columnconfigure(0, weight=1)
        back_button_part.columnconfigure(1, weight=1)
        back_button_part.bind("<Button-1>", show_home)
        
        self.get_image(back_button_part, '/home/stella/env_sensor/env_py_gui/img/parts/back_button.png', 30, 30,0, 0, 'E', command=show_home)
        back_label = Label(back_button_part, text='MAIN', font=('Arial', 30), fg='white', bg='black', pady=3)
        back_label.grid(row=0, column=1, sticky='NW')
        
        # 나중에 정리....
        def back_click(event):
            show_home()
        
        back_label.bind("<Button-1>", back_click)
        
        ###############################################################################################################
        # main frame
        
        main_part = tk.Frame(self, bg='black')
        main_part.grid(row=1, column=0, sticky='NEWS')
        main_part.columnconfigure(0, weight=1)
        main_part.rowconfigure(0, weight=9)
        main_part.rowconfigure(1, weight=5)
        
        ######################## 1 2 1 1 1 ########################
        
        ### Sensor Description Part
        sensor_description_part = tk.Frame(main_part, bg='black')
        sensor_description_part.grid(row=0, column=0, sticky='NEWS')
        sensor_description_part.columnconfigure(0, weight=2)
        sensor_description_part.columnconfigure(1, weight=9)
        sensor_description_part.rowconfigure(0, weight=1)
        sensor_description_part.rowconfigure(1, weight=4)
        
        
        ###########################################################################
        ######################## 이미지 변경을 위해 고쳐야함 ########################
        ###########################################################################
        # print('sensor_name : ', end='')
        # print(self.sensor_name)
        image_path = '/home/stella/env_sensor/env_py_gui/img/sensor/' + self.sensor_name + '.png'
        # image_name = '/home/stella/env_sensor/env_py_gui/img/sensor/' + controller.sensor_name + '.png'
        # self.get_image(sensor_description_part, image_name, 80, 80, 0, 0, 'NEWS', rowspan=2)
        # if self.sensor_name == 'NO2':
        #     image_path = '/home/stella/env_sensor/env_py_gui/img/sensor/Main-NO2.png'
        sensor_img = Image.open(image_path)
        resized_img = sensor_img.resize((80, 80), Image.ANTIALIAS)
        sensor_image = ImageTk.PhotoImage(resized_img)
        self.img_label = Label(sensor_description_part, image=sensor_image, bg='black')
        self.img_label.image = sensor_image
        self.img_label.grid(row=0, column=0, rowspan=2, sticky='NEWS')
        

        # 1 - Sensor name
        self.title_label = Label(sensor_description_part, font=('Arial', 23),fg='white', bg='black', text='sensor_name part')
        self.title_label.grid(row=0, column=1, sticky='NWS')
        
        # 2 - Sensor description
        # description_label = tk.Text(sensor_description_part)
        # description_label.insert("sensor_name","의 기준치는","recommend_value","recommended_value_unit","이고","검출량은","sensor_value","value_unit","로","level","수준입니다.")

############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
        description_frame = tk.Frame(sensor_description_part, bg='black')
        description_frame.grid(row=1, column=1 ,sticky='NEWS')
        description_frame.columnconfigure(0, weight = 1)
        description_frame.rowconfigure(0, weight=1)
        description_frame.rowconfigure(1, weight=1)
        description_frame.rowconfigure(2, weight=1)
############################################################################################################################################################
        recommended_frame = tk.Frame(description_frame, bg='black')
        recommended_frame.grid(row=0, column=0, sticky='NEWS')
        recommended_frame.rowconfigure(0, weight=1)
        recommended_frame.columnconfigure(0, weight=1)
        recommended_frame.columnconfigure(1, weight=10)
        recommended_title_label = Label(recommended_frame, text='권고치    :', fg='white', bg='black', font=('Arial',19))
        recommended_title_label.grid(row=0, column=0, sticky='WNS')
        self.recommended_label = Label(recommended_frame, text='0000.00 ug/m3', fg='white', bg='black', font=('Arial',19))
        self.recommended_label.grid(row=0, column=1, sticky='NSW')

############################################################################################################################################################
        measurement_frame = tk.Frame(description_frame, bg='black')
        measurement_frame.grid(row=1, column=0, sticky='NEWS')
        measurement_frame.rowconfigure(0, weight=1)
        measurement_frame.columnconfigure(0, weight=1)
        measurement_frame.columnconfigure(1, weight=10)
        measurement_title_label = Label(measurement_frame, text='측정량    :', fg='white', bg='black', font=('Arial',19))
        measurement_title_label.grid(row=0, column=0, sticky='WNS')
        self.measurement_label = Label(measurement_frame, text='1111.11 ug/m3', fg='white', bg='black', font=('Arial',19))
        self.measurement_label.grid(row=0, column=1, sticky='NSW')
        
        
############################################################################################################################################################
        level_frame = tk.Frame(description_frame, bg='black')
        level_frame.grid(row=2, column=0, sticky='NEWS')
        level_frame.rowconfigure(0,weight=1)
        level_frame.columnconfigure(0, weight=1)
        level_frame.columnconfigure(1, weight=1)
        level_frame.columnconfigure(2, weight=10)

        level_reco_label = Label(level_frame, text='권고치 대비', bg='black', fg='white',font=('Arial',19))
        level_reco_label.grid(row=0, column=0,sticky='NSW')
        self.level_value_label = Label(level_frame, text='보통', bg='black', fg='white',font=('Arial',19))
        self.level_value_label.grid(row=0, column=1,sticky='NSW')
        level_extra_label = Label(level_frame, text='수준입니다.', bg='black', fg='white',font=('Arial',19))
        level_extra_label.grid(row=0, column=2,sticky='NSW')
        
    
        
        # description_label = Label(sensor_description_part, bg='black', text='description!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        # description_label.grid(row=1, column=1, sticky='NEWS')
        
        
        
        
        ### Sensor Gauge & Range Part
        sensor_value_part = tk.Frame(main_part, bg='black')
        sensor_value_part.grid(row=1, column=0, sticky='NEWS')
        sensor_value_part.columnconfigure(0,weight=1)
        sensor_value_part.rowconfigure(0,weight=3)
        sensor_value_part.rowconfigure(1,weight=1)
        # sensor_value_part.rowconfigure(2,weight=3)

        # 1 - Sensor value
        # value = Label(sensor_value_part, bg='orange', text='52g/m^3')
        # value.grid(row=0, column=0, sticky='W')

        # 1 - Sensor gauge
        # self.get_image(sensor_value_part, '/home/stella/env_sensor/env_py_gui/img/gauge/gage-12.png',700,50,row=0,column=0, sticky='EWS',pady=10)
        self.sensor_gauge = self.get_image_instance(sensor_value_part, '/home/stella/env_sensor/env_py_gui/img/gauge/gage-12.png',700,50,row=0,column=0, sticky='EWS',pady=10)
        # gauge = Label(sensor_value_part, bg='magenta')
        # gauge.grid(row=1, column=0, sticky='NEWS')
        # 1 - Sensor range
        range_frame = tk.Frame(sensor_value_part, bg='black')
        range_frame.grid(row=1, column=0, sticky='NEWS', padx=40)
        range_frame.rowconfigure(0, weight=1)
        range_frame.columnconfigure(0, weight=1)
        range_frame.columnconfigure(1, weight=1)
        range_frame.columnconfigure(2, weight=1)
        
        self.first_range_label = Label(range_frame, text='good', fg='white', bg='black',font=('Arial',10))
        self.first_range_label.grid(row=0, column=0, sticky='E')

        self.second_range_label = Label(range_frame, text='soso', fg='white', bg='black',font=('Arial',10))
        self.second_range_label.grid(row=0, column=1, sticky='E')

        self.last_range_label = Label(range_frame, text='bad', fg='white', bg='black',font=('Arial',10))
        self.last_range_label.grid(row=0, column=2, sticky='E')
        
        
        # range = Label(sensor_value_part, bg='cyan')
        # range.grid(row=1, column=0, sticky='NEWS')
        
        
        
    def get_image(self, frame, path, width, height, row, column,sticky, command=None,rowspan=1, pady=0):
        img = Image.open(path)
        resized_img = img.resize((width,height), Image.ANTIALIAS)
        photo_img = ImageTk.PhotoImage(resized_img)
        img_label = Label(frame, image=photo_img, bg='black')
        img_label.image = photo_img
        img_label.grid(row=row, column=column, rowspan=rowspan, sticky=sticky, pady=pady)
        def local_click(event):
            command()
        img_label.bind("<Button-1>", local_click)
    
    def get_image_instance(self, frame, path, width, height, row, column,sticky, command=None,rowspan=1, pady=0):
        img = Image.open(path)
        resized_img = img.resize((width,height), Image.ANTIALIAS)
        photo_img = ImageTk.PhotoImage(resized_img)
        img_label = Label(frame, image=photo_img, bg='black')
        img_label.image = photo_img
        img_label.grid(row=row, column=column, rowspan=rowspan, sticky=sticky, pady=pady)
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
        
        # SENSOR_DICT = {
        #     'TVOC':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-TVOC.png','/home/stella/env_sensor/env_py_gui/img/sensor/TVOC.png', 200, 600, 2000],  # ~200 : 좋음(1) || ~600 : 보통(2) || ~2000 : 나쁨(3) || 2000~ : 아주나쁨(4)
        #     'CO':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-CO.png','/home/stella/env_sensor/env_py_gui/img/sensor/CO.png', 2, 9, 15],
        #     'CO2':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-CO2.png','/home/stella/env_sensor/env_py_gui/img/sensor/CO2.png', 450, 1000, 2000],
        #     'NO2':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-NO2.png','/home/stella/env_sensor/env_py_gui/img/sensor/NO2.png', 0.03, 0.05, 0.2],
        #     'PM25':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-PM2.5.png','/home/stella/env_sensor/env_py_gui/img/sensor/PM2.5.png', 15, 35, 75],
        #     'H2S':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-H2S.png','/home/stella/env_sensor/env_py_gui/img/sensor/H2S.png', 0.005, 0.02, 0.3],
        #     'PM10':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-PM10.png','/home/stella/env_sensor/env_py_gui/img/sensor/PM10.png', 30, 80, 150],
        #     'LIGHT':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-LIGHT.png','/home/stella/env_sensor/env_py_gui/img/sensor/LIGHT.png', 3, 5, 10],
        #     'CH2O':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-CH2O.png','/home/stella/env_sensor/env_py_gui/img/sensor/CH2O.png', 0.001, 0.01, 0.08],
        #     'SOUND':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-SOUND.png','/home/stella/env_sensor/env_py_gui/img/sensor/SOUND.png', 35, 40, 60],
        #     'SM':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-Sm.png','/home/stella/env_sensor/env_py_gui/img/sensor/Sm.png', 0, 1, 2],  # temp
        #     'RN':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-Rn.png','/home/stella/env_sensor/env_py_gui/img/sensor/Rn.png', 50, 100, 150],  # unit 설정 필수 일단 pCi/l
        #     'NH3':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-NH3.png','/home/stella/env_sensor/env_py_gui/img/sensor/NH3.png', 0.15, 1, 5],
        #     'O3':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-O3.png','/home/stella/env_sensor/env_py_gui/img/sensor/O3.png', 0.03, 0.09, 0.15],
        # }

    def change_image(self,sensor_name):
        # self.controller
        processed_sensor_name = ''
        if sensor_name=='CO2':
            processed_sensor_name = 'CO₂'
        elif sensor_name == 'NO2':
            processed_sensor_name ='NO₂'
        elif sensor_name == 'CH2O':
            processed_sensor_name = 'CH₂O'
        elif sensor_name == 'NH3':
            processed_sensor_name = 'NH₃'
        elif sensor_name == 'H2S':
            processed_sensor_name = 'H₂S'
        elif sensor_name == 'O3':
            processed_sensor_name = 'O₃'
        else:
            processed_sensor_name = sensor_name
        self.title_label.config(text=processed_sensor_name)
        last_range = SENSOR_DICT[sensor_name][4]
        first_range = last_range/3
        first_range = "{:.2f}".format(first_range)
        second_range = 2*last_range/3
        second_range = "{:.2f}".format(second_range)
        last_range = "{:.2f}".format(last_range)
        last_range = last_range + ' [' + SENSOR_DICT[sensor_name][6] + ']'
        # reco_range = SENSOR_DICT[sensor_name][5]
        
        self.first_range_label.config(text=first_range)
        self.second_range_label.config(text=second_range)
        self.last_range_label.config(text=last_range)
        if sensor_name == 'TVOC':
            text = str(self.controller.TVOC) + ' [' + SENSOR_DICT[sensor_name][6] + ']'
            # print('################## Test 1 ##################')
            print(self.controller.TVOC)
            self.measurement_label.config(text=text)
            

            self.change_to_level(self.controller.TVOC_level)

            value = float(self.controller.TVOC)
            max = SENSOR_DICT[sensor_name][4]
            
            self.change_gauge(value, max)
            
                

        elif sensor_name == 'CO2':
            text = str(self.controller.CO2) + ' [' + SENSOR_DICT[sensor_name][6] + ']'
            self.measurement_label.config(text=text)
            self.change_to_level(self.controller.CO2_level)
            value = float(self.controller.CO2)
            max = SENSOR_DICT[sensor_name][4]
            
            self.change_gauge(value, max)

        # elif sensor_name == 'PM1':
        #     text = str(self.controller.PM1) + ' [' + SENSOR_DICT[sensor_name][6] + ']'
        #     self.measurement_label.config(text=text)
        #     self.change_to_level(self.controller.PM1_level)
        #     value = float(self.controller.PM1)
        #     max = SENSOR_DICT[sensor_name][4]
            
        #     self.change_gauge(value, max)

        elif sensor_name == 'PM25':
            text = 'PM1.0 - ' + str(int(self.controller.PM1)) + ' [' + SENSOR_DICT[sensor_name][6] + ']\n' + 'PM2.5 - '+str(int(self.controller.PM25)) + ' [' + SENSOR_DICT[sensor_name][6] + ']'
            self.measurement_label.config(text=text)
            self.change_to_level(self.controller.PM25_level)
            value = float(self.controller.PM25)
            max = SENSOR_DICT[sensor_name][4]
            
            self.change_gauge(value, max)

        elif sensor_name == 'PM10':
            text = str(int(self.controller.PM10)) + ' [' + SENSOR_DICT[sensor_name][6] + ']'
            self.measurement_label.config(text=text)
            self.change_to_level(self.controller.PM10_level)
            value = float(self.controller.PM10)
            max = SENSOR_DICT[sensor_name][4]
            
            self.change_gauge(value, max)

        elif sensor_name == 'CH2O':
            text = str(self.controller.CH2O) + ' [' + SENSOR_DICT[sensor_name][6] + ']'
            self.measurement_label.config(text=text)
            self.change_to_level(self.controller.CH2O_level)
            value = float(self.controller.CH2O)
            max = SENSOR_DICT[sensor_name][4]
            
            self.change_gauge(value, max)

        elif sensor_name == 'SM':
            text = str(self.controller.Sm) + ' [' + SENSOR_DICT[sensor_name][6] + ']'
            self.measurement_label.config(text=text)
            self.change_to_level(self.controller.Sm_level)
            value = float(self.controller.Sm)
            max = SENSOR_DICT[sensor_name][4]
            
            self.change_gauge(value, max)

        elif sensor_name == 'NH3':
            text = str(self.controller.NH3) + ' [' + SENSOR_DICT[sensor_name][6] + ']'
            self.measurement_label.config(text=text)
            self.change_to_level(self.controller.NH3_level)
            value = float(self.controller.NH3)
            max = SENSOR_DICT[sensor_name][4]
            
            self.change_gauge(value, max)

        elif sensor_name == 'CO':
            text = str(self.controller.CO) + ' [' + SENSOR_DICT[sensor_name][6] + ']'
            self.measurement_label.config(text=text)
            self.change_to_level(self.controller.CO_level)
            value = float(self.controller.CO)
            max = SENSOR_DICT[sensor_name][4]
            
            self.change_gauge(value, max)

        elif sensor_name == 'NO2':
            text = str(self.controller.NO2) + ' [' + SENSOR_DICT[sensor_name][6] + ']'
            self.measurement_label.config(text=text)
            self.change_to_level(self.controller.NO2_level)
            value = float(self.controller.NO2)
            max = SENSOR_DICT[sensor_name][4]
            
            self.change_gauge(value, max)

        elif sensor_name == 'H2S':
            text = str(self.controller.H2S) + ' [' + SENSOR_DICT[sensor_name][6] + ']'
            self.measurement_label.config(text=text)
            self.change_to_level(self.controller.H2S_level)
            value = float(self.controller.H2S)
            max = SENSOR_DICT[sensor_name][4]
            
            self.change_gauge(value, max)

        elif sensor_name == 'LIGHT':
            text = str(self.controller.LIGHT) + ' [' + SENSOR_DICT[sensor_name][6] + ']'
            self.measurement_label.config(text=text)
            self.change_to_level(self.controller.LIGHT_level)
            value = float(self.controller.LIGHT)
            max = SENSOR_DICT[sensor_name][4]
            
            self.change_gauge(value, max)

        elif sensor_name == 'SOUND':
            text = str(self.controller.SOUND) + ' [' + SENSOR_DICT[sensor_name][6] + ']'
            self.measurement_label.config(text=text)
            self.change_to_level(self.controller.SOUND_level)
            value = float(self.controller.SOUND)
            max = SENSOR_DICT[sensor_name][4]
            
            self.change_gauge(value, max)

        elif sensor_name == 'RN':
            text = str(self.controller.Rn) + ' [' + SENSOR_DICT[sensor_name][6] + ']'
            self.measurement_label.config(text=text)
            self.change_to_level(self.controller.Rn_level)
            value = float(self.controller.Rn)
            max = SENSOR_DICT[sensor_name][4]
            
            self.change_gauge(value, max)

        elif sensor_name == 'O3':
            text = str(self.controller.O3) + ' [' + SENSOR_DICT[sensor_name][6] + ']'
            self.measurement_label.config(text=text)
            self.change_to_level(self.controller.O3_level)
            value = float(self.controller.O3)
            max = SENSOR_DICT[sensor_name][4]
            
            self.change_gauge(value, max)

        else:
            print('sensorname_failed')
        
        
        
        
        recommended_text = str(SENSOR_DICT[sensor_name][5]) + ' [' + SENSOR_DICT[sensor_name][6] +']'
        self.recommended_label.config(text=recommended_text)
        
        # print(SENSOR_DICT[sensor_name][2:6])

        
        img = PhotoImage(file=SENSOR_DICT[sensor_name][1])
        self.img_label.configure(image=img)
        self.img_label.image = img
        # self.check_value(sensor_name)
        # self.after(3000, self.change_image)
        # self.after(3000, self.change_to_level)
        # self.after(3000, self.change_gauge)
    def check_value(self):
        self.change_image(self.controller.sensor_name)
        self.after(3000, self.check_value)
        
    def change_to_level(self, level):
        if level == 1:
            self.level_value_label.config(text='좋음', fg='blue')
        elif level == 2:
            self.level_value_label.config(text='보통', fg='green')
        elif level == 3:
            self.level_value_label.config(text='나쁨', fg='brown')
        elif level == 4:
            self.level_value_label.config(text='매우 나쁨', fg='red')
        else:
            pass
    
    def change_gauge(self, value, max):
        if value < 0:
            print('value minus error')
        elif value < max/12:
            self.sensor_gauge.config(image=self.gauge_01_img)
            self.sensor_gauge.image = self.gauge_01_img
        elif value < max/12*2:
            self.sensor_gauge.config(image=self.gauge_02_img)
            self.sensor_gauge.image = self.gauge_02_img
        elif value < max/12*3:
            self.sensor_gauge.config(image=self.gauge_03_img)
            self.sensor_gauge.image = self.gauge_03_img
        elif value < max/12*4:
            self.sensor_gauge.config(image=self.gauge_04_img)
            self.sensor_gauge.image = self.gauge_04_img
        elif value < max/12*5:
            self.sensor_gauge.config(image=self.gauge_05_img)
            self.sensor_gauge.image = self.gauge_05_img
        elif value < max/12*6:
            self.sensor_gauge.config(image=self.gauge_06_img)
            self.sensor_gauge.image = self.gauge_06_img
        elif value < max/12*7:
            self.sensor_gauge.config(image=self.gauge_07_img)
            self.sensor_gauge.image = self.gauge_07_img
        elif value < max/12*8:
            self.sensor_gauge.config(image=self.gauge_08_img)
            self.sensor_gauge.image = self.gauge_08_img
        elif value < max/12*9:
            self.sensor_gauge.config(image=self.gauge_09_img)
            self.sensor_gauge.image = self.gauge_09_img
        elif value < max/12*10:
            self.sensor_gauge.config(image=self.gauge_10_img)
            self.sensor_gauge.image = self.gauge_10_img
        elif value < max/12*11:
            self.sensor_gauge.config(image=self.gauge_11_img)
            self.sensor_gauge.image = self.gauge_11_img
        elif value < max/12*12:
            self.sensor_gauge.config(image=self.gauge_12_img)
            self.sensor_gauge.image = self.gauge_12_img
        elif value < max/12*13:
            self.sensor_gauge.config(image=self.gauge_13_img)
            self.sensor_gauge.image = self.gauge_13_img
        elif value < max/12*14:
            self.sensor_gauge.config(image=self.gauge_14_img)
            self.sensor_gauge.image = self.gauge_14_img
        elif value < max/12*15:
            self.sensor_gauge.config(image=self.gauge_15_img)
            self.sensor_gauge.image = self.gauge_15_img
        elif value < max/12*16:
            self.sensor_gauge.config(image=self.gauge_16_img)
            self.sensor_gauge.image = self.gauge_16_img
        elif value < max/12*17:
            self.sensor_gauge.config(image=self.gauge_17_img)
            self.sensor_gauge.image = self.gauge_17_img
        elif value < max/12*18:
            self.sensor_gauge.config(image=self.gauge_18_img)
            self.sensor_gauge.image = self.gauge_18_img
        elif value < max/12*19:
            self.sensor_gauge.config(image=self.gauge_19_img)
            self.sensor_gauge.image = self.gauge_19_img
        elif value < max/12*20:
            self.sensor_gauge.config(image=self.gauge_20_img)
            self.sensor_gauge.image = self.gauge_20_img
        elif value < max/12*21:
            self.sensor_gauge.config(image=self.gauge_21_img)
            self.sensor_gauge.image = self.gauge_21_img
        elif value < max/12*22:
            self.sensor_gauge.config(image=self.gauge_22_img)
            self.sensor_gauge.image = self.gauge_22_img
        elif value < max/12*23:
            self.sensor_gauge.config(image=self.gauge_23_img)
            self.sensor_gauge.image = self.gauge_23_img
        elif value < max/12*24:
            self.sensor_gauge.config(image=self.gauge_24_img)
            self.sensor_gauge.image = self.gauge_24_img
        elif value > max:
            self.sensor_gauge.config(image=self.gauge_25_img)
            self.sensor_gauge.image = self.gauge_25_img
        else:
            print('something error in element_value')
        