import numpy as np
import matplotlib.pyplot as plt

with open("C:/Users/tanx0/Downloads/settings (1).txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n") if i.strip()]

data_array = np.loadtxt("C:/Users/tanx0/Downloads/data (1).txt", dtype=int)
voltage_array = data_array * tmp[1]

fig, ax = plt.subplots(figsize=(16, 10), dpi=250)
x = np.arange(len(data_array))
t = x * tmp[0]

ax.plot(t, voltage_array, label='V(t)', c='b', linestyle='-', linewidth=1.5, marker='o', markersize=4, markevery=10)
ax.set_xlabel("Время, мс", fontsize=14)
ax.set_ylabel("Напряжение, В", fontsize=14)
ax.set_title("Процесс зарядки конденсатора в RC цепочке", fontsize=16, ha="center", va="center", wrap=True)
ax.set_xlim([0, t.max() + 0.2])
ax.set_ylim([0, voltage_array.max() + 0.2])
ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
ax.grid(which='minor', linestyle='--', linewidth='0.5', color='gray')
ax.minorticks_on()

charge_time = f"Время заряда = {len(data_array) * tmp[0]:.2f} с"
ax.text(t.max() * 0.6, voltage_array.max() * 0.8, charge_time, fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

ax.legend(fontsize=12)
fig.savefig("graph.svg")
plt.show()
