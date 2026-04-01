import random
from time import sleep

co2 = 1000      # ppm
TVOC = 400      # ppb
light = 10
pm1 = 15
pm25 = 35
pm10 = 75
ch2o = 0.1
sound = 60
radon = 200
Sm = 0.05
nh3 = 10
co = 10
h2s = 0.005
o3 = 0.02
no2 = 0.05

# print(random.random())
# print(random.random())
# print(random.random())

percentage = 10

def random_value(name,value):
    ran_value = value + (random.random()*value)/100*percentage
    print(name+'의 정상 수치('+str(value)+')' + ' : ', round(ran_value, 2))

for i in range(10):
    random_value('co2',co2)
    random_value('TVOC',TVOC)
    random_value('light',light)
    random_value('pm1',pm1)
    random_value('pm25',pm25)
    random_value('pm10',pm10)
    random_value('ch2o',ch2o)
    random_value('sound',sound)
    random_value('radon',radon)
    random_value('Sm',Sm)
    random_value('nh3',nh3)
    random_value('co',co)
    random_value('h2s',h2s)
    random_value('o3',o3)
    random_value('no2',no2)
    sleep(2)