# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:01:17 2021

@author: legion
"""

import math
import matplotlib.pyplot as plt

#input
kecepatan_awal = 0
posisi_awal = 100
percepatan = -9.8
t = 0
dt = 0.1

y_numerik  = [posisi_awal]
t_numerik = [t]

y_analitik = [posisi_awal]
t_analitik = [t]


#solusi numerik

print("=========Solusi Numerik==========")
v = kecepatan_awal
y = posisi_awal
t_num = t
while y >= 0:
    v = v+ (percepatan * dt)
    y = y + (v * dt)
    t_num += dt
    print("Posisi Numerik :", y)
    print("Waktu : {:.1f}" . format(t_num))
    print("")
    y_numerik.append(y)
    t_numerik.append(t_num)
    
#solusi analitik
print("=========Solusi Analitik==========")
y_exact = kecepatan_awal
t_exact = t
while y_exact >= 0:
    t_exact += dt
    y_exact = posisi_awal + (0.5 * percepatan * t_exact**2)
    print("Posisi Analitik: ", y_exact)
    print("Waktu : {:.1f}" . format(t_exact))
    print("")
    
    y_analitik.append(y_exact)
    t_analitik.append(t_exact)
    
plt.plot(t_numerik, y_numerik, c='b', label='Numerik')

plt.plot(t_analitik, y_analitik, c='r', label='Analitik')

plt.xlabel('Waktu')
plt.ylabel('Posisi')
plt.xlim(-0.5,5)
plt.ylim(-5,105)
plt.legend()
plt.show()

print("waktu exact: ", float(math.sqrt(2*posisi_awal / (-1* percepatan))))