import tkinter as tk
from tkinter import ttk
from home_screen import Home
from element_screen import Element
from wifi_screen import WifiScreen
from wifi_connection_screen import WifiConnectionScreen
from wifi_detail_screen import WifiDetailScreen
from info_screen import InfoScreen
from keyboard_screen import KeyboardScreen
from ethernet_screen import EthernetScreen
from mac_address import get_mac_address
from ipv4_screen import Ipv4Screen

# 202310281654

import sys
# 여기서 수정한 것이 git 한다.
# 나중에 링크 풀어줘야한다.
from uart_data_thread import UartDataThread
# 제일 처음 수정은 
 
sys.path.append('/home/stella/env_sensor/info')
# DEVICE_NUM -> 1               # 1 <= Device 30000000    device_info[0]
from device_number import DEVICE_NUM

FULL_SCREEN = True             # (True/False) - (Full Screen/Fixed Size Screen)
UART_DATA_VIEW = False
PRIMARY_COLOR = "#2e3f4f"

class EnvSensor(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print('############## test ##############')
        # print(DEVICE_NUM)         # 잘 나오는 것 확인했다.
        # print('- test -')

        self.Board_Serial_Num = ''
        self.ROU = tk.DoubleVar(value=0)
        self.device_number = DEVICE_NUM
        self.uart_data_view = UART_DATA_VIEW
        self.send_term = 1
        self.TVOC = tk.DoubleVar(value=0)
        self.CO2 = tk.DoubleVar(value=0)
        self.PM1 = tk.DoubleVar(value=0)
        self.PM25 = tk.DoubleVar(value=0)
        self.PM10 = tk.DoubleVar(value=0)
        self.CH2O = tk.DoubleVar(value=0)
        self.Sm = tk.DoubleVar(value=0)
        self.NH3 = tk.DoubleVar(value=0)
        self.CO = tk.DoubleVar(value=0)
        self.NO2 = tk.DoubleVar(value=0)
        self.H2S = tk.DoubleVar(value=0)
        self.LIGHT = tk.DoubleVar(value=0)
        self.SOUND = tk.DoubleVar(value=0)
        self.Rn = tk.DoubleVar(value=0)
        self.O3 = tk.DoubleVar(value=0)
        self.temperature = tk.DoubleVar(value=0)
        self.humidity = tk.DoubleVar(value=0)
        self.mac_address = get_mac_address()
        self.wifi_ssid = tk.DoubleVar(value='')
        self.wifi_pw = tk.DoubleVar(value='')
        
        self.TVOC_level = tk.DoubleVar(value=0)             # 0 - 제대로 된 센서 값을 받아오지 못하는 것이다.
        self.CO2_level = tk.DoubleVar(value=0)              # 1 - 좋음
        self.PM1_level = tk.DoubleVar(value=0)
        self.PM25_level = tk.DoubleVar(value=0)             # 2 - 보통
        self.PM10_level = tk.DoubleVar(value=0)             # 3 - 나쁨
        self.CH2O_level = tk.DoubleVar(value=0)             # 4 - 아주 나쁨
        self.Sm_level = tk.DoubleVar(value=0)   
        self.NH3_level = tk.DoubleVar(value=0)  
        self.CO_level = tk.DoubleVar(value=0)   
        self.NO2_level = tk.DoubleVar(value=0)  
        self.H2S_level = tk.DoubleVar(value=0)  
        self.LIGHT_level = tk.DoubleVar(value=0)    
        self.SOUND_level = tk.DoubleVar(value=0)    
        self.Rn_level = tk.DoubleVar(value=0)   
        self.O3_level = tk.DoubleVar(value=0)   
        
        
        
        self.eth0_connection = False            # 초기값은 0으로 잡아준다.
        self.wlan0_connection = False
        

        style = ttk.Style(self)
        style.theme_use("clam")
        
        style.configure("Home.TFrame", background=PRIMARY_COLOR)
        
        self["background"] = PRIMARY_COLOR
        
        self.title("Env LAB")
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight=1)
        self.resizable(False, False)
        # self.sensor_name = tk.StringVar(value='TVOC')
        self.sensor_name = 'TVOC'
        self.selected_sensor_range = []
        container = ttk.Frame(self)
        container.grid(row=0, column=0, sticky="NEWS")
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)
        container.config(width=800, height=480)
        
        self.frames = dict()
        
        #### frames ####
        
        # For Home
        self.home_frame = Home(container, self, lambda: self.show_element_frame(Element), lambda: self.show_frame(WifiScreen), lambda: self.show_frame(InfoScreen), lambda: self.show_frame(EthernetScreen))
        self.home_frame.grid(row=0, column=0, sticky="NESW")
        ############################################################################################################################################
        
        # For Element
        self.element_frame = Element(container, self, lambda: self.show_frame(Home), sensor=self.sensor_name, sensor_range = self.selected_sensor_range)
        self.element_frame.grid(row=0, column=0, sticky="NESW")
        ############################################################################################################################################
        
        # For Wifi
        self.wifi_frame = WifiScreen(container, self, lambda: self.show_frame(Home), lambda: self.show_frame(WifiDetailScreen))
        self.wifi_frame.grid(row=0, column=0, sticky="NEWS")
        ############################################################################################################################################
        
        # For Wifi Connection Screen
        self.wifi_connection_frame = WifiConnectionScreen(container, self, lambda: self.show_frame(WifiScreen))
        self.wifi_connection_frame.grid(row=0, column=0, sticky='NEWS')
        ############################################################################################################################################

        # For Wifi Detail Screen
        self.wifi_detail_frame = WifiDetailScreen(container, self, lambda:self.show_frame(WifiScreen), lambda: self.show_frame(KeyboardScreen))
        self.wifi_detail_frame.grid(row=0, column=0, sticky='NEWS')
        ############################################################################################################################################
        
        # For Info Screen
        self.info_frame = InfoScreen(container, self, lambda:self.show_frame(Home))
        self.info_frame.grid(row=0, column=0, sticky='NEWS')
        ############################################################################################################################################

        # For Ethernet Screen
        self.ethernet_frame = EthernetScreen(container, self, lambda:self.show_frame(Home), lambda: self.show_frame(Ipv4Screen))
        self.ethernet_frame.grid(row=0, column=0, sticky='NEWS')
        ############################################################################################################################################
        
        # For Keyboard Screen
        self.keyboard_frame = KeyboardScreen(container, self, self.wifi_detail_frame.password_entry, lambda:self.show_frame(WifiDetailScreen))
        self.keyboard_frame.grid(row=0, column=0, sticky='NEWS')
        ############################################################################################################################################

        # For Keyboard Screen
        self.ipv4_frame = Ipv4Screen(container, self,  lambda:self.show_frame(EthernetScreen), lambda: self.show_frame(Home))
        self.ipv4_frame.grid(row=0, column=0, sticky='NEWS')
        ############################################################################################################################################

        
        
        self.frames[Home] = self.home_frame
        self.frames[Element] = self.element_frame
        self.frames[WifiScreen] = self.wifi_frame
        self.frames[WifiConnectionScreen] = self.wifi_connection_frame
        self.frames[WifiDetailScreen] = self.wifi_detail_frame
        self.frames[InfoScreen] = self.info_frame
        self.frames[EthernetScreen] = self.ethernet_frame
        self.frames[KeyboardScreen] = self.keyboard_frame
        self.frames[Ipv4Screen] = self.ipv4_frame
        
        # First Screenu
        # self.element_frame.change_image(self.sensor_name)
        self.show_frame(Home)
    
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
    
    def show_element_frame(self, container):
        # Element UI고치느라 주석
        
        # self.element_frame.change_image(self.sensor_name)  
        self.element_frame.check_value()
        frame = self.frames[container]
        frame.tkraise()
    




# if __name__== '__main__':

#     app = EnvSensor()
#     u = UartDataThread(app, UART_DATA_VIEW)
#     u.start()

#     app.home_frame.get_all_data()
#     app.home_frame.time_update()
    
#     # 꼭 풀어줘야함 519
#     app.home_frame.lan_connection_update()
#     app.wifi_frame.new_ver_wifi_func()
#     app.wifi_frame.get_current_wifi()
    
#     app.geometry("800x480")
#     app.attributes('-fullscreen', FULL_SCREEN)
#     app.mainloop()
# self.get_image(sensor_description_part, '/home/orangepi/env_sensor/env_py_gui/img/sensor/CH2O.png', 80, 80, 0, 0, 'NEWS', rowspan=2)
