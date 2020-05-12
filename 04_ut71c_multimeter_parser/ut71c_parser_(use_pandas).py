#########################################
#   C:\Users\x1x\AppData\Local\Programs\Python\Python37>python.exe -m pip install xlrd
#   Collecting xlrd
#     Downloading xlrd-1.2.0-py2.py3-none-any.whl (103 kB)
#       |████████████████████████████████| 103 kB 1.1 MB/s
#   Installing collected packages: xlrd
#   Successfully installed xlrd-1.2.0
############################################


import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from datetime import datetime
import sys
import pandas as pd

file_name = r'board_power.xls'
df = pd.read_table(file_name, header=0,sep=r"\s+")
#print(df['Value'][:3]) - print first 3 lines
#print(df.iloc[0,3]) - print first row, 3d column value
print('row count = ', len(df.index))

X_ts_df = df['Time']
Y_V_df = df['Value']
X_ts = []
Y_V = []
i = 0
while i < len(df.index):
    time_str = '2017-01-01 ' + X_ts_df[i]
    dt_obj = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    ts = dt_obj.timestamp()
    if i == 0:
        start_ts = ts
    X_ts.append((int)(ts - start_ts))
    #print((int)(ts - start_ts))
    Y_V.append(float(Y_V_df[i].replace(',', '.')))
    #print(float(Y_V_df[i].replace(',', '.')))
    i = i + 1
    #input()

print ('matplotlib ver: ', mpl.__version__)

#-----------------------------------------------------
dpi = 96
fig = plt.figure(dpi = dpi, figsize = (800 / dpi, 600 / dpi) )
mpl.rcParams.update({'font.size': 10})

min_val = min(Y_V)
max_val = max(Y_V)
diap = max_val - min_val
plt.axis([0, max(X_ts), min_val-diap*0.1, max_val+diap*0.1])
print('Y_V_min = ', min_val)
print('Y_V_max = ', max_val)
print('Y_V_diap = ', diap)
print('Y[] = ', min_val-diap*0.1, max_val+diap*0.1)

plt.title('UT71C, voltage, ' + file_name)
plt.xlabel('s')
plt.ylabel('Volts')

ax = plt.axes()
ax.xaxis.grid(True)
ax.yaxis.grid(True)

        
ax.minorticks_on()
ax.grid(which='major',
        color = 'k', 
        linewidth = 1)       
        
plt.plot(X_ts, Y_V, color = 'blue', linestyle = 'solid',
         label = 'accum model x', marker=".")

plt.legend(loc = 'upper right')
plt.show()

input()