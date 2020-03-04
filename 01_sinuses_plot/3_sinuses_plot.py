import numpy as np
import math as math
import matplotlib.pyplot as plt
import matplotlib as mpl

ampl = 100
delta = 0.0
n = 6
#-------------------
pi = math.pi
xrange = np.arange(0, 6, 0.001)
sn1 = []
sn2 = []
sn3 = []
for x in xrange:
    sn1.append(ampl * math.sin((x + delta)*6 + 0))
    sn2.append(ampl * math.sin((x + delta)*6 + 2*pi/3))
    sn3.append(ampl * math.sin((x + delta)*6 + 4*pi/3))

#---------------------
print ('matplotlib ver: ', mpl.__version__)
dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 10})

min_val = min(sn1)
max_val = max(sn1)

plt.axis([0, max(xrange), min_val-20, max_val+20])

plt.title('3 sinuses with phase offset')
plt.xlabel('x, * 0.001 rad')
plt.ylabel('sn(x)')

ax = plt.axes()
ax.xaxis.grid(True)
ax.yaxis.grid(True)

#locator = mpl.ticker.MultipleLocator (base=1.0)
#ax.xaxis.set_major_locator (locator)
        
ax.minorticks_on()
ax.grid(which='major',
        color = 'k', 
        linewidth = 1)
ax.grid(which='minor', 
        color = 'k', 
        linestyle = ':')        
        
plt.plot(xrange, sn1, color = 'blue', linestyle = '-',
         label = 'sn1', marker=".")
plt.plot(xrange, sn2, color = 'red', linestyle = '-',
         label = 'sn2', marker=".")
plt.plot(xrange, sn3, color = 'green', linestyle = '-',
         label = 'sn3', marker=".")
plt.legend(loc = 'upper right')
plt.show()
        
input()