import matplotlib.pyplot as plt
import numpy as np
import psutil
import os

d = {0: 0.19849878712984576,
5000: 0.093917341754771386,
10000: 0.075060643507712022,
20000: 0.06673074282575861,
30000: 0.057119318961966224,
50000: 0.046134834546203485,
100000: 0.032495766396631424,
200000: 0.018536317451599615,
500000: 0.0059499290585381479}

lists = sorted(d.items()) # sorted by key, return a list of tuples

x, y = zip(*lists) # unpack a list of pairs into two tuples

plt.plot(x, y)
plt.show()
print("Elapsed time during the whole program in nanoseconds:",(t1_stop-t1_start)*60*60)