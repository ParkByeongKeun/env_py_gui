# # using datetime module
from datetime import datetime

ct = datetime.now()
# ct stores current time
# print("current time:-", ct)

# # ts store timestamp of current time
ts = ct.timestamp()
print("timestamp:-", ts)

# # 1684473929.099615
# # 1684473929099    615
# # 소수점 3자리까지 가져온다

# # 1451649600512

# import math
# a = 12345.6789876
# rounded_value = math.floor(a*1000)
# print(rounded_value)