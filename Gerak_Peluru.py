import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Variabel input
x = 0       # Posisi x awal
y = 0       # Posisi y awal
g = -9.8    # Gravitasi
v0 = 20     # Kecepatan awal
angle = 60  # sudut
t = 0       # waktu
dt = 0.01   # delta t


angle_rad = (angle/360)*(2*np.pi) # sudut dalam radian
vx = v0 * np.cos(angle_rad)       # kecepatan x awal
vy = v0 * np.sin(angle_rad)       # kecepatan y awal
print(vx, vy)


# Inisialisasi array posisi dan waktu untuk solusi numerik
x_arr = [x]
y_arr = [y]
t_arr = [t]


# Solusi Numerik
print("Solusi Numerik")
while y >= 0:
    vy += g*dt
    y += vy*dt
    x += vx*dt
    t += dt
    print("Waktu :", round(t,2), ", Posisi x :", x, ", Posisi y :", y, "\n")
    x_arr.append(x)
    y_arr.append(y)
    t_arr.append(t)

# waktu total yang dibutuhkan
t_total_numerik = t_arr[-1]
# jarak maksimal
jarak_max_numerik = x_arr[-1]
# ketinggian maksimal
tinggi_max_numerik = np.max(y_arr)

# Inisialisasi array posisi untuk solusi analitik
x_arr_analitik = [0]
y_arr_analitik = [0]

# Solusi Analitik
print("Solusi Analitik")
for t in t_arr:
    x_analitik = v0 * np.cos(angle_rad) * t
    y_analitik = (0.5 * g * t**2) + (v0 * np.sin(angle_rad) * t)
    x_arr_analitik.append(x_analitik)
    y_arr_analitik.append(y_analitik)
    print("Waktu :", round(t,2), ", Posisi x :", x_analitik, ", Posisi y :", y_analitik)


# waktu total yang dibutuhkan
t_total_analitik = (2 * v0 * np.sin(angle_rad))/-g
# jarak maksimal
jarak_max_analitik = v0 * np.cos(angle_rad) * t_total_analitik
# ketinggian maksimal
tinggi_max_analitik = (v0**2 * np.sin(angle_rad)**2) / (-2 * g)


print("Solusi Numerik")
print("Waktu total :", t_total_numerik)
print("Jarak Maksimum :", jarak_max_numerik)
print("Tinggi Maksimum :", tinggi_max_numerik)

print("\nSolusi Analitik")
print("Waktu total :", t_total_analitik)
print("Jarak Maksimum :", jarak_max_analitik)
print("Tinggi Maksimum :", tinggi_max_analitik)


#Graph
fig = plt.figure()
plt.plot(x_arr, y_arr, c='b', label='Numerik')
plt.plot(x_arr_analitik, y_arr_analitik, c='r', label='Analitik')
plt.axhline(c='black')
plt.axvline(c='black')
plt.legend()

#Animasi Numerik
fig2, ax, = plt.subplots()
ax.set_xlim(0, 40)
ax.set_ylim(0, 20)
line, = ax.plot(0,0, c="b")

x_data = []
y_data = []
def animate(i):
    x_data.append(x_arr[i])
    y_data.append(y_arr[i])

    line.set_xdata(x_data)
    line.set_ydata(y_data)
    return line,

anima = animation.FuncAnimation(fig2, func=animate,frames=len(x_arr), interval=10)
plt.show()