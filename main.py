import tkinter as tk
from tkinter import ttk
import math
import matplotlib.pyplot as plt
import numpy as np

# Функция для численного решения ОДУ
def simulate_motion(v0, angle_deg, h0, k, g=9.81, m=1.0, dt=0.01, t_max=10):
    angle_rad = math.radians(angle_deg)
    vx, vy = v0 * math.cos(angle_rad), v0 * math.sin(angle_rad)
    
    # Начальные условия
    x, y = 0, h0
    t = 0
    
    # Массивы для хранения результатов
    x_vals, y_vals, vx_vals, vy_vals, t_vals, speed_vals = [x], [y], [vx], [vy], [t], [v0]
    
    # Метод Рунге-Кутта 4-го порядка
    while y >= 0 and t <= t_max:
        def dx_dt(vx): return vx
        def dy_dt(vy): return vy
        def dvx_dt(vx): return -k / m * vx
        def dvy_dt(vy): return -g - (k / m) * vy

        # Обновление для скорости по x и y
        k1_vx = dvx_dt(vx) * dt
        k1_vy = dvy_dt(vy) * dt
        k2_vx = dvx_dt(vx + 0.5 * k1_vx) * dt
        k2_vy = dvy_dt(vy + 0.5 * k1_vy) * dt
        k3_vx = dvx_dt(vx + 0.5 * k2_vx) * dt
        k3_vy = dvy_dt(vy + 0.5 * k2_vy) * dt
        k4_vx = dvx_dt(vx + k3_vx) * dt
        k4_vy = dvy_dt(vy + k3_vy) * dt
        vx += (k1_vx + 2 * k2_vx + 2 * k3_vx + k4_vx) / 6
        vy += (k1_vy + 2 * k2_vy + 2 * k3_vy + k4_vy) / 6

        # Обновление для координат x и y
        k1_x = dx_dt(vx) * dt
        k1_y = dy_dt(vy) * dt
        k2_x = dx_dt(vx + 0.5 * k1_vx) * dt
        k2_y = dy_dt(vy + 0.5 * k1_vy) * dt
        k3_x = dx_dt(vx + 0.5 * k2_vx) * dt
        k3_y = dy_dt(vy + 0.5 * k2_vy) * dt
        k4_x = dx_dt(vx + k3_vx) * dt
        k4_y = dy_dt(vy + k3_vy) * dt
        x += (k1_x + 2 * k2_x + 2 * k3_x + k4_x) / 6
        y += (k1_y + 2 * k2_y + 2 * k3_y) / 6

        # Обновление времени и значений для графиков
        t += dt
        x_vals.append(x)
        y_vals.append(y)
        vx_vals.append(vx)
        vy_vals.append(vy)
        t_vals.append(t)
        speed_vals.append(math.sqrt(vx**2 + vy**2))

    return t_vals, x_vals, y_vals, vx_vals, vy_vals, speed_vals

# Функция для отображения графиков
def plot_results(t_vals, x_vals, y_vals, vx_vals, vy_vals, speed_vals):
    fig, axs = plt.subplots(3, 1, figsize=(10, 15))

    # Траектория
    axs[0].plot(x_vals, y_vals)
    axs[0].set_xlabel("Горизонтальная позиция (м)")
    axs[0].set_ylabel("Вертикальная позиция (м)")
    axs[0].set_title("Траектория движения")
    axs[0].grid()

    # Скорости
    axs[1].plot(t_vals, vx_vals, label="Скорость по x")
    axs[1].plot(t_vals, vy_vals, label="Скорость по y")
    axs[1].plot(t_vals, speed_vals, label="Скорость (|v|)")
    axs[1].set_xlabel("Время (с)")
    axs[1].set_ylabel("Скорость (м/с)")
    axs[1].legend()
    axs[1].grid()

    # Координаты
    axs[2].plot(t_vals, x_vals, label="x-позиция")
    axs[2].plot(t_vals, y_vals, label="y-позиция")
    axs[2].set_xlabel("Время (с)")
    axs[2].set_ylabel("Координаты (м)")
    axs[2].legend()
    axs[2].grid()

    plt.tight_layout()
    plt.show()

# Функция для запуска симуляции
def run_simulation():
    try:
        v0 = float(entry_v0.get())
        angle = float(entry_angle.get())
        h0 = float(entry_h0.get())
        k = float(entry_k.get())
        
        t_vals, x_vals, y_vals, vx_vals, vy_vals, speed_vals = simulate_motion(v0, angle, h0, k)
        plot_results(t_vals, x_vals, y_vals, vx_vals, vy_vals, speed_vals)
    except ValueError:
        print("Введите корректные числовые значения.")

# Интерфейс с Tkinter
root = tk.Tk()
root.title("Моделирование движения тела")

# Входные параметры
ttk.Label(root, text="Начальная скорость (м/с):").grid(row=0, column=0)
entry_v0 = ttk.Entry(root)
entry_v0.grid(row=0, column=1)

ttk.Label(root, text="Угол (градусы):").grid(row=1, column=0)
entry_angle = ttk.Entry(root)
entry_angle.grid(row=1, column=1)

ttk.Label(root, text="Начальная высота (м):").grid(row=2, column=0)
entry_h0 = ttk.Entry(root)
entry_h0.grid(row=2, column=1)

ttk.Label(root, text="Коэффициент сопротивления (k):").grid(row=3, column=0)
entry_k = ttk.Entry(root)
entry_k.grid(row=3, column=1)

# Кнопка для запуска симуляции
button_run = ttk.Button(root, text="Запустить симуляцию", command=run_simulation)
button_run.grid(row=4, columnspan=2)

root.mainloop()
