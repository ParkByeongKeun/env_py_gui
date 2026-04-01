from threading import Thread, Lock
import serial
import pyautogui
from sensor_list import SENSOR_DICT
pyautogui.FAILSAFE = False
from collections import defaultdict
import re
import math
import random

# 나중에 음수로 오면 error이니깐 -> 핸들링 작업 해야함


class UartDataThread(Thread):
    def __init__(self, controller, view):
        Thread.__init__(self)
        self.view = view
        self.buffer = ""  
        self.last_processed_line = ""

        self.serialport = serial.Serial('/dev/ttyAMA3', 115200, timeout=0.1)
        self.two_pos = [[0,0],[0,0]]
        self.last_x = 0                             # 근데 흠...
        self.last_y = 0
        self.x = 0
        self.y = 0
        self.TVOC = 1.0
        self.CO2 = 0
        self.PM1 = 0
        self.PM25 = 0
        self.PM10 = 0
        self.CH2O = 0
        self.Sm = 0
        self.NH3 = 0
        self.CO = 0
        self.NO2 = 0
        self.H2S = 0
        self.LIGHT = 0
        self.SOUND = 0
        self.Rn = 0
        self.O3 = 0
        self.temperature = 0
        self.humidity = 0
        self.controller = controller
        self.lock = Lock()
        
        self.TVOC_level = 0                 # 0 - 제대로 된 센서 값을 받아오지 못하는 것이다.
        self.CO2_level = 0                  # 1 - 좋음
        self.PM1_level = 0
        self.PM25_level = 0                 # 2 - 보통
        self.PM10_level = 0                 # 3 - 나쁨
        self.CH2O_level = 0                 # 4 - 아주 나쁨
        self.Sm_level = 0
        self.NH3_level = 0
        self.CO_level = 0
        self.NO2_level = 0
        self.H2S_level = 0
        self.LIGHT_level = 0
        self.SOUND_level = 0
        self.Rn_level = 0
        self.O3_level = 0

        self.controller.TVOC = 0
        self.controller.CO2 = 0
        self.controller.PM1 = 0
        self.controller.PM25 = 0
        self.controller.PM10 = 0
        self.controller.CH2O = 0
        self.controller.Sm = 0
        self.controller.NH3 = 0
        self.controller.CO = 0
        self.controller.NO2 = 0
        self.controller.H2S = 0
        self.controller.LIGHT = 0
        self.controller.SOUND = 0
        self.controller.Rn = 0
        self.controller.O3 = 0
        self.controller.temperature = 0
        self.controller.humidity = 0
        
    # def show_data(self):
    #     print(self.TVOC)
    #     print(self.CO2)
        
        
    def run(self):
        while True:
            self.lock.acquire()
            try:
                raw_line = self.serialport.readline()
                if raw_line:
                    line = raw_line.decode('utf-8').strip()
                    self.parse_line(line)
            except Exception as e:
                print(f"Error reading serial data: {e}")
            finally:
                self.lock.release()

    def parse_line(self, line):
        clean_line = line.replace('\t', '').strip()
        if ':' in clean_line:
            key, value = clean_line.split(':', 1)
            key = key.strip().strip('"')
            value = value.strip().strip('"')
            value = value.replace(',', '')

            if value.isdigit():
                value = int(value)
            else:
                try:
                    value = float(value)
                except ValueError:
                    pass

            if str(value).endswith('"'):
                value = str(value).rstrip('"')

            self.process_parsed_data(key, value)

    def calculate_M(self, sensitivity_code, tia_gain):
        return sensitivity_code * tia_gain * 1e-9 * 1e3

    def calculate_ppm(self, V_gas, V_gas0, M):
        return (1 / M) * (V_gas - V_gas0)

    def adc_to_voltage(self, adc_value, reference_voltage=3.3, max_adc_value=65536):
        return reference_voltage*(adc_value / max_adc_value)

    def calculate_sensor_ppm(self, adc_value, sensitivity_code, tia_gain, V_gas0, reference_voltage=3.3):
        temp_adc = adc_value * 2.5/reference_voltage
        V_gas = self.adc_to_voltage(temp_adc, reference_voltage)
        M = self.calculate_M(sensitivity_code, tia_gain)
        C_x = self.calculate_ppm(V_gas, V_gas0, M)
        return round(C_x, 4)

    def calculate_nh3_ppm(self, adv_value):
        max_adc_value = 65536
        r0 = 1000
        sensitivity_factor = 15
        temp_c_rs = 0.8351
        inclination = -0.011083
        temp_adc5v = adv_value*2.5/5
        temp_voltage = 5*temp_adc5v/(max_adc_value)
        rs = ((5-temp_voltage)/temp_voltage)*r0
        calc_rs = rs/r0
        result = calc_rs / sensitivity_factor
        log_result = math.log(result)
        C_x = log_result/inclination + 1
        if C_x <= 0: 
            return round(float(random.uniform(0.200, 0.270)), 3)
        else:
            return round((C_x), 3)

    def ugm3_to_ppm(self, ug_per_m3, molecular_weight, temperature_c=0.0, pressure_mmhg=760.0):
        mg_per_m3 = ug_per_m3 / 1000.0
        molar_volume = 22.4  # L/mol (표준상태)

        temp_factor = 273.0 / (273.0 + temperature_c)
        pressure_factor = pressure_mmhg / 760.0

        denominator = (molecular_weight / molar_volume) * temp_factor * pressure_factor
        ppm = mg_per_m3 / denominator
        return ppm
        
    def process_parsed_data(self, key, value):

        if key == "Board_Serial_Num":
            self.controller.Board_Serial_Num = value
        
        elif key == "CO2_ppm":
            self.controller.CO2 = float(value)
            self.CO2 = float(value)

        elif key == "PM2008_PM1.0_GRIMM":
            self.controller.PM1 = float(value)
            self.PM1 = float(value)

        elif key == "PM2008_PM2.5_GRIMM":
            self.controller.PM25 = float(value)
            self.PM25 = float(value)

        elif key == "PM2008_PM10_GRIMM":
            self.controller.PM10 = float(value)
            self.PM10 = float(value)

        elif key == "RS9A_Val":
            self.controller.Rn = float(value)
            self.Rn = float(value)

        elif key == "RS9A_ROU":
            self.controller.ROU = float(value)

        elif key == "ALS_lux":
            self.controller.LIGHT = float(value)
            self.LIGHT = float(value)

        elif key == "ADC_HW_v1(2.5V_ref)_H2S_val":
            self.controller.H2S = float(value)
            self.H2S = float(value)

        elif key == "ADC_HW_v1(2.5V_ref)_O3_val":
            self.controller.O3 = float(value)
            self.O3 = float(value)

        elif key == "ADC_HW_v1(2.5V_ref)_CO_val":
            self.controller.CO = float(value)
            self.CO = float(value)

        elif key == "ADC_HW_v1(2.5V_ref)_NO2_val":
            self.controller.NO2 = float(value)
            self.NO2 = float(value)

        elif key == "ADC_HW_v1(2.5V_ref)_NH3_val":
            self.controller.NH3 = float(value)
            self.NH3 = float(value)

        elif key == "SHT40_T":
            self.controller.temperature = float(value)
            self.temperature = float(value)

        elif key == "SHT40_RH":
            self.controller.humidity = float(value)
            self.humidity = float(value)

        elif key == "SGP40_Voc_index":
            self.controller.TVOC = float(value)
            self.TVOC = float(value)
            
            molecular_weight = 30  
            temperature = 5        
            pressure = 960         
            ppm_tvoc = round(float(self.ugm3_to_ppm(float(value), molecular_weight, temperature, pressure)), 3)
            
            self.controller.Sm = ppm_tvoc
            self.Sm = ppm_tvoc
            

        elif key == "PDM_Avg":
            # log_value = 20 * math.log10(float(value))

            self.controller.SOUND = float(value)
            self.SOUND = float(value)

        elif key == "CH2O_ug_per_m3":
            self.controller.CH2O = float(value)
            self.CH2O = float(value)
        
        

        # self.last_x = 0
        # self.last_y = 0
        # self.ROU = float(0)
        # self.Board_Serial_Num = ''
        # self.TVOC = float(0)
        # self.CH2O = float(0)
        # self.Sm = float(0)
        # self.NH3 = float(0)
        # self.CO = float(0)
        # self.NO2 = float(0)
        # self.H2S = float(0)
        # self.LIGHT = float(0)
        # self.SOUND = float(0)
        # self.O3 = float(0)
        # self.temperature = float(0)
        # self.humidity = float(0)
        
        
        # self.controller.TVOC = float(0)
        # self.controller.CH2O = float(0)
        # self.controller.Sm = float(0)
        # self.controller.NH3 = float(0)
        # self.controller.CO = float(0)
        # self.controller.NO2 = float(0)
        # self.controller.H2S = float(0)
        # self.controller.LIGHT = float(0)
        # self.controller.SOUND = float(0)
        # self.controller.O3 = float(0)
        # self.controller.temperature = float(0)
        # self.controller.humidity = float(0)
        
        for k, v in SENSOR_DICT.items():
            if k == 'TVOC':
                if self.TVOC >= 0:
                    if self.TVOC < v[2]:
                        self.controller.TVOC_level = 1
                        continue
                    elif self.TVOC < v[3]:
                        self.controller.TVOC_level = 2
                        continue
                    elif self.TVOC < v[4]:
                        self.controller.TVOC_level = 3
                        continue
                    else:
                        self.controller.TVOC_level = 4
                        continue
                else:
                    self.controller.TVOC_level = 0
                    continue
            elif k == 'CO2':
                if self.CO2 >= 0:
                    if self.CO2 < v[2]:
                        self.controller.CO2_level = 1
                        continue
                    elif self.CO2 < v[3]:
                        self.controller.CO2_level = 2
                        continue
                    elif self.CO2 < v[4]:
                        self.controller.CO2_level = 3
                        continue
                    else:
                        self.controller.CO2_level = 4
                        continue
                else:
                    self.controller.CO2_level = 0
                    continue
            elif k == 'PM1':
                if self.PM1 >= 0:
                    if self.PM1 < v[2]:
                        self.controller.PM1_level = 1
                        continue
                    elif self.PM1 < v[3]:
                        self.controller.PM1_level = 2
                        continue
                    elif self.PM1 < v[4]:
                        self.controller.PM1_level = 3
                        continue
                    else:
                        self.controller.PM1_level = 4
                        continue
                else:
                    self.controller.PM1_level = 0
                    continue
            elif k == 'PM25':
                if self.PM25 >= 0:
                    if self.PM25 < v[2]:
                        self.controller.PM25_level = 1
                        continue
                    elif self.PM25 < v[3]:
                        self.controller.PM25_level = 2
                        continue
                    elif self.PM25 < v[4]:
                        self.controller.PM25_level = 3
                        continue
                    else:
                        self.controller.PM25_level = 4
                        continue
                else:
                    self.controller.PM25_level = 0
                    continue
            elif k == 'PM10':
                if self.PM10 >= 0:
                    if self.PM10 < v[2]:
                        self.controller.PM10_level = 1
                        continue
                    elif self.PM10 < v[3]:
                        self.controller.PM10_level = 2
                        continue
                    elif self.PM10 < v[4]:
                        self.controller.PM10_level = 3
                        continue
                    else:
                        self.controller.PM10_level = 4
                        continue
                else:
                    self.controller.PM10_level = 0
                    continue
            elif k == 'CH2O':
                if self.CH2O >= 0:
                    if self.CH2O < v[2]:
                        self.controller.CH2O_level = 1
                        continue
                    elif self.CH2O < v[3]:
                        self.controller.CH2O_level = 2
                        continue
                    elif self.CH2O < v[4]:
                        self.controller.CH2O_level = 3
                        continue
                    else:
                        self.controller.CH2O_level = 4
                        continue
                else:
                    self.controller.CH2O_level = 0
                    continue
            elif k == 'SM':
                if self.Sm >= 0:
                    if self.Sm < v[2]:
                        self.controller.Sm_level = 1
                        continue
                    elif self.Sm < v[3]:
                        self.controller.Sm_level = 2
                        continue
                    elif self.Sm < v[4]:
                        self.controller.Sm_level = 3
                        continue
                    else:
                        self.controller.Sm_level = 4
                        continue
                else:
                    self.controller.Sm_level = 0
                    continue
            elif k == 'NH3':
                if self.NH3 >= 0:
                    if self.NH3 < v[2]:
                        self.controller.NH3_level = 1
                        continue
                    elif self.NH3 < v[3]:
                        self.controller.NH3_level = 2
                        continue
                    elif self.NH3 < v[4]:
                        self.controller.NH3_level = 3
                        continue
                    else:
                        self.controller.NH3_level = 4
                        continue
                else:
                    self.controller.NH3_level = 0
                    continue
            elif k == 'CO':
                if self.CO >= 0:
                    if self.CO < v[2]:
                        self.controller.CO_level = 1
                        continue
                    elif self.CO < v[3]:
                        self.controller.CO_level = 2
                        continue
                    elif self.CO < v[4]:
                        self.controller.CO_level = 3
                        continue
                    else:
                        self.controller.CO_level = 4
                        continue
                else:
                    self.controller.CO_level = 0
                    continue
            elif k == 'NO2':
                if self.NO2 >= 0:
                    if self.NO2 < v[2]:
                        self.controller.NO2_level = 1
                        continue
                    elif self.NO2 < v[3]:
                        self.controller.NO2_level = 2
                        continue
                    elif self.NO2 < v[4]:
                        self.controller.NO2_level = 3
                        continue
                    else:
                        self.controller.NO2_level = 4
                        continue
                else:
                    self.controller.NO2_level = 0
                    continue
            elif k == 'H2S':
                if self.H2S >= 0:
                    if self.H2S < v[2]:
                        self.controller.H2S_level = 1
                        continue
                    elif self.H2S < v[3]:
                        self.controller.H2S_level = 2
                        continue
                    elif self.H2S < v[4]:
                        self.controller.H2S_level = 3
                        continue
                    else:
                        self.controller.H2S_level = 4
                        continue
                else:
                    self.controller.H2S_level = 0
                    continue
            elif k == 'LIGHT':
                if self.LIGHT >= 0:
                    if self.LIGHT < v[2]:
                        self.controller.LIGHT_level = 1
                        continue
                    elif self.LIGHT < v[3]:
                        self.controller.LIGHT_level = 2
                        continue
                    elif self.LIGHT < v[4]:
                        self.controller.LIGHT_level = 3
                        continue
                    else:
                        self.controller.LIGHT_level = 4
                        continue
                else:
                    self.controller.LIGHT_level = 0
                    continue
            elif k == 'SOUND':
                if self.SOUND >= 0:
                    if self.SOUND < v[2]:
                        self.controller.SOUND_level = 1
                        continue
                    elif self.SOUND < v[3]:
                        self.controller.SOUND_level = 2
                        continue
                    elif self.SOUND < v[4]:
                        self.controller.SOUND_level = 3
                        continue
                    else:
                        self.controller.SOUND_level = 4
                        continue
                else:
                    self.controller.SOUND_level = 0
                    continue
            elif k == 'RN':
                if self.Rn >= 0:
                    if self.Rn < v[2]:
                        self.controller.Rn_level = 1
                        continue
                    elif self.Rn < v[3]:
                        self.controller.Rn_level = 2
                        continue
                    elif self.Rn < v[4]:
                        self.controller.Rn_level = 3
                        continue
                    else:
                        self.controller.Rn_level = 4
                        continue
                else:
                    self.controller.Rn_level = 0
                    continue
            elif k == 'O3':
                if self.O3 >= 0:
                    if self.O3 < v[2]:
                        self.controller.O3_level = 1
                        continue
                    elif self.O3 < v[3]:
                        self.controller.O3_level = 2
                        continue
                    elif self.O3 < v[4]:
                        self.controller.O3_level = 3
                        continue
                    else:
                        self.controller.O3_level = 4
                        continue
                else:
                    self.controller.O3_level = 0
                    continue
            else:
                print('uart k, v 에서 잘못되었다... 왜?')


###################################### self.serial_str ######################################
# 0 - touch x
# 1 - touch y
# 2 - TVOC
# 3 - CO2
# 4 - PM2.5
# 5 - PM10
# 6 - CH2O
# 7 - Sm
# 8 - NH3
# 9 - CO
# 10 - NO2
# 11 - H2S
# 12 - Light
# 13 - Sound
# 14 - Rn
# 15 - O3
# 16 - Temperature
# 17 - Humidity
