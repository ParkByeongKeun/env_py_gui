import serial
import tkinter as tk
import pyautogui
from time import sleep


serialport = serial.Serial('/dev/ttyS5', 115200, timeout=0.1)

pyautogui.FAILSAFE = False

two_pos = [[0,0], [0,0]]

last_x = 0
last_y = 0




try:
    while 1:
        serial_str = str(serialport.readline())[2:-5]
        if serial_str == '':
            print('No Data')
            # two_pos[1] = [-1,-1]
            two_pos = [[last_x, last_y], [-1, -1]]
            if (two_pos[0] != [-1,-1]) and (two_pos[1] == [-1, -1]):
                pyautogui.click()
            
            last_x = -1
            last_y = -1
            
            

            
        else:
            temp_list = serial_str.split(",")
            x, y = float(temp_list[0]), float(temp_list[-1])
            x = int((x-180)/3740*799)
            y = int((y-400)/3410*479)
            two_pos = [[last_x, last_y],[x, y]]
            last_x = x
            last_y = y
            # print('x : ', x, ' & ', 'y : ', y)
            pyautogui.moveTo(x, y)
            
            
except KeyboardInterrupt:
    pass

