import numpy as np


# Система диференціальних рівнянь у векторному вигляді
# u = [y, z], тому u[0] це y, а u[1] це z
def F(x, u):
    y, z = u[0], u[1]
    dy = 2 * y - 3 * z
    dz = y - 2 * z + 2 * np.sin(x)
    return np.array([dy, dz])

# Точні розв'язки
def exact_y(x):
    return 3 * np.exp(x) + np.exp(-x) + 3 * np.sin(x)

def exact_z(x):
    return np.exp(x) + np.exp(-x) + 2 * np.sin(x) - np.cos(x)

# Початкові умови та параметри
x0 = 0.0
u0 = np.array([4.0, 1.0])  # [y(0), z(0)]
x_end = 0.5
h = 0.05

# Масив значень x
x_values = np.arange(x0, x_end + h / 2, h)
n = len(x_values)

# Масиви для результатів (розмір n x 2, де стовпці - це y та z)
u_euler = np.zeros((n, 2))
u_heun = np.zeros((n, 2))
u_rk3 = np.zeros((n, 2))
u_rk4 = np.zeros((n, 2))

# Встановлення початкових умов
u_euler[0] = u_heun[0] = u_rk3[0] = u_rk4[0] = u0

# Обчислення
for i in range(n - 1):
    x_i = x_values[i]

    # 1. Метод Ейлера
    u_euler[i + 1] = u_euler[i] + h * F(x_i, u_euler[i])

    # 2. Метод Хойна
    k1_h = F(x_i, u_heun[i])
    k2_h = F(x_i + h, u_heun[i] + h * k1_h)
    u_heun[i + 1] = u_heun[i] + (h / 2) * (k1_h + k2_h)

    # 3. Метод Рунге-Кутта 3-го порядку
    k1_3 = F(x_i, u_rk3[i])
    k2_3 = F(x_i + h / 2, u_rk3[i] + (h / 2) * k1_3)
    k3_3 = F(x_i + h, u_rk3[i] - h * k1_3 + 2 * h * k2_3)
    u_rk3[i + 1] = u_rk3[i] + (h / 6) * (k1_3 + 4 * k2_3 + k3_3)

    # 4. Метод Рунге-Кутта 4-го порядку
    k1_4 = F(x_i, u_rk4[i])
    k2_4 = F(x_i + h / 2, u_rk4[i] + (h / 2) * k1_4)
    k3_4 = F(x_i + h / 2, u_rk4[i] + (h / 2) * k2_4)
    k4_4 = F(x_i + h, u_rk4[i] + h * k3_4)
    u_rk4[i + 1] = u_rk4[i] + (h / 6) * (k1_4 + 2 * k2_4 + 2 * k3_4 + k4_4)

# Вивід результатів
print("Результати для y(x):")
print(f"{'x':<5}  {'Ейлер':<10}  {'Хойн':<10}  {'РК-3':<10}  {'РК-4':<10}  {'Точний (y*)':<10}")
for i in range(n):
    ex_y = exact_y(x_values[i])
    print(
        f"{x_values[i]:<5.2f}  {u_euler[i][0]:<10.6f}  {u_heun[i][0]:<10.6f}  {u_rk3[i][0]:<10.6f}  {u_rk4[i][0]:<10.6f}  {ex_y:<10.6f}")

print("\nРезультати для z(x):")
print(f"{'x':<5}  {'Ейлер':<10}  {'Хойн':<10}  {'РК-3':<10}  {'РК-4':<10}  {'Точний (z*)':<10}")
for i in range(n):
    ex_z = exact_z(x_values[i])
    print(
        f"{x_values[i]:<5.2f}  {u_euler[i][1]:<10.6f}  {u_heun[i][1]:<10.6f}  {u_rk3[i][1]:<10.6f}  {u_rk4[i][1]:<10.6f}  {ex_z:<10.6f}")