# from enum import Enum

# class SensorList(Enum):
#     TVOC = 1
#     CO = 2
#     CO2 = 3
#     NO2 = 4
#     PM25 = 5
#     H2S = 6
#     PM10 = 7
#     LIGHT = 8
#     CH2O = 9
#     SOUND = 10
#     SM = 11
#     RN = 12
#     NH3 = 13
#     O3 = 14

# sensorname : ['main에서 쓰이는 img.png', 'element_page에서 쓰이는 img.png']
SENSOR_DICT = {
    'TVOC':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-TVOC.png','/home/stella/env_sensor/env_py_gui/img/sensor/TVOC.png', 200, 500, 1000,500,'ug/m3'],  # ~6.7 : 좋음(1) || ~20 : 보통(2) || ~66.7 : 나쁨(3) || 66.7~ : 아주나쁨(4)        마지막은 권고치
    'CO2':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-CO2.png','/home/stella/env_sensor/env_py_gui/img/sensor/CO2.png', 750, 1000, 1900,1000, 'ppm'],
    'PM1' :['','',10,15,40,20, 'ug/m3'],         # <= temp range
    'PM25':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-PM2.5.png','/home/stella/env_sensor/env_py_gui/img/sensor/PM2.5.png', 25, 35, 75,35,'ug/m3'],
    'PM10':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-PM10.png','/home/stella/env_sensor/env_py_gui/img/sensor/PM10.png', 30, 75, 150,75,'ug/m3'],
    'CH2O':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-CH2O.png','/home/stella/env_sensor/env_py_gui/img/sensor/CH2O.png', 80, 100, 500, 100, 'ug/m3'], # ppm * 30.03 * 1000 / 25.025
    'SM':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-Sm.png','/home/stella/env_sensor/env_py_gui/img/sensor/Sm.png', 0.3, 0.6, 1,0.06, 'ppm'],  # temp
    'NH3':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-NH3.png','/home/stella/env_sensor/env_py_gui/img/sensor/NH3.png', 0.5, 1, 5,1, 'ppm'],
    'CO':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-CO.png','/home/stella/env_sensor/env_py_gui/img/sensor/CO.png', 4, 9, 15,10, 'ppm'],
    'NO2':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-NO2.png','/home/stella/env_sensor/env_py_gui/img/sensor/NO2.png', 0.03, 0.05, 0.2,0.05, 'ppm'],
    'H2S':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-H2S.png','/home/stella/env_sensor/env_py_gui/img/sensor/H2S.png', 0.01, 0.02, 0.3,0.005, 'ppm'],
    'LIGHT':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-LIGHT.png','/home/stella/env_sensor/env_py_gui/img/sensor/LIGHT.png', 2000, 3000, 5000, 1500, 'lx'],
    'SOUND':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-Sound.png','/home/stella/env_sensor/env_py_gui/img/sensor/Sound.png', 40, 50, 60,65, 'dB'],
    'RN':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-Rn.png','/home/stella/env_sensor/env_py_gui/img/sensor/Rn.png', 74, 148, 300,148, 'Bq/m3'],  # unit 설정 필수 일단 pCi/l
    'O3':['/home/stella/env_sensor/env_py_gui/img/sensor/Main-O3.png','/home/stella/env_sensor/env_py_gui/img/sensor/O3.png', 0.03, 0.09, 0.15,0.12, 'ppm'],
}