import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from datetime import datetime
import sys

handle = open("log.txt")
fout_ts1 = open("log_" + "__sens1_out.txt", 'w')
fout_ts2 = open("log_" + "__sens2_out.txt", 'w')

cnt = 0
ts1_min_val = sys.maxsize
ts1_max_val = -sys.maxsize -1
ts1_arr = []
ts2_min_val = sys.maxsize
ts2_max_val = -sys.maxsize -1
ts2_arr = []
xs = []
xs_ms = []
year_str = '2017-01-01 '

for line in handle:
    start = line.find(",")
    if start > 0:
        space_idx = line.find(',')
        line_time = year_str + line[0:space_idx]
        dt_obj = datetime.strptime(line_time, '%Y-%m-%d %H:%M:%S.%f')
        ms = dt_obj.timestamp() * 1000
        if cnt == 0:
            start_time_ms = ms
        
        sep = len(line)
        line1 = line[start+len(","):sep]
        line1 = line1.lstrip()
        space_idx = line1.find(',')
        line2 = line1[space_idx+len(","):len(line1)-1]
        line1 = line1[0:space_idx]
        line1 = line1.replace(' ', '')
        line2 = line2.replace(' ', '')
        fout_ts1.write(line1 + '\n')
        fout_ts2.write(line2 + '\n')
        xs.append(cnt)
        xs_ms.append((int)(ms - start_time_ms))
        cnt = cnt + 1
        
        #print('---------')
        #print(ms)
        #print((int)(ms - start_time_ms))
        #print(line1)
        #print(line2)
        #print('---------')
        #input()

        ts1_val = int(line1)
        ts1_arr.append(ts1_val)
        if ts1_val > 0:
            if ts1_val < ts1_min_val:
                ts1_min_val = ts1_val
            if ts1_val > ts1_max_val:
                ts1_max_val = ts1_val
                
        ts2_val = int(line2)
        ts2_arr.append(ts2_val)
        if ts2_val > 0:
            if ts2_val < ts2_min_val:
                ts2_min_val = ts2_val
            if ts2_val > ts2_max_val:
                ts2_max_val = ts2_val
        
print("cnt = ", cnt)
print("[1] min_val = ", ts1_min_val)
print("[1] max_val = ", ts1_max_val)
print("[1] mean = ", np.mean(ts1_arr))
print("[1] sko = ", np.std(ts1_arr))
print("[1] disp = ", np.var(ts1_arr))
print("\n")
print("[2] min_val = ", ts2_min_val)
print("[2] max_val = ", ts2_max_val)
print("[2] mean = ", np.mean(ts2_arr))
print("[2] sko = ", np.std(ts2_arr))
print("[2] disp = ", np.var(ts2_arr))

print ('matplotlib ver: ', mpl.__version__)

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 10})

min_val = min(ts1_min_val, ts2_min_val)
max_val = max(ts1_max_val, ts2_max_val)

diap = max_val - min_val
plt.axis([0, max(xs_ms), min_val-diap*0.1, max_val+diap*0.1])

plt.title('Current Sensors')
plt.xlabel('x, ms')
plt.ylabel('0.001 Amp * val')

ax = plt.axes()
ax.xaxis.grid(True)
ax.yaxis.grid(True)

        
ax.minorticks_on()
ax.grid(which='major',
        color = 'k', 
        linewidth = 1)
ax.grid(which='minor', 
        color = 'k', 
        linestyle = ':')        
        
plt.plot(xs_ms, ts1_arr, color = 'blue', linestyle = 'solid',
         label = 'sens_1', marker=".")
plt.plot(xs_ms, ts2_arr, color = 'red', linestyle = 'solid',
         label = 'sens_2', marker=".")
plt.legend(loc = 'upper right')
plt.show()

fout_ts1.close()
fout_ts2.close()
handle.close()
        
input()
        
        
