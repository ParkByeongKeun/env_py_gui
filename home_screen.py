import tkinter as tk
from tkinter import ttk
from tkinter import *
from datetime import datetime
from time import strftime
from PIL import Image, ImageTk
import sys
from wifi_func import get_current_connection_state, notify_esp32_if_wifi_connected
import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion
import os
import json
import math
from sensor_list import SENSOR_DICT
from device_list import device_info
from VERSION_INFO import CURRENT_VERSION
from element_screen import Element
from time import sleep
import random
# import mysql.connector
import threading

THINGSBOARD_HOST = "210.117.143.37"

# 오프라인 텔레메트리 큐 상한 (JSON UTF-8 바이트 합계 기준)
_TELEMETRY_QUEUE_MAX_BYTES = 500 * 1024 * 1024

# # DB
# my_db = mysql.connector.connect(
#     host= THINGSBOARD_HOST,          # MySQL 서버 주소
#     user= "yot132",      # MySQL 사용자 이름
#     passwd= "tmxjavm67",  # MㅈySQL 비밀번호
#     database= "airstella"   # MySQL 데이터베이스 이름
# )

#mqtt
port = 10061

# temp
sensor_data = {
        "values":{
                "S_0_0":0,
                "S_0_1":0,
                "S_0_2":0,
                "S_0_3":0,
                "S_0_4":0,
                "S_0_5":0,
                "S_0_6":0,
                "S_0_7":0,
                "S_0_8":0,
                "S_0_9":0,
                "S_0_10":0,
                "S_0_11":0,
                "S_0_12":0,
                "S_0_13":0,
                }}

class Home(ttk.Frame):
    def __init__(self, parent, controller, show_element, show_wifi, show_info, show_ethernet):
        super().__init__(parent)
        self.my_db = None
        self.db_connected = False
        # self.start_db_thread()
        self.controller = controller
        self.show_wifi = show_wifi
        self.show_ethernet = show_ethernet
        self.info_device = device_info[self.controller.device_number-1]
        self.thingsboard_connection_state = False
        self.pre_term = self.controller.send_term
        self.Board_Serial_Num = ''
        self.ROU = 0.0
        self.TVOC = 0.0
        # self.TVOC = tk.StringVar(value=123)
        self.CO2 = 0.0
        self.PM1 = 0.0
        self.PM25 = 0.0
        self.PM10 = 0.0
        self.CH2O = 0.0
        self.Sm = 0.0
        self.NH3 = 0.0
        self.CO = 0.0
        self.NO2 = 0.0
        self.H2S = 0.0
        self.LIGHT = 0.0
        self.SOUND = 0.0
        self.Rn = 0.0
        self.O3 = 0.0
        self.temperature = 0.0
        self.humidity = 0.0


        self.avg_count_TVOC = 0
        self.avg_count_CO2 = 0
        self.avg_count_PM1 = 0
        self.avg_count_PM25 = 0
        self.avg_count_PM10 = 0
        self.avg_count_CH2O = 0
        self.avg_count_Sm = 0
        self.avg_count_NH3 = 0
        self.avg_count_CO = 0
        self.avg_count_NO2 = 0
        self.avg_count_H2S = 0
        self.avg_count_LIGHT = 0
        self.avg_count_SOUND = 0
        self.avg_count_Rn = 0
        self.avg_count_O3 = 0
        self.avg_count_temperature = 0
        self.avg_count_humidity = 0
        self.avg_TVOC = 0.0
        self.avg_CO2 = 0.0
        self.avg_PM1 = 0.0
        self.avg_PM25 = 0.0
        self.avg_PM10 = 0.0
        self.avg_CH2O = 0.0
        self.avg_Sm = 0.0
        self.avg_NH3 = 0.0
        self.avg_CO = 0.0
        self.avg_NO2 = 0.0
        self.avg_H2S = 0.0
        self.avg_LIGHT = 0.0
        self.avg_SOUND = 0.0
        self.avg_Rn = 0.0
        self.avg_O3 = 0.0
        self.avg_temperature = 0.0
        self.avg_humidity = 0.0

        self.prev_TVOC = 0.0
        self.prev_CO2 = 0.0
        self.prev_PM1 = 0.0
        self.prev_PM25 = 0.0
        self.prev_PM10 = 0.0
        self.prev_CH2O = 0.0
        self.prev_Sm = 0.0
        self.prev_NH3 = 0.0
        self.prev_CO = 0.0
        self.prev_NO2 = 0.0
        self.prev_H2S = 0.0
        self.prev_LIGHT = 0.0
        self.prev_SOUND = 0.0
        self.prev_Rn = 0.0
        self.prev_O3 = 0.0
        self.prev_temperature = 0.0
        self.prev_humidity = 0.0


        self.first_sent = False
        self.sample_count = 0

        self.lan_state = 'wlan'     
        self.pre_lan_state = 'wlan' 
        self.client = mqtt.Client(callback_api_version=CallbackAPIVersion.VERSION2)
        self.client.username_pw_set(self.info_device[3])
        self.previous_sensor_data = None  
        self.network_connected = False
        self.data_queue = []  # (sensor_data, wire_json_utf8_bytes)
        self._data_queue_bytes = 0
        self._data_queue_lock = threading.RLock()
        self.start_network_check_thread()
        self.pre_temperature_level = 0
        self.pre_humidity_level = 0
        self.temperature_level = 0
        self.humidity_level = 0
        
        
        # self.start_send_thread()
        self.schedule_mqtt_data()


        # self.time_update()
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=5)
        
        
        # status (upper)
        status_part = tk.Frame(self, bg="black")
        status_part.grid(row=0, column=0, sticky="NEWS")
        status_part.columnconfigure(0, weight=10)
        status_part.columnconfigure(1, weight=1)
        status_part.columnconfigure(2, weight=1)
        # status_part.columnconfigure(3, weight=1)
        # status_part.columnconfigure(4, weight=1)                        # For MQTT send - gonna be erased soon
        status_part.rowconfigure(0, weight=1)
        
        
        # temperature & humidity (middle)
        temp_hum_part = tk.Frame(self, bg="black")
        temp_hum_part.grid(row=1, column=0, sticky="NEWS")
        temp_hum_part.rowconfigure(0, weight=1)
        temp_hum_part.columnconfigure(0, weight=2)
        temp_hum_part.columnconfigure(1, weight=3)
        temp_hum_part.columnconfigure(2, weight=8)
        temp_hum_part.columnconfigure(3, weight=2)
        temp_hum_part.columnconfigure(4, weight=3)
        temp_hum_part.columnconfigure(5, weight=8)
        
        # sensor values (lower)
        sensor_part = tk.Frame(self, bg="black")
        sensor_part.grid(row=2, column=0, sticky="NEWS")
        # row configure
        sensor_part.rowconfigure(0, weight=10)      # first row
        sensor_part.rowconfigure(1, weight=1)       # separator
        sensor_part.rowconfigure(2, weight=10)      # second row
        # column configure
        sensor_part.columnconfigure(0,weight=9)     # tvoc  &   co
        sensor_part.columnconfigure(1,weight=1)
        sensor_part.columnconfigure(2,weight=9)     # co2   &   no2
        sensor_part.columnconfigure(3,weight=1)
        sensor_part.columnconfigure(4,weight=9)     # pm2.5 &   h2s
        sensor_part.columnconfigure(5,weight=1)
        sensor_part.columnconfigure(6,weight=9)     # pm10  &   light
        sensor_part.columnconfigure(7,weight=1)
        sensor_part.columnconfigure(8,weight=9)     # ch2o  &   sound
        sensor_part.columnconfigure(9,weight=1)
        sensor_part.columnconfigure(10,weight=9)    # sm    &   rn
        sensor_part.columnconfigure(11,weight=1)
        sensor_part.columnconfigure(12,weight=9)    # nh3   &   o3
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/humidity/humidity0.png')
        temp_hum_0_img = img.resize((240, 35), Image.ANTIALIAS)
        self.hum_0_img = ImageTk.PhotoImage(temp_hum_0_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/humidity/humidity1.png')
        temp_hum_1_img = img.resize((240, 35), Image.ANTIALIAS)
        self.hum_1_img = ImageTk.PhotoImage(temp_hum_1_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/humidity/humidity2.png')
        temp_hum_2_img = img.resize((240, 35), Image.ANTIALIAS)
        self.hum_2_img = ImageTk.PhotoImage(temp_hum_2_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/humidity/humidity3.png')
        temp_hum_3_img = img.resize((240, 35), Image.ANTIALIAS)
        self.hum_3_img = ImageTk.PhotoImage(temp_hum_3_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/humidity/humidity4.png')
        temp_hum_4_img = img.resize((240, 35), Image.ANTIALIAS)
        self.hum_4_img = ImageTk.PhotoImage(temp_hum_4_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/humidity/humidity5.png')
        temp_hum_5_img = img.resize((240, 35), Image.ANTIALIAS)
        self.hum_5_img = ImageTk.PhotoImage(temp_hum_5_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/humidity/humidity6.png')
        temp_hum_6_img = img.resize((240, 35), Image.ANTIALIAS)
        self.hum_6_img = ImageTk.PhotoImage(temp_hum_6_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/humidity/humidity7.png')
        temp_hum_7_img = img.resize((240, 35), Image.ANTIALIAS)
        self.hum_7_img = ImageTk.PhotoImage(temp_hum_7_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/humidity/humidity8.png')
        temp_hum_8_img = img.resize((240, 35), Image.ANTIALIAS)
        self.hum_8_img = ImageTk.PhotoImage(temp_hum_8_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/humidity/humidity9.png')
        temp_hum_9_img = img.resize((240, 35), Image.ANTIALIAS)
        self.hum_9_img = ImageTk.PhotoImage(temp_hum_9_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/humidity/humidity10.png')
        temp_hum_10_img = img.resize((240, 35), Image.ANTIALIAS)
        self.hum_10_img = ImageTk.PhotoImage(temp_hum_10_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/humidity/humidity11.png')
        temp_hum_11_img = img.resize((240, 35), Image.ANTIALIAS)
        self.hum_11_img = ImageTk.PhotoImage(temp_hum_11_img)
        
##################################################################################################
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/temperature/temp0.png')
        temp_temperature_0_img = img.resize((240, 35), Image.ANTIALIAS)
        self.temp_0_img = ImageTk.PhotoImage(temp_temperature_0_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/temperature/temp1.png')
        temp_temperature_1_img = img.resize((240, 35), Image.ANTIALIAS)
        self.temp_1_img = ImageTk.PhotoImage(temp_temperature_1_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/temperature/temp2.png')
        temp_temperature_2_img = img.resize((240, 35), Image.ANTIALIAS)
        self.temp_2_img = ImageTk.PhotoImage(temp_temperature_2_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/temperature/temp3.png')
        temp_temperature_3_img = img.resize((240, 35), Image.ANTIALIAS)
        self.temp_3_img = ImageTk.PhotoImage(temp_temperature_3_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/temperature/temp4.png')
        temp_temperature_4_img = img.resize((240, 35), Image.ANTIALIAS)
        self.temp_4_img = ImageTk.PhotoImage(temp_temperature_4_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/temperature/temp5.png')
        temp_temperature_5_img = img.resize((240, 35), Image.ANTIALIAS)
        self.temp_5_img = ImageTk.PhotoImage(temp_temperature_5_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/temperature/temp6.png')
        temp_temperature_6_img = img.resize((240, 35), Image.ANTIALIAS)
        self.temp_6_img = ImageTk.PhotoImage(temp_temperature_6_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/temperature/temp7.png')
        temp_temperature_7_img = img.resize((240, 35), Image.ANTIALIAS)
        self.temp_7_img = ImageTk.PhotoImage(temp_temperature_7_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/temperature/temp8.png')
        temp_temperature_8_img = img.resize((240, 35), Image.ANTIALIAS)
        self.temp_8_img = ImageTk.PhotoImage(temp_temperature_8_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/temperature/temp9.png')
        temp_temperature_9_img = img.resize((240, 35), Image.ANTIALIAS)
        self.temp_9_img = ImageTk.PhotoImage(temp_temperature_9_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/temperature/temp10.png')
        temp_temperature_10_img = img.resize((240, 35), Image.ANTIALIAS)
        self.temp_10_img = ImageTk.PhotoImage(temp_temperature_10_img)
        
        img = Image.open('/home/stella/env_sensor/env_py_gui/img/temperature/temp11.png')
        temp_temperature_11_img = img.resize((240, 35), Image.ANTIALIAS)
        self.temp_11_img = ImageTk.PhotoImage(temp_temperature_11_img)
        

        
        
        
        
        
        
        
        ##### put modules in frames #####
################################################################################################################################################################
        # from PIL import Image, ImageTk

        #status
        self.time_label = tk.Label(status_part,bg='black',text='', fg='white', font=('Arial', 20))
        self.time_label.grid(column=0, row=0,sticky="W")
        
        non_connection_status_img = Image.open('/home/stella/env_sensor/env_py_gui/img/wifi/non_connection.png')
        resized_non_connection_status_img = non_connection_status_img.resize((20, 20), Image.ANTIALIAS)
        self.photo_non_connection_status = ImageTk.PhotoImage(resized_non_connection_status_img)
        
        
        wifi_connection_status_img = Image.open('/home/stella/env_sensor/env_py_gui/img/wifi/strength/wifi_strength_4.png')
        resized_wifi_connection_status_img = wifi_connection_status_img.resize((20, 20), Image.ANTIALIAS)
        self.photo_wifi_connection_status = ImageTk.PhotoImage(resized_wifi_connection_status_img)
        
        ethernet_connection_status_img = Image.open('/home/stella/env_sensor/env_py_gui/img/wifi/ethernet.png')
        resized_ethernet_connection_status_img = ethernet_connection_status_img.resize((20, 20), Image.ANTIALIAS)
        self.photo_ethernet_connection_status = ImageTk.PhotoImage(resized_ethernet_connection_status_img)
        
        

        # wifi_image = tk.PhotoImage(file='/home/stella/env_sensor/env_py_gui/img/wifi/wifi.png')
        # quit_image = tk.PhotoImage(file='/home/stella/env_sensor/env_py_gui/img/parts/back_button.png')
        
        
        # Temporary Quit Button for DEBUG!!!!!!!!!!
        # quit_button = tk.Button(status_part, image=quit_image, command=controller.destroy, height=20, width=20)
        # quit_button.image = quit_image                  # to keep a ref
        # quit_button.grid(column=1,row=0)

        self.wifi_button = tk.Button(status_part, image=self.photo_wifi_connection_status,highlightthickness=0, command=show_wifi, height=20, width=20, bg='black', bd=0, borderwidth=0)
        self.wifi_button.image = self.photo_wifi_connection_status                  # to keep a ref
        self.wifi_button.grid(column=1,row=0)
        
        
        # Info Screen
        # info_button = tk.Button(status_part, image=info_image, command=show_info, height=20, width=20)
        # info_button.image = info_image                  # to keep a ref
        # info_button.grid(column=3,row=0)
        info_button = self.get_image_instance(status_part, '/home/stella/env_sensor/env_py_gui/img/wifi/info.png', 20, 20, 0, 2, 'NEWS', command=show_info)

        
        # Temporary MQTT Button for DEBUG!!!!!!!!!!
        # mqtt_button = tk.Button(status_part,bg='red',image=quit_image,highlightthickness=0, command=self.send_mqtt_data, height=20, width=20, bd=0, borderwidth=0)
        # mqtt_button.grid(column=4,row=0)
        
        
        # temperature & humidity
        
        # temperature
        # self.set_image(temp_hum_part, '/home/stella/env_sensor/env_py_gui/img/temperature/temp_img.png', row=0, column=0, height=40)
        self.get_image(temp_hum_part,'/home/stella/env_sensor/env_py_gui/img/temperature/temp_img.png', 35, 35, 0, 0, 'NEWS')
        # self.set_label(temp_hum_part, self.temperature, row=0, column=1)
        temp_text = str(self.temperature) + '°C'
        self.temp_label = Label(temp_hum_part, text=temp_text, bg='black', fg='white', font=('Arial', 15))
        self.temp_label.grid(row=0, column=1, sticky='NEWS')
        # self.set_image(temp_hum_part, '/home/stella/env_sensor/env_py_gui/img/temperature/temp5.png', row=0, column=2, height=20)
        self.temp_gauge = self.get_image_instance(temp_hum_part,'/home/stella/env_sensor/env_py_gui/img/temperature/temp5.png', 240, 35, 0, 2, 'NEWS')


        # humidity
        # self.set_image(temp_hum_part, '/home/stella/env_sensor/env_py_gui/img/humidity/humidity_img.png', row=0, column=3, height=40)
        self.get_image(temp_hum_part,'/home/stella/env_sensor/env_py_gui/img/humidity/humidity_img.png', 35, 35, 0, 3, 'NEWS')
        # self.set_label(temp_hum_part, '53%', row=0, column=4)
        hum_text = str(self.humidity) + '%'
        self.humidity_label = Label(temp_hum_part, text=hum_text, bg='black', fg='white', font=('Arial', 15))
        self.humidity_label.grid(row=0, column=4, sticky='NEWS')
        # self.set_image(temp_hum_part, '/home/stella/env_sensor/env_py_gui/img/humidity/humidity5.png', row=0, column=5, height=20)
        self.hum_gauge = self.get_image_instance(temp_hum_part,'/home/stella/env_sensor/env_py_gui/img/humidity/humidity5.png', 240, 35, 0, 5, 'NEWS')
        
        
        
        
        # sensor values
        tvoc_part = tk.Frame(sensor_part,bg="black")
        tvoc_part.grid(row=0,column=0,sticky='NEWS')
        self.set_frame_configure(tvoc_part)
        self.TVOC_label = Label(tvoc_part, text=self.TVOC, bg='black', fg='white', font=('Arial', 15))
        self.TVOC_label.grid(row=1, column=0, sticky='NEWS')
        self.TVOC_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='TVOC'))
        self.TVOC_unit_label = Label(tvoc_part, text='ug/m3', bg='black', fg='white', font=('Arial', 11))
        self.TVOC_unit_label.grid(row=2,column=0)

        
        
        co_part = tk.Frame(sensor_part, bg='black')
        co_part.grid(row=2,column=0,sticky='NEWS')
        self.set_frame_configure(co_part)
        self.CO_label = Label(co_part, text=self.CO, bg='black', fg='white', font=('Arial', 15))
        self.CO_label.grid(row=1, column=0, sticky='NEWS')
        self.CO_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='CO'))
        self.CO_unit_label = Label(co_part, text='PPM', bg='black', fg='white', font=('Arial', 11))
        self.CO_unit_label.grid(row=2,column=0)
        

        co2_part = tk.Frame(sensor_part, bg='black')
        co2_part.grid(row=0,column=2,sticky='NEWS')
        self.set_frame_configure(co2_part)
        self.CO2_label = Label(co2_part, text=self.CO2, bg='black', fg='white', font=('Arial', 15))
        self.CO2_label.grid(row=1, column=0, sticky='NEWS')
        self.CO2_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='CO2'))
        self.CO2_unit_label = Label(co2_part, text='PPM', bg='black', fg='white', font=('Arial', 11))
        self.CO2_unit_label.grid(row=2,column=0)
        
        no2_part = tk.Frame(sensor_part, bg='black')
        no2_part.grid(row=2,column=2,sticky='NEWS')
        self.set_frame_configure(no2_part)
        self.NO2_label = Label(no2_part, text=self.NO2, bg='black', fg='white', font=('Arial', 15))
        self.NO2_label.grid(row=1, column=0, sticky='NEWS')
        self.NO2_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='NO2'))
        self.NO2_unit_label = Label(no2_part, text='PPM', bg='black', fg='white', font=('Arial', 11))
        self.NO2_unit_label.grid(row=2,column=0)
        
        pm25_part = tk.Frame(sensor_part, bg='black')
        pm25_part.grid(row=0,column=4,sticky='NEWS')
        # self.set_frame_configure(pm25_part)
        pm25_part.columnconfigure(0, weight=1)
        pm25_part.rowconfigure(0,weight=2)
        pm25_part.rowconfigure(1,weight=1)
        pm25_part.rowconfigure(2,weight=1)
        pm25_part.rowconfigure(3,weight=1)
        pm25_part.rowconfigure(4,weight=1)
        
        

        self.PM1_label = Label(pm25_part, text=self.PM25, bg='black', fg='white', font=('Arial', 12))
        self.PM1_label.grid(row=1, column=0, sticky='NEWS')
        
        self.PM25_label = Label(pm25_part, text=self.PM25, bg='black', fg='white', font=('Arial', 12))
        self.PM25_label.grid(row=2, column=0, sticky='NEWS')
        
        self.PM25_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='PM25'))
        self.PM25_unit_label = Label(pm25_part, text='ug/m3', bg='black', fg='white', font=('Arial', 11))
        self.PM25_unit_label.grid(row=3,column=0)

        h2s_part = tk.Frame(sensor_part, bg='black')
        h2s_part.grid(row=2,column=4,sticky='NEWS')
        self.set_frame_configure(h2s_part)
        self.H2S_label = Label(h2s_part, text=self.H2S, bg='black', fg='white', font=('Arial', 15))
        self.H2S_label.grid(row=1, column=0, sticky='NEWS')
        self.H2S_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='H2S'))
        self.H2S_unit_label = Label(h2s_part, text='PPM', bg='black', fg='white', font=('Arial', 11))
        self.H2S_unit_label.grid(row=2,column=0)

        pm10_part = tk.Frame(sensor_part, bg='black')
        pm10_part.grid(row=0,column=6,sticky='NEWS')
        self.set_frame_configure(pm10_part)
        self.PM10_label = Label(pm10_part, text=self.PM10, bg='black', fg='white', font=('Arial', 15))
        self.PM10_label.grid(row=1, column=0, sticky='NEWS')
        self.PM10_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='PM10'))
        self.PM10_unit_label = Label(pm10_part, text='ug/m3', bg='black', fg='white', font=('Arial', 11))
        self.PM10_unit_label.grid(row=2,column=0)

        light_part = tk.Frame(sensor_part, bg='black')
        light_part.grid(row=2,column=6,sticky='NEWS')
        self.set_frame_configure(light_part)
        self.Light_label = Label(light_part, text=self.LIGHT, bg='black', fg='white', font=('Arial', 15))
        self.Light_label.grid(row=1, column=0, sticky='NEWS')
        self.Light_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='LIGHT'))
        self.Light_unit_label = Label(light_part, text='lx', bg='black', fg='white', font=('Arial', 11))
        self.Light_unit_label.grid(row=2,column=0)
        

        ch2o_part = tk.Frame(sensor_part, bg='black')
        ch2o_part.grid(row=0,column=8,sticky='NEWS')
        self.set_frame_configure(ch2o_part)
        self.CH2O_label = Label(ch2o_part, text=self.CH2O, bg='black', fg='white', font=('Arial', 15))
        self.CH2O_label.grid(row=1, column=0, sticky='NEWS')
        self.CH2O_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='CH2O'))
        self.CH2O_unit_label = Label(ch2o_part, text='ug/m3', bg='black', fg='white', font=('Arial', 11))
        self.CH2O_unit_label.grid(row=2,column=0)



        sound_part = tk.Frame(sensor_part, bg='black')
        sound_part.grid(row=2,column=8,sticky='NEWS')
        self.set_frame_configure(sound_part)
        self.Sound_label = Label(sound_part, text=self.SOUND, bg='black', fg='white', font=('Arial', 15))
        self.Sound_label.grid(row=1, column=0, sticky='NEWS')
        self.Sound_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='SOUND'))
        self.Sound_unit_label = Label(sound_part, text='dB', bg='black', fg='white', font=('Arial', 11))
        self.Sound_unit_label.grid(row=2,column=0)



        sm_part = tk.Frame(sensor_part, bg='black')
        sm_part.grid(row=0,column=10,sticky='NEWS')
        self.set_frame_configure(sm_part)
        self.Sm_label = Label(sm_part, text=self.Sm, bg='black', fg='white', font=('Arial', 15))
        self.Sm_label.grid(row=1, column=0, sticky='NEWS')
        self.Sm_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='SM'))
        self.Sm_unit_label = Label(sm_part, text='PPM', bg='black', fg='white', font=('Arial', 11))
        self.Sm_unit_label.grid(row=2,column=0)


        rn_part = tk.Frame(sensor_part, bg='black')
        rn_part.grid(row=2,column=10,sticky='NEWS')
        self.set_frame_configure(rn_part)
        self.Rn_label = Label(rn_part, text=self.Rn, bg='black', fg='white', font=('Arial', 15))
        self.Rn_label.grid(row=1, column=0, sticky='NEWS')
        self.Rn_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='RN'))
        self.Rn_unit_label = Label(rn_part, text='Bq/m3', bg='black', fg='white', font=('Arial', 11))
        self.Rn_unit_label.grid(row=2,column=0)


        nh3_part = tk.Frame(sensor_part, bg='black')
        nh3_part.grid(row=0,column=12,sticky='NEWS')
        self.set_frame_configure(nh3_part)
        self.NH3_label = Label(nh3_part, text=self.NH3, bg='black', fg='white', font=('Arial', 15))
        self.NH3_label.grid(row=1, column=0, sticky='NEWS')
        self.NH3_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='NH3'))
        self.NH3_unit_label = Label(nh3_part, text='PPM', bg='black', fg='white', font=('Arial', 11))
        self.NH3_unit_label.grid(row=2,column=0)


        o3_part = tk.Frame(sensor_part, bg='black')
        o3_part.grid(row=2,column=12,sticky='NEWS')
        self.set_frame_configure(o3_part)
        self.O3_label = Label(o3_part, text=self.O3, bg='black', fg='white', font=('Arial', 15))
        self.O3_label.grid(row=1, column=0, sticky='NEWS')
        self.O3_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='O3'))
        self.O3_unit_label = Label(o3_part, text='PPM', bg='black', fg='white', font=('Arial', 11))
        self.O3_unit_label.grid(row=2,column=0)
        
        



        # element_button = ttk.Button(
        #     self,
        #     text="to Element",
        #     command=show_element,
        #     cursor="hand2"
        # )
        # element_button.grid(row=0, column=1, sticky="NEWS", pady = (10,0))


        def event_func(event, sensor_name, sensor_value=0):
            # 순서 바꾸면 안돼!!!!
        #     print('Value : ', end='')
        #     print(sensor_value)
        #     print('Range : ', end='')
        #     print(SENSOR_DICT[sensor_name][2:5])
        #     controller.element_frame.change_image()
        #     Element.change_image(sensor_name)
            controller.sensor_name = sensor_name
            controller.selected_sensor_range = SENSOR_DICT[sensor_name][2:5]
            show_element()
            
        
        
            
###########################################################################################################            
        #tvoc_part - contents
        
        tvoc_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='TVOC', sensor_value=self.controller.TVOC))
        # self.set_image(tvoc_part, '/home/stella/env_sensor/env_py_gui/img/sensor/Main-TVOC.png')
        # self.set_label(tvoc_part, 'TVOC')

        tvoc_img = PhotoImage(file='/home/stella/env_sensor/env_py_gui/img/sensor/Main-TVOC.png')
        tvoc_img_label = Label(tvoc_part, image=tvoc_img, bg='black', height=80)
        tvoc_img_label.image = tvoc_img
        tvoc_img_label.grid(row=0, column=0)
        tvoc_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='TVOC', sensor_value=self.controller.TVOC))

        tvoc_label = Label(tvoc_part, text='TVOC', bg='black', fg='white', font=('Arial', 15))
        tvoc_label.grid(row=3, column=0, sticky='NEWS')
        tvoc_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='TVOC', sensor_value=self.controller.TVOC))
###########################################################################################################
        #co_part - contents

        co_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='CO', sensor_value=self.controller.CO))
        # self.set_image(co_part, '/home/stella/env_sensor/env_py_gui/img/sensor/Main-CO.png')
        # self.set_label(co_part, 'CO')

        co_img = PhotoImage(file='/home/stella/env_sensor/env_py_gui/img/sensor/Main-CO.png')
        co_img_label = Label(co_part, image=co_img, bg='black', height=80)
        co_img_label.image = co_img
        co_img_label.grid(row=0, column=0)
        co_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='CO', sensor_value=self.controller.CO))

        co_label = Label(co_part, text='CO', bg='black', fg='white', font=('Arial', 15))
        co_label.grid(row=3, column=0, sticky='NEWS')
        co_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='CO', sensor_value=self.controller.CO))
###########################################################################################################
        #co2_part - contents

        co2_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='CO2',sensor_value=self.controller.CO2))
        # self.set_image(co2_part, '/home/stella/env_sensor/env_py_gui/img/sensor/Main-CO2.png')
        # self.set_label(co2_part, 'CO2')

        co2_img = PhotoImage(file='/home/stella/env_sensor/env_py_gui/img/sensor/Main-CO2.png')
        co2_img_label = Label(co2_part, image=co2_img, bg='black', height=80)
        co2_img_label.image = co2_img
        co2_img_label.grid(row=0, column=0)
        co2_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='CO2',sensor_value=self.controller.CO2))

        co2_label = Label(co2_part, text='CO₂', bg='black', fg='white', font=('Arial', 15))
        co2_label.grid(row=3, column=0, sticky='NEWS')
        co2_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='CO2',sensor_value=self.controller.CO2))
###########################################################################################################
        #no2_part - contents

        no2_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='NO2', sensor_value=self.controller.NO2))
        # self.set_image(no2_part, '/home/stella/env_sensor/env_py_gui/img/sensor/Main-NO2.png')
        # self.set_label(no2_part, 'NO2')

        no2_img = PhotoImage(file='/home/stella/env_sensor/env_py_gui/img/sensor/Main-NO2.png')
        no2_img_label = Label(no2_part, image=no2_img, bg='black', height=80)
        no2_img_label.image = no2_img
        no2_img_label.grid(row=0, column=0)
        no2_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='NO2', sensor_value=self.controller.NO2))

        no2_label = Label(no2_part, text='NO₂', bg='black', fg='white', font=('Arial', 15))
        no2_label.grid(row=3, column=0, sticky='NEWS')
        no2_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='NO2', sensor_value=self.controller.NO2))
###########################################################################################################
        #pm25_part - contents

        pm25_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='PM25', sensor_value=self.controller.PM25))
        # self.set_image(pm25_part, '/home/stella/env_sensor/env_py_gui/img/sensor/Main-PM2.5.png')
        # self.set_label(pm25_part, 'PM2.5')

        pm25_img = PhotoImage(file='/home/stella/env_sensor/env_py_gui/img/sensor/Main-PM2.5.png')
        pm25_img_label = Label(pm25_part, image=pm25_img, bg='black', height=80)
        pm25_img_label.image = pm25_img
        pm25_img_label.grid(row=0, column=0)
        pm25_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='PM25', sensor_value=self.controller.PM25))

        pm25_label = Label(pm25_part, text='PM1.0 , 2.5', bg='black', fg='white', font=('Arial', 12))
        pm25_label.grid(row=4, column=0, sticky='NEWS')
        pm25_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='PM25', sensor_value=self.controller.PM25))
###########################################################################################################
        #h2s_part - contents

        h2s_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='H2S', sensor_value=self.controller.H2S))
        # self.set_image(h2s_part, '/home/stella/env_sensor/env_py_gui/img/sensor/Main-H2S.png')
        # self.set_label(h2s_part, 'H2S')

        h2s_img = PhotoImage(file='/home/stella/env_sensor/env_py_gui/img/sensor/Main-H2S.png')
        h2s_img_label = Label(h2s_part, image=h2s_img, bg='black', height=80)
        h2s_img_label.image = h2s_img
        h2s_img_label.grid(row=0, column=0)
        h2s_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='H2S', sensor_value=self.controller.H2S))

        h2s_label = Label(h2s_part, text='H₂S', bg='black', fg='white', font=('Arial', 15))
        h2s_label.grid(row=3, column=0, sticky='NEWS')
        h2s_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='H2S', sensor_value=self.controller.H2S))
###########################################################################################################
        #pm10_part - contents

        pm10_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='PM10', sensor_value=self.controller.PM10))
        # self.set_image(pm10_part, '/home/stella/env_sensor/env_py_gui/img/sensor/Main-PM10.png')
        # self.set_label(pm10_part, 'PM10')

        pm10_img = PhotoImage(file='/home/stella/env_sensor/env_py_gui/img/sensor/Main-PM10.png')
        pm10_img_label = Label(pm10_part, image=pm10_img, bg='black', height=80)
        pm10_img_label.image = pm10_img
        pm10_img_label.grid(row=0, column=0)
        pm10_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='PM10', sensor_value=self.controller.PM10))

        pm10_label = Label(pm10_part, text='PM10', bg='black', fg='white', font=('Arial', 15))
        pm10_label.grid(row=3, column=0, sticky='NEWS')
        pm10_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='PM10', sensor_value=self.controller.PM10))
###########################################################################################################
        #light_part - contents

        light_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='LIGHT', sensor_value=self.controller.LIGHT))
        # self.set_image(light_part, '/home/stella/env_sensor/env_py_gui/img/sensor/Main-Light.png')
        # self.set_label(light_part, 'Light')

        light_img = PhotoImage(file='/home/stella/env_sensor/env_py_gui/img/sensor/Main-Light.png')
        light_img_label = Label(light_part, image=light_img, bg='black', height=80)
        light_img_label.image = light_img
        light_img_label.grid(row=0, column=0)
        light_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='LIGHT', sensor_value=self.controller.LIGHT))

        light_label = Label(light_part, text='Light', bg='black', fg='white', font=('Arial', 15))
        light_label.grid(row=3, column=0, sticky='NEWS')
        light_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='LIGHT', sensor_value=self.controller.LIGHT))
###########################################################################################################
        #ch2o_part - contents

        ch2o_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='CH2O', sensor_value=self.controller.CH2O))
        # self.set_image(ch2o_part, '/home/stella/env_sensor/env_py_gui/img/sensor/Main-CH2O.png')
        # self.set_label(ch2o_part, 'CH2O')

        CH2O_img = PhotoImage(file='/home/stella/env_sensor/env_py_gui/img/sensor/Main-CH2O.png')
        CH2O_img_label = Label(ch2o_part, image=CH2O_img, bg='black', height=80)
        CH2O_img_label.image = CH2O_img
        CH2O_img_label.grid(row=0, column=0)
        CH2O_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='CH2O', sensor_value=self.controller.CH2O))

        CH2O_label = Label(ch2o_part, text='CH₂O', bg='black', fg='white', font=('Arial', 15))
        CH2O_label.grid(row=3, column=0, sticky='NEWS')
        CH2O_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='CH2O', sensor_value=self.controller.CH2O))
###########################################################################################################
        #sound_part - contents

        sound_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='SOUND', sensor_value=self.controller.SOUND))
        # self.set_image(sound_part, '/home/stella/env_sensor/env_py_gui/img/sensor/Main-Sound.png')
        # self.set_label(sound_part, 'Sound')

        sound_img = PhotoImage(file='/home/stella/env_sensor/env_py_gui/img/sensor/Main-Sound.png')
        sound_img_label = Label(sound_part, image=sound_img, bg='black', height=80)
        sound_img_label.image = sound_img
        sound_img_label.grid(row=0, column=0)
        sound_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='SOUND', sensor_value=self.controller.SOUND))

        sound_label = Label(sound_part, text='Sound', bg='black', fg='white', font=('Arial', 15))
        sound_label.grid(row=3, column=0, sticky='NEWS')
        sound_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='SOUND', sensor_value=self.controller.SOUND))
###########################################################################################################
        #sm_part - contents

        sm_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='SM', sensor_value=self.controller.Sm))
        # self.set_image(sm_part, '/home/stella/env_sensor/env_py_gui/img/sensor/Main-Sm.png')
        # self.set_label(sm_part, 'Sm')

        Sm_img = PhotoImage(file='/home/stella/env_sensor/env_py_gui/img/sensor/Main-Sm.png')
        Sm_img_label = Label(sm_part, image=Sm_img, bg='black', height=80)
        Sm_img_label.image = Sm_img
        Sm_img_label.grid(row=0, column=0)
        Sm_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='SM', sensor_value=self.controller.Sm))

        Sm_label = Label(sm_part, text='Sm', bg='black', fg='white', font=('Arial', 15))
        Sm_label.grid(row=3, column=0, sticky='NEWS')
        Sm_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='SM', sensor_value=self.controller.Sm))
###########################################################################################################
        #rn_part - contents

        rn_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='RN', sensor_value=self.controller.Rn))
        # self.set_image(rn_part, '/home/stella/env_sensor/env_py_gui/img/sensor/Main-Rn.png')
        # self.set_label(rn_part, 'Rn')

        Rn_img = PhotoImage(file='/home/stella/env_sensor/env_py_gui/img/sensor/Main-Rn.png')
        Rn_img_label = Label(rn_part, image=Rn_img, bg='black', height=80)
        Rn_img_label.image = Rn_img
        Rn_img_label.grid(row=0, column=0)
        Rn_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='RN', sensor_value=self.controller.Rn))

        Rn_label = Label(rn_part, text='Rn', bg='black', fg='white', font=('Arial', 15))
        Rn_label.grid(row=3, column=0, sticky='NEWS')
        Rn_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='RN', sensor_value=self.controller.Rn))
###########################################################################################################
        #nh3_part - contents

        nh3_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='NH3', sensor_value=self.controller.NH3))
        # self.set_image(nh3_part, '/home/stella/env_sensor/env_py_gui/img/sensor/Main-NH3.png')
        # self.set_label(nh3_part, 'NH3')

        NH3_img = PhotoImage(file='/home/stella/env_sensor/env_py_gui/img/sensor/Main-NH3.png')
        NH3_img_label = Label(nh3_part, image=NH3_img, bg='black', height=80)
        NH3_img_label.image = NH3_img
        NH3_img_label.grid(row=0, column=0)
        NH3_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='NH3', sensor_value=self.controller.NH3))

        NH3_label = Label(nh3_part, text='NH₃', bg='black', fg='white', font=('Arial', 15))
        NH3_label.grid(row=3, column=0, sticky='NEWS')
        NH3_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='NH3', sensor_value=self.controller.NH3))
###########################################################################################################
        #o3_part - contents

        o3_part.bind("<Button-1>", lambda event: event_func(event, sensor_name='O3', sensor_value=self.controller.O3))
        # self.set_image(o3_part, '/home/stella/env_sensor/env_py_gui/img/sensor/Main-O3.png')
        # self.set_label(o3_part, 'O3')

        O3_img = PhotoImage(file='/home/stella/env_sensor/env_py_gui/img/sensor/Main-O3.png')
        O3_img_label = Label(o3_part, image=O3_img, bg='black', height=80)
        O3_img_label.image = O3_img
        O3_img_label.grid(row=0, column=0)
        O3_img_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='O3', sensor_value=self.controller.O3))

        O3_label = Label(o3_part, text='O₃', bg='black', fg='white', font=('Arial', 15))
        O3_label.grid(row=3, column=0, sticky='NEWS')
        O3_label.bind("<Button-1>", lambda event: event_func(event, sensor_name='O3', sensor_value=self.controller.O3))
###########################################################################################################  
        ########################################### Separator ###########################################
        # horizontal
        self.set_horizontal_separator_image(sensor_part, 0)
        self.set_horizontal_separator_image(sensor_part, 2)
        self.set_horizontal_separator_image(sensor_part, 4)
        self.set_horizontal_separator_image(sensor_part, 6)
        self.set_horizontal_separator_image(sensor_part, 8)
        self.set_horizontal_separator_image(sensor_part, 10)
        self.set_horizontal_separator_image(sensor_part, 12)
        # vertical
        self.set_vertical_separator_image(sensor_part, 1)
        self.set_vertical_separator_image(sensor_part, 3)
        self.set_vertical_separator_image(sensor_part, 5)
        self.set_vertical_separator_image(sensor_part, 7)
        self.set_vertical_separator_image(sensor_part, 9)
        self.set_vertical_separator_image(sensor_part, 11)
        
        
        
        # temp_img = PhotoImage(file='/home/stella/env_sensor/env_py_gui/img/parts/Main_V_separator.png')
        # temp_img_label = Label(sensor_part, image=temp_img, bg='black')
        # temp_img_label.image = temp_img
        # temp_img_label.grid(row=1, column=0)

    def start_thingsboard_mqtt(self):
        try:
            self.client.connect(THINGSBOARD_HOST, port, 60)
            self.client.loop_start()
            self.network_connected = True
            self.thingsboard_connection_state = True
        except Exception:
            print('No internet Here')
            self.network_connected = False
            self.thingsboard_connection_state = False

    def schedule_mqtt_data(self):
        self.send_mqtt_data()
        self.mqtt_timer = threading.Timer(10.0, self.schedule_mqtt_data)
        self.mqtt_timer.daemon = True
        self.mqtt_timer.start()

    def _telemetry_wire_bytes(self, sensor_data):
        return len(json.dumps(sensor_data, ensure_ascii=False).encode('utf-8'))

    def save_to_memory(self, sensor_data):
        try:
            wire = self._telemetry_wire_bytes(sensor_data)
            with self._data_queue_lock:
                while (
                    self._data_queue_bytes + wire > _TELEMETRY_QUEUE_MAX_BYTES
                    and self.data_queue
                ):
                    _, old_b = self.data_queue.pop(0)
                    self._data_queue_bytes -= old_b
                self.data_queue.append((sensor_data, wire))
                self._data_queue_bytes += wire
        except Exception as e:
            print(f"메모리 저장 실패: {e}")

    def read_from_memory(self):
        with self._data_queue_lock:
            return list(self.data_queue)

    def delete_from_memory(self, index):
        try:
            with self._data_queue_lock:
                _, b = self.data_queue.pop(index)
                self._data_queue_bytes -= b
        except Exception as e:
            print(f"메모리 데이터 삭제 실패: {e}")

    def check_network_status(self):
        try:
            if self.client and self.client.is_connected():
                return True
            self.client.reconnect()
            return True
        except Exception:
            return False

    def start_network_check_thread(self):
        def network_check_loop():
            while True:
                self.network_connected = self.check_network_status()
                if self.network_connected:
                    self.send_queued_data()
                sleep(10)  # 10초마다 확인

        thread = threading.Thread(target=network_check_loop, daemon=True)
        thread.start()

    def send_queued_data(self):
        with self._data_queue_lock:
            for i in range(len(self.data_queue) - 1, -1, -1):
                try:
                    sensor_data, _ = self.data_queue[i]
                    self.client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
                    _, b = self.data_queue.pop(i)
                    self._data_queue_bytes -= b
                except Exception as e:
                    print(f"큐 데이터 전송 실패: {e}")
                    break


    def set_horizontal_separator_image(self, frame, column):
        sep_h_img = PhotoImage(file='/home/stella/env_sensor/env_py_gui/img/parts/Main_H_separator.png')
        sep_h_img_label = Label(frame, image=sep_h_img, bg='black')
        sep_h_img_label.image = sep_h_img
        sep_h_img_label.grid(row=1, column=column, padx=12)
    
    def set_vertical_separator_image(self, frame, column):
        sep_v_img = PhotoImage(file='/home/stella/env_sensor/env_py_gui/img/parts/Main_V_separator.png',height=350)
        sep_v_img_label = Label(frame, image=sep_v_img, bg='black')
        sep_v_img_label.image = sep_v_img
        sep_v_img_label.grid(row=0, column=column, rowspan=3)
    
    
    def set_image(self, frame, img_path, row=0, column=0, height=80):
        img = PhotoImage(file=img_path)
        img_label = Label(frame, image=img, bg='black',height=height)
        img_label.image = img
        img_label.grid(row=row, column=column)
        
        
        
    def set_frame_configure(self, frame):
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0,weight=2)
        frame.rowconfigure(1,weight=1)
        frame.rowconfigure(2,weight=1)
        frame.rowconfigure(3,weight=1)

    def set_label(self, frame, title,row=2, column=0, font_size=15):
        common_label = Label(frame, text=title, bg='black', fg='white', font=('Arial',font_size))
        common_label.grid(row=row, column=column, sticky="NEWS")

    def time_update(self):
        # time_string = strftime('%Y-%m-%d %H:%M:%S')
        time_string = strftime('%Y-%m-%d %H:%M')
        self.time_label.config(text=time_string)
        self.time_label.after(1000, self.time_update)
    
    def lan_connection_update(self):
        connection_state = get_current_connection_state()                       # [ethernet, wlan] <- False(미연결) & True(연결)
        # print(connection_state)                                                 # ex) [False, True] -> wlan 연결 [True, True] -> wlan무시 ethernet연결
        if connection_state[0] == True:         # ethernet mode
                self.lan_state = 'ethernet'                                     # todo : enum으로 나중에 빼면 좋음
                if self.thingsboard_connection_state == False:
                        try:
                                self.client.connect(THINGSBOARD_HOST, port, 60)
                                self.client.loop_start()
                                self.thingsboard_connection_state = True
                        except:
                                self.thingsboard_connection_state = False
                
                # self.wifi_button.config(image='/home/stella/env_sensor/env_py_gui/img/',command=None)
                if self.pre_lan_state != self.lan_state:
                        self.wifi_button.config(image=self.photo_ethernet_connection_status, command=self.show_ethernet)
                        self.wifi_button.image = self.photo_ethernet_connection_status

                notify_esp32_if_wifi_connected()
                self.pre_lan_state = 'ethernet'
        elif connection_state[0] == False and connection_state[1] == True:              # wifi 연결
                self.lan_state = 'wlan'
                if self.thingsboard_connection_state == False:
                        try:
                                self.client.connect(THINGSBOARD_HOST, port, 60)
                                self.client.loop_start()
                                self.thingsboard_connection_state = True
                        except:
                                self.thingsboard_connection_state = False
                
                if self.pre_lan_state != self.lan_state:
                        self.wifi_button.config(image=self.photo_wifi_connection_status, command=self.show_wifi)
                        self.wifi_button.image = self.photo_wifi_connection_status
                        
                notify_esp32_if_wifi_connected()
                self.pre_lan_state = 'wlan'
        elif connection_state[0] == False and connection_state[1] == False:
                self.lan_state = 'none'
                if self.pre_lan_state != self.lan_state:
                        self.wifi_button.config(image=self.photo_non_connection_status, command=self.show_wifi)
                        self.wifi_button.image = self.photo_non_connection_status
                self.pre_lan_state = 'none'
        
        # print(self.lan_state)
        self.after(3000, self.lan_connection_update)
        
    def get_image_instance(self, frame, path, width, height, row, column,sticky, command=None):
        img = Image.open(path)
        resized_img = img.resize((width,height), Image.ANTIALIAS)
        photo_img = ImageTk.PhotoImage(resized_img)
        img_label = Label(frame, image=photo_img, bg='black')
        img_label.image = photo_img
        img_label.grid(row=row, column=column, sticky=sticky)
        def local_click(event):
            if command == None:
                pass
            else:
                command()
        img_label.bind("<Button-1>", local_click)
        return img_label
    
    def get_image(self, frame, path, width, height, row, column,sticky, command=None):
        img = Image.open(path)
        resized_img = img.resize((width,height), Image.ANTIALIAS)
        photo_img = ImageTk.PhotoImage(resized_img)
        img_label = Label(frame, image=photo_img, bg='black')
        img_label.image = photo_img
        img_label.grid(row=row, column=column, sticky=sticky)
        def local_click(event):
            if command == None:
                pass
            else:
                command()
        img_label.bind("<Button-1>", local_click)
    
    
    def send_mqtt_data(self):
        try:
        # while True:
                ct = datetime.now()
                ts = ct.timestamp()
                ts = math.floor(ts*1000)

                if float(self.CO2) <= 0 and float(self.temperature) <= 0 and float(self.humidity) <= 0:
                        return
                        
                try:
                        if self.TVOC > 0:
                                self.avg_count_TVOC += 1
                                self.avg_TVOC += self.TVOC
                        if self.CO2 > 0:
                                self.avg_count_CO2 += 1
                                self.avg_CO2 += self.CO2
                        if self.PM1 > 0:
                                self.avg_count_PM1 += 1
                                self.avg_PM1 += self.PM1
                        if self.PM25 > 0:
                                self.avg_count_PM25 += 1
                                self.avg_PM25 += self.PM25
                        if self.PM10 > 0:
                                self.avg_count_PM10 += 1
                                self.avg_PM10 += self.PM10
                        if self.CH2O > 0:
                                self.avg_count_CH2O += 1
                                self.avg_CH2O += self.CH2O
                        if self.Sm > 0:
                                self.avg_count_Sm += 1
                                self.avg_Sm += self.Sm
                        if self.NH3 > 0:
                                self.avg_count_NH3 += 1
                                self.avg_NH3 += self.NH3
                        if self.CO > 0:
                                self.avg_count_CO += 1
                                self.avg_CO += self.CO
                        if self.NO2 > 0:
                                self.avg_count_NO2 += 1
                                self.avg_NO2 += self.NO2
                        if self.H2S > 0:
                                self.avg_count_H2S += 1
                                self.avg_H2S += self.H2S
                        if self.LIGHT > 0:
                                self.avg_count_LIGHT += 1
                                self.avg_LIGHT += self.LIGHT
                        if self.SOUND > 0:
                                self.avg_count_SOUND += 1
                                self.avg_SOUND += self.SOUND
                        if self.Rn > 0:
                                self.avg_count_Rn += 1
                                self.avg_Rn += self.Rn
                        if self.O3 > 0:
                                self.avg_count_O3 += 1
                                self.avg_O3 += self.O3
                        if self.temperature > 0:
                                self.avg_count_temperature += 1
                                self.avg_temperature += self.temperature
                        if self.humidity > 0:
                                self.avg_count_humidity += 1
                                self.avg_humidity += self.humidity


                except Exception as e:
                        print(f"error bk : {e}")



                sensor_data = {
                'ts': ts,
                'serial': self.Board_Serial_Num,
                'rou':self.ROU,
                'values':{
                        "S_0_0":round(float(self.avg_CH2O/self.avg_count_CH2O), 2)  if self.avg_count_CH2O != 0 else self.prev_CH2O,
                        "S_0_1":int(self.avg_PM25/self.avg_count_PM25) if self.avg_count_PM25 != 0 else self.prev_PM25,
                        "S_0_2":int(self.avg_PM10/self.avg_count_PM10) if self.avg_count_PM10 != 0 else self.prev_PM10,
                        "S_0_3":round(float(self.avg_TVOC/self.avg_count_TVOC),2) if self.avg_count_TVOC != 0 else self.prev_TVOC,
                        "S_0_4":round(float(self.avg_CO2/self.avg_count_CO2),2) if self.avg_count_CO2 != 0 else self.prev_CO2,
                        "S_0_5":round(float(self.avg_temperature/self.avg_count_temperature),2) if self.avg_count_temperature != 0 else self.prev_temperature,
                        "S_0_6":round(float(self.avg_humidity/self.avg_count_humidity),2) if self.avg_count_humidity != 0 else self.prev_humidity,
                        "S_0_7":round(float(self.avg_Rn/self.avg_count_Rn),2) if self.avg_count_Rn != 0 else self.prev_Rn,
                        "S_0_8":round(float(self.avg_SOUND/self.avg_count_SOUND),2) if self.avg_count_SOUND != 0 else self.prev_SOUND,
                        "S_0_9":round(float(self.avg_CO/self.avg_count_CO),2) if self.avg_count_CO != 0 else self.prev_CO,
                        "S_0_10":round(float(self.avg_Sm/self.avg_count_Sm),2) if self.avg_count_Sm != 0 else self.prev_Sm,
                        "S_0_11":round(float(self.avg_NO2/self.avg_count_NO2),2) if self.avg_count_NO2 != 0 else self.prev_NO2,
                        "S_0_12":round(float(self.avg_H2S/self.avg_count_H2S),2) if self.avg_count_H2S != 0 else self.prev_H2S,
                        "S_0_13":round(float(self.avg_NH3/self.avg_count_NH3),2) if self.avg_count_NH3 != 0 else self.prev_NH3,
                        "S_0_14":round(float(self.avg_LIGHT/self.avg_count_LIGHT),2) if self.avg_count_LIGHT != 0 else self.prev_LIGHT,
                        "S_0_15":round(float(self.avg_O3/self.avg_count_O3),2) if self.avg_count_O3 != 0 else self.prev_O3,
                        "S_0_16":int(self.avg_PM1/self.avg_count_PM1) if self.avg_count_PM1 != 0 else self.prev_PM1,
                        "ver":CURRENT_VERSION,
                        }
                }

                # 변경된 데이터가 있는지 확인합니다.
                data_changed = self.has_data_changed(sensor_data['values'])

                current_time = datetime.now()
                #print(f"{current_time}: {sensor_data['values']}")        
                #print(sensor_data)

                # sleep(9)

                

                try:
                        # print(f"{current_time}: {sensor_data['values']}")
                        #print("sensor_data : ",sensor_data)
                        
                        # DoubleVar 값을 변환
                        for key in sensor_data:
                                if isinstance(sensor_data[key], DoubleVar):
                                        sensor_data[key] = sensor_data[key].get()
                        self.sample_count = self.sample_count + 1
                        if self.network_connected:
                                if self.first_sent == False:
                                        self.client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
                                        self.first_sent = True

                        if self.sample_count >= 30:
                                if self.network_connected:
                                        self.client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)                                        
                                
                                else:
                                        # print(f"{current_time}: 네트워크 연결 끊김 - 데이터 메모리 저장")
                                        self.save_to_memory(sensor_data)

                                self.sample_count = 0
                                
                                self.prev_TVOC = self.avg_TVOC
                                self.prev_CO2 = self.avg_CO2
                                self.prev_PM1 = self.avg_PM1
                                self.prev_PM25 = self.avg_PM25
                                self.prev_PM10 = self.avg_PM10
                                self.prev_CH2O = self.avg_CH2O
                                self.prev_Sm = self.avg_Sm
                                self.prev_NH3 = self.avg_NH3
                                self.prev_CO = self.avg_CO
                                self.prev_NO2 = self.avg_NO2
                                self.prev_H2S = self.avg_H2S
                                self.prev_LIGHT = self.avg_LIGHT
                                self.prev_SOUND = self.avg_SOUND
                                self.prev_Rn = self.avg_Rn
                                self.prev_O3 = self.avg_O3
                                self.prev_temperature = self.avg_temperature
                                self.prev_humidity = self.avg_humidity
                                
                                self.avg_TVOC = 0.0
                                self.avg_CO2 = 0.0
                                self.avg_PM1 = 0.0
                                self.avg_PM25 = 0.0
                                self.avg_PM10 = 0.0
                                self.avg_CH2O = 0.0
                                self.avg_Sm = 0.0
                                self.avg_NH3 = 0.0
                                self.avg_CO = 0.0
                                self.avg_NO2 = 0.0
                                self.avg_H2S = 0.0
                                self.avg_LIGHT = 0.0
                                self.avg_SOUND = 0.0
                                self.avg_Rn = 0.0
                                self.avg_O3 = 0.0
                                self.avg_temperature = 0.0
                                self.avg_humidity = 0.0

                                self.avg_count_TVOC = 0
                                self.avg_count_CO2 = 0
                                self.avg_count_PM1 = 0
                                self.avg_count_PM25 = 0
                                self.avg_count_PM10 = 0
                                self.avg_count_CH2O = 0
                                self.avg_count_Sm = 0
                                self.avg_count_NH3 = 0
                                self.avg_count_CO = 0
                                self.avg_count_NO2 = 0
                                self.avg_count_H2S = 0
                                self.avg_count_LIGHT = 0
                                self.avg_count_SOUND = 0
                                self.avg_count_Rn = 0
                                self.avg_count_O3 = 0
                                self.avg_count_temperature = 0
                                self.avg_count_humidity = 0
                        
                        

                        
                        
                except Exception as e:
                        #print('네트워크 연결 x')
                        # print(f'데이터 전송 실패: ', e)
                        # self.db_connected = False
                        # self.start_db_thread()
                        self.network_connected = False  # 추가: 전송 실패 시 네트워크 상태 업데이트
                        # self.save_to_memory(sensor_data)  # 추가: 전송 실패 시 메모리 저장
                                
                # 현재 센서 데이터를 이전 데이터로 저장합니다.
                self.previous_sensor_data = sensor_data['values'].copy()       
                # sleep(10)
        except Exception as e:
                print("send_mqtt_data 예외 발생:", e)
                
    def has_data_changed(self, current_data):
        # 이전 데이터가 없으면 변경이 없다고 가정합니다.
        if self.previous_sensor_data is None:
            return False

        # 이전 데이터와 현재 데이터를 비교합니다.
        for key, value in current_data.items():
            if self.previous_sensor_data.get(key) != value:
                return True

        return False

        
    def get_all_data(self):
        check_value1 = str(self.controller.TVOC)        #  
        check_value2 = str(self.controller.temperature) # 
        check_value3 = str(self.controller.humidity)    # 
        
        
        
        if not check_value1.startswith('PY') and not check_value2.startswith('PY') and not check_value3.startswith('PY'):                    # 원래 이렇게 처리하는게 아닌데.. 시간이 없어서 나중에 고칠 것...
                
                self.temperature = float(self.controller.temperature)
                if self.temperature == -100:
                        self.temp_label.config(text='...')
                else:
                        temperature_2f = "{:.2f}°C".format(self.temperature)
                        self.temp_label.config(text=temperature_2f)
                self.humidity = float(self.controller.humidity)
                if self.humidity < 0:
                        self.humidity_label.config(text='...')
                else:
                        humidity_2f = "{:.2f}%".format(self.humidity)
                        self.humidity_label.config(text=humidity_2f)
                # 밑에 마저 해야한다.
                self.Board_Serial_Num = self.controller.Board_Serial_Num
                self.ROU = self.controller.ROU

                self.TVOC = self.controller.TVOC
                # self.TVOC = self.TVOC * 1.2
                # print('self.TVOC', end='')
                # print(self.TVOC)
                # print(type(self.TVOC))
                
                #32번일 경우 y = 0.1549x + 95.328
                # if self.controller.device_number == 32:
                #         self.TVOC = 0.15429 * self.TVOC + 95.328

                # if self.controller.device_number == 22:
                #         self.TVOC = 0.15429 * self.TVOC + 95.328
                
                # if self.controller.device_number == 13:
                #         self.TVOC = 0.15429 * self.TVOC + 95.328

                # if self.controller.device_number == 5:
                #         self.TVOC = 0.15429 * self.TVOC + 95.328

                # #21번일 경우 y = 0.1549x + 95.328
                # if self.controller.device_number == 23:
                #         self.TVOC = ((0.15429* self.TVOC) + 95.328)
                
                # #23번일 경우 y = 0.1542x + 550.25
                # if self.controller.device_number == 21:
                #         self.TVOC = ((0.1542 * self.TVOC) + 550.25)

                if self.TVOC > 150:
                      calculated_value = self.TVOC
                      self.TVOC_label.config(text=round(calculated_value, 2))
                else:
                        self.TVOC_label.config(text=round(self.TVOC, 2))

                if self.TVOC < 0:
                        self.TVOC_label.config(text='...')

                self.CO2 = self.controller.CO2

                # if self.controller.device_number == 4:
                #         self.CO2 += 210

                # #5번일 경우 y = y=x+210
                # if self.controller.device_number == 5:
                #         self.CO2 += 210

                # if self.controller.device_number == 12:
                #         self.CO2 += 210

                # if self.controller.device_number == 13:
                #         self.CO2 += 210

                # #17번일 경우 y = y=x+210
                # if self.controller.device_number == 17:
                #         self.CO2 += 210   

                # if self.controller.device_number == 19:
                #         self.CO2 = self.CO2 + 200
                
                # #21번일 경우 y = 0.1542x + 550.25
                # if self.controller.device_number == 21:
                #         self.CO2 += 130

                # if self.controller.device_number == 22:
                #         self.CO2 = self.CO2 + 205

                # if self.controller.device_number == 23:
                #         self.CO2 = self.CO2 + 200
                
                # if self.controller.device_number == 30:
                #         self.CO2 = self.CO2 + 200

                # if self.controller.device_number == 32:
                #         self.CO2 = self.CO2 + 200

                # #35번일 경우 y = y=x+210
                # if self.controller.device_number == 35:
                #         self.CO2 += 210
                
                

                if self.CO2 < 0:
                        self.CO2_label.config(text='...')        
                else:
                        self.CO2_label.config(text=self.CO2)

                # 새로운 계산식을 적용
                #self.PM1 = (0.554  * original_PM1) + 5.1584
                self.PM1 = self.controller.PM1
                                
                #PM25_1 = self.controller.PM25 - self.PM1  # PM2.5에서 PM1을 뺌
                self.PM25 = self.controller.PM25                
                
                #self.PM10 = ((self.controller.PM10  -PM25_1) - self.PM1)
                self.PM10 = self.controller.PM10

                # if self.controller.device_number == 0:
                #         self.PM1 = self.PM1 * 0.67
                #         self.PM25 = (self.PM25 - self.PM1 * 1.52)
                #         self.PM10 = self.PM10  - (self.PM25 * 1.33)
                        
                # if self.controller.device_number == 1:
                #         self.PM1 = self.PM1 * 0.63
                #         self.PM25 = (self.PM25 - self.PM1 * 1.67)
                #         self.PM10 = self.PM10  - (self.PM25 * 1.39)

                # if self.controller.device_number == 2:
                #         self.PM1 = self.PM1 * 0.85
                #         self.PM25 = (self.PM25 - self.PM1 * 0.48)
                #         self.PM10 = self.PM10  - (self.PM25 * 0.52)

                # if self.controller.device_number == 3:
                #         self.PM1 = self.PM1 * 0.64
                #         self.PM25 = (self.PM25 - self.PM1 * 1.61)
                #         self.PM10 = self.PM10  - (self.PM25 * 1.35)

                # if self.controller.device_number == 4:
                #         self.PM1 = self.PM1 * 0.71
                #         self.PM25 = (self.PM25 - self.PM1 * 1.26)
                #         self.PM10 = self.PM10  - (self.PM25 * 1.02)

                # if self.controller.device_number == 5:
                #         self.PM1 = self.PM1 * 0.75
                #         self.PM25 = (self.PM25 - self.PM1 * 1.1)
                #         self.PM10 = self.PM10  - (self.PM25 * 2) / 5 - (self.PM25 / 2)

                # if self.controller.device_number == 7:
                #         self.PM1 = self.PM1 * 0.61
                #         self.PM25 = (self.PM25 - self.PM1 * 1.7)
                #         self.PM10 = self.PM10  - (self.PM25 * 1.39)

                # if self.controller.device_number == 9:
                #         self.PM1 = self.PM1 * 0.71
                #         self.PM25 = (self.PM25 - self.PM1 * 1.16)
                #         self.PM10 = self.PM10  - (self.PM25 * 0.86)

                # if self.controller.device_number == 10:
                #         self.PM1 = self.PM1 *0.65
                #         self.PM25 = (self.PM25 - self.PM1 * 1.46)                        
                #         self.PM10 = self.PM10  - (self.PM25 * 1.16)                            

                # if self.controller.device_number == 12:
                #         self.PM1 = self.PM1 * 0.68
                #         self.PM25 = (self.PM25 - self.PM1 * 1.45)
                #         self.PM10 = self.PM10  - (self.PM25 * 1.2)

                # if self.controller.device_number == 13:
                #         self.PM1 = self.PM1 * 0.75
                #         self.PM25 = (self.PM25 - self.PM1 )
                #         self.PM10 = self.PM10  - (self.PM25 * 0.87) 
                
                # if self.controller.device_number == 14:
                #         self.PM1 = self.PM1 * 0.7
                #         self.PM25 = (self.PM25 - self.PM1 * 1.45)
                #         self.PM10 = self.PM10  - (self.PM25 * 2.7) / 2

                # #15번일 경우  y=(PM2.5-PM1.0)x0.554+5.1584
                # if self.controller.device_number == 15:
                #         self.PM1 = self.PM1 * 0.65
                #         self.PM25 = (self.PM25 - self.PM1 * 1.65)                        
                #         self.PM10 = self.PM10  - (self.PM25 * 4.4) / 3

                # if self.controller.device_number == 16:
                #         self.PM1 = self.PM1 * 0.64
                #         self.PM25 = (self.PM25 - self.PM1 * 1.52)                        
                #         self.PM10 = self.PM10  - (self.PM25 * 1.23)   

                # if self.controller.device_number == 19:
                #         self.PM25 = (self.PM25 - self.PM1 *0.73)                        
                #         self.PM10 = self.PM10  - (self.PM25 * 0.69)
                
                # if self.controller.device_number == 20:
                #         self.PM1 = self.PM1 * 0.65
                #         self.PM25 = (self.PM25 - self.PM1 * 1.63)                        
                #         self.PM10 = self.PM10  - (self.PM25 * 1.33)

                # #22번일 경우  y=(PM2.5-PM1.0)x0.612+5.2096
                # if self.controller.device_number == 22:
                #         self.PM1 = self.PM1 * 0.79
                #         self.PM25 = (self.PM25 - self.PM1)                        
                #         self.PM10 = self.PM10  - (self.PM25 * 2) / 5 - (self.PM25 / 2)

                # # 23번일 경우
                # if self.controller.device_number == 23:
                #         self.PM1 = self.PM1 * 0.8
                #         self.PM25 = (self.PM25 - self.PM1 )                     
                #         self.PM10 = self.PM10  - (self.PM25 * 0.91)           

                # if self.controller.device_number == 24:
                #         self.PM1 = self.PM1 * 0.78
                #         self.PM25 = (self.PM25 - self.PM1 * 1.17)                     
                #         self.PM10 = self.PM10  - (self.PM25 * 1.1)           

                # #25번일 경우   y=(PM2.5-PM1.0)x0.5791+4.9836
                # if self.controller.device_number == 25:
                #         self.PM1 = self.PM1 *0.7
                #         self.PM25 = (self.PM25 - self.PM1 * 1.35)                        
                #         self.PM10 = self.PM10  - (self.PM25 * 1.25)

                # if self.controller.device_number == 26:
                #         self.PM1 = self.PM1 *0.64
                #         self.PM25 = (self.PM25 - self.PM1 * 1.46)                        
                #         self.PM10 = self.PM10  - (self.PM25 * 1.06)     

                # if self.controller.device_number == 27:
                #         self.PM25 = (self.PM25 - self.PM1 * 0.48)                        
                #         self.PM10 = self.PM10  - (self.PM25 * 0.5)                                               

                # if self.controller.device_number == 28:
                #         self.PM1 = self.PM1 *0.65
                #         self.PM25 = (self.PM25 - self.PM1 * 1.6)                        
                #         self.PM10 = self.PM10  - (self.PM25 * 4) / 3
                
                # if self.controller.device_number == 29:
                #         self.PM25 = (self.PM25 - self.PM1 * 0.6)                        
                #         self.PM10 = self.PM10  - (self.PM25 * 0.66)

                # if self.controller.device_number == 30:
                #         self.PM1 = self.PM1 * 0.61
                #         self.PM25 = (self.PM25 - self.PM1 * 1.72)
                #         self.PM10 = self.PM10  - (self.PM25 * 1.39)

                # #32번일 경우  y=(pm10 - pm2.5) - pm1.0
                # if self.controller.device_number == 32:
                # #         self.PM1 = self.PM1 * 0.78
                #         self.PM25 = (self.PM25 - self.PM1 * 0.32)
                #         self.PM10 = self.PM10  - (self.PM25 * 0.36)

                # if self.controller.device_number == 33:
                #         self.PM25 = (self.PM25 - self.PM1 * 0.4 )                     
                #         self.PM10 = self.PM10  - (self.PM25 * 0.42)            

                # if self.controller.device_number == 34:
                #         self.PM25 = (self.PM25 - self.PM1 * 0.59 )                     
                #         self.PM10 = self.PM10  - (self.PM25 * 0.59)                                                 
               
                if self.PM1 < 0:
                        self.PM1_label.config(text='...')        
                else:
                        self.PM1_label.config(text=int(self.PM1))

                if self.PM25 < 0:
                        self.PM25_label.config(text='...')        
                else:
                        self.PM25_label.config(text=int(self.PM25))
                        
                if self.PM10 < 0:
                        self.PM10_label.config(text='...')        
                else:
                        self.PM10_label.config(text=int(self.PM10))
                
                #CH20
                self.CH2O = self.controller.CH2O
                # if self.CH2O < 22:
                #         self.CH2O = (self.CH2O * 0.7626) * -1 + 22.794
                # else:
                #        self.CH2O = self.CH2O
                
                # if self.controller.device_number == 4:

                #         self.CH2O = (self.CH2O * 0.7626) * -1 + 22.794
                
                # if self.controller.device_number == 5:
                #         self.CH2O = (self.CH2O * 0.7626) * -1 + 22.794

                # if self.controller.device_number == 12:
                #         self.CH2O = (self.CH2O * 0.7626) * -1 + 22.794
                
                # if self.controller.device_number == 13:
                #         self.CH2O = (self.CH2O * 0.7626) * -1 + 22.794
                
                # if self.controller.device_number == 22:
                #         self.CH2O = (self.CH2O * 0.7626) * -1 + 22.794

                # if self.controller.device_number == 23:
                #         self.CH2O = (self.CH2O * 0.7626) * -1 + 22.794
                
                # if self.controller.device_number == 30:
                #         self.CH2O = (self.CH2O * 0.7626) * -1 + 22.794

                # if self.controller.device_number == 32:
                #         self.CH2O = (self.CH2O * 0.7626) * -1 + 22.794

                if self.CH2O < 0:
                        self.CH2O_label.config(text='...')        
                else:
                        self.CH2O_label.config(text=round(self.CH2O,2))
                
                self.Sm = self.controller.Sm
                if self.Sm < 0:
                        self.Sm_label.config(text='...')        
                else:
                        self.Sm_label.config(text=self.Sm)
                
                self.NH3 = self.controller.NH3
                if self.NH3 < 0:
                        self.NH3_label.config(text='...')        
                else:
                        self.NH3_label.config(text=self.NH3)
                
                self.CO = self.controller.CO
                if self.CO < 0:
                        self.CO_label.config(text='...')        
                else:
                        self.CO_label.config(text=self.CO)
                
                self.NO2 = self.controller.NO2
                if self.NO2 < 0:
                        self.NO2_label.config(text='...')        
                else:
                        self.NO2_label.config(text=self.NO2)
                
                self.H2S = self.controller.H2S
                if self.H2S < 0:
                        self.H2S_label.config(text='...')        
                else:
                        self.H2S_label.config(text=self.H2S)
                
                self.LIGHT = self.controller.LIGHT
                if self.LIGHT < 0:
                        self.Light_label.config(text='...')        
                else:
                        self.Light_label.config(text=self.LIGHT)
                
                self.SOUND = self.controller.SOUND
                if self.SOUND < 0:
                        self.Sound_label.config(text='...')        
                else:
                        self.Sound_label.config(text=self.SOUND)
                
                if self.controller.device_number == 11:
                       self.SOUND = self.SOUND -19
                
                if self.controller.device_number == 34:
                       self.SOUND = self.SOUND -19.7
                
                #self.Rn = ((self.controller.Rn * 37) + 79)
                self.Rn = self.controller.Rn
                # 디바이스 번호가 특정번호인 경우 Rn 값을 조정합니다.
                #if self.controller.device_number == 26:
                #        self.Rn += 100

                #11번일 경우 y=x+140
                # if self.controller.device_number == 11:
                #         self.Rn += 140

                #18번일 경우 y=x+170
                # if self.controller.device_number == 18:
                #         self.Rn += 170

                #28번일 경우 y=x+130
                # if self.controller.device_number == 28:
                #         self.Rn += 130

                #31번일 경우 y=x+130
                # if self.controller.device_number == 31:
                #         self.Rn += 130

                #self.Rn = self.controller.Rn + 130
                if self.Rn < 0:
                        self.Rn_label.config(text='...')        
                else:
                        self.Rn_label.config(text=self.Rn)



                self.O3 = self.controller.O3
                if self.O3 < 0:
                        self.O3_label.config(text='...')        
                else:
                        self.O3_label.config(text=self.O3)
                
                self.change_text_color(self.controller.TVOC_level, self.TVOC_label)
                self.change_text_color(self.controller.CO2_level, self.CO2_label)
                # self.change_text_color(self.controller.PM1_level, self.PM1_label)
                self.change_text_color(self.controller.PM25_level, self.PM25_label)
                self.change_text_color(self.controller.PM10_level, self.PM10_label)
                self.change_text_color(self.controller.CH2O_level, self.CH2O_label)
                self.change_text_color(self.controller.Sm_level, self.Sm_label)
                self.change_text_color(self.controller.NH3_level, self.NH3_label)
                self.change_text_color(self.controller.CO_level, self.CO_label)
                self.change_text_color(self.controller.NO2_level, self.NO2_label)
                self.change_text_color(self.controller.H2S_level, self.H2S_label)
                self.change_text_color(self.controller.LIGHT_level, self.Light_label)
                self.change_text_color(self.controller.SOUND_level, self.Sound_label)
                self.change_text_color(self.controller.Rn_level, self.Rn_label)
                self.change_text_color(self.controller.O3_level, self.O3_label)

                # self.temperature
                # 0~100'C까지
                # if temperature < 0:
                #         print('temperatire error')
                # elif temperature < 5:
                #         self.temperature_level = 0
                #         # self.temp_gauge.config(image)
                # elif temperature < 10:
                #         self.
                temperature = float(self.controller.temperature)
                humidity = float(self.controller.humidity)
                self.change_temp_gauge(temperature)
                self.change_hum_gauge(humidity)
                # print('temperature level : '+ str(self.temperature_level))
                # print('humidity level : ' + str(self.humidity_level))
                # 여기서 바꿔주고
                if self.temperature_level != self.pre_temperature_level:
                        if self.temperature_level == 0:
                                self.temp_gauge.config(image=self.temp_0_img)
                                self.temp_gauge.image = self.temp_0_img
                        elif self.temperature_level == 1:
                                self.temp_gauge.config(image=self.temp_1_img)
                                self.temp_gauge.image = self.temp_1_img
                        elif self.temperature_level == 2:
                                self.temp_gauge.config(image=self.temp_2_img)
                                self.temp_gauge.image = self.temp_2_img
                        elif self.temperature_level == 3:
                                self.temp_gauge.config(image=self.temp_3_img)
                                self.temp_gauge.image = self.temp_3_img
                        elif self.temperature_level == 4:
                                self.temp_gauge.config(image=self.temp_4_img)
                                self.temp_gauge.image = self.temp_4_img
                        elif self.temperature_level == 5:
                                self.temp_gauge.config(image=self.temp_5_img)
                                self.temp_gauge.image = self.temp_5_img
                        elif self.temperature_level == 6:
                                self.temp_gauge.config(image=self.temp_6_img)
                                self.temp_gauge.image = self.temp_6_img
                        elif self.temperature_level == 7:
                                self.temp_gauge.config(image=self.temp_7_img)
                                self.temp_gauge.image = self.temp_7_img
                        elif self.temperature_level == 8:
                                self.temp_gauge.config(image=self.temp_8_img)
                                self.temp_gauge.image = self.temp_8_img
                        elif self.temperature_level == 9:
                                self.temp_gauge.config(image=self.temp_9_img)
                                self.temp_gauge.image = self.temp_9_img
                        elif self.temperature_level == 10:
                                self.temp_gauge.config(image=self.temp_10_img)
                                self.temp_gauge.image = self.temp_10_img
                        elif self.temperature_level == 11:
                                self.temp_gauge.config(image=self.temp_11_img)
                                self.temp_gauge.image = self.temp_11_img
                        else:
                                pass
                        
                if self.humidity_level != self.pre_humidity_level:
                        if self.humidity_level == 0:
                                self.hum_gauge.config(image=self.hum_0_img)
                                self.hum_gauge.image = self.hum_0_img
                        elif self.humidity_level == 1:
                                self.hum_gauge.config(image=self.hum_1_img)
                                self.hum_gauge.image = self.hum_1_img
                        elif self.humidity_level == 2:
                                self.hum_gauge.config(image=self.hum_2_img)
                                self.hum_gauge.image = self.hum_2_img
                        elif self.humidity_level == 3:
                                self.hum_gauge.config(image=self.hum_3_img)
                                self.hum_gauge.image = self.hum_3_img
                        elif self.humidity_level == 4:
                                self.hum_gauge.config(image=self.hum_4_img)
                                self.hum_gauge.image = self.hum_4_img
                        elif self.humidity_level == 5:
                                self.hum_gauge.config(image=self.hum_5_img)
                                self.hum_gauge.image = self.hum_5_img
                        elif self.humidity_level == 6:
                                self.hum_gauge.config(image=self.hum_6_img)
                                self.hum_gauge.image = self.hum_6_img
                        elif self.humidity_level == 7:
                                self.hum_gauge.config(image=self.hum_7_img)
                                self.hum_gauge.image = self.hum_7_img
                        elif self.humidity_level == 8:
                                self.hum_gauge.config(image=self.hum_8_img)
                                self.hum_gauge.image = self.hum_8_img
                        elif self.humidity_level == 9:
                                self.hum_gauge.config(image=self.hum_9_img)
                                self.hum_gauge.image = self.hum_9_img
                        elif self.humidity_level == 10:
                                self.hum_gauge.config(image=self.hum_10_img)
                                self.hum_gauge.image = self.hum_10_img
                        elif self.humidity_level == 11:
                                self.hum_gauge.config(image=self.hum_11_img)
                                self.hum_gauge.image = self.hum_11_img
                        else:
                                pass
                self.pre_temperature_level = self.temperature_level
                self.pre_humidity_level = self.humidity_level
                # print('pre temperature level : '+ str(self.pre_temperature_level))
                # print('pre humidity level : ' + str(self.pre_humidity_level))
        
        # Element.change_image(self.controller.sensor_name)
        self.after(2000, self.get_all_data)

    def change_text_color(self,level, label):
        # print('level : ', level)
        # print('label : ', label)
        if level == 1:
                label.config(fg='blue')
        elif level == 2:
                label.config(fg='green')    
        elif level == 3:
                # label.config(fg='brown')
                label.config(fg='yellow')
        elif level == 4:
                label.config(fg='red')
        #        label.config(fg='yellow')
        else:
                pass
    
    
    def quit_program(self):
        sys.exit()
   
    def change_temp_gauge(self, value):         # temp, hum 을 합치기 실패
        if value < 0:
                # print('error이거나 온도가 너무 낮음')
                self.temperature_level = 0
        elif value < 10:
                self.temperature_level = 1
        elif value < 20:
                self.temperature_level = 2
        elif value < 30:
                self.temperature_level = 3
        elif value < 40:
                self.temperature_level = 4
        elif value < 50:
                self.temperature_level = 5
        elif value < 60:
                self.temperature_level = 6
        elif value < 70:
                self.temperature_level = 7
        elif value < 80:
                self.temperature_level = 8
        elif value < 90:
                self.temperature_level = 9
        elif value < 100:
                self.temperature_level = 10
        elif value >= 100:
                self.temperature_level = 11
        else:
                print('error value')

    def change_hum_gauge(self, value):         # temp, hum 을 합치기 실패
        if value < 0:
                # print('error')
                self.humidity_level = 0
        elif value < 10:
                self.humidity_level = 1
        elif value < 20:
                self.humidity_level = 2
        elif value < 30:
                self.humidity_level = 3
        elif value < 40:
                self.humidity_level = 4
        elif value < 50:
                self.humidity_level = 5
        elif value < 60:
                self.humidity_level = 6
        elif value < 70:
                self.humidity_level = 7
        elif value < 80:
                self.humidity_level = 8
        elif value < 90:
                self.humidity_level = 9
        elif value < 100:
                self.humidity_level = 10
        elif value >= 100:
                self.humidity_level = 11
        else:
                print('error value')



#     def start_db_thread(self):
#         threading.Thread(target=self.connect_to_db, daemon=True).start()

#     def connect_to_db(self):
#         while not self.db_connected:
#             try:
#                 print("DB 연결 시도 중...",THINGSBOARD_HOST)
#                 self.my_db = mysql.connector.connect(
#                     host=THINGSBOARD_HOST,  
#                     user="yot132",          
#                     passwd="tmxjavm67",     
#                     database="airstella"    
#                 )
#                 self.db_connected = True
#                 print("DB 연결 성공:",THINGSBOARD_HOST)
#             except mysql.connector.Error as e:
#                 print(f"DB 연결 실패: {e}")
