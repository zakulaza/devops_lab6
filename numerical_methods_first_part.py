import numpy as np


# Задана функція f(x, y) = y'
def f(x, y):
    return 2 * x ** 3 + 2 * y / x


# Точний розв'язок
def exact_solution(x):
    return x ** 4 + x ** 2


# Початкові умови та параметри
x0 = 1
y0 = 2.0
x_end = x0 + 1
h = 0.1

# Масив значень x
x_values = np.arange(x0, x_end + h / 2, h)
n = len(x_values)

# Масиви для збереження результатів
y_euler = np.zeros(n)
y_heun = np.zeros(n)
y_rk3 = np.zeros(n)
y_rk4 = np.zeros(n)
y_exact = np.zeros(n)

# Встановлення початкових умов
y_euler[0] = y_heun[0] = y_rk3[0] = y_rk4[0] = y0
y_exact[0] = exact_solution(x0)

# Обчислення
for i in range(n - 1):
    x_i = x_values[i]

    # 1. Метод Ейлера
    y_euler[i + 1] = y_euler[i] + h * f(x_i, y_euler[i])

    # 2. Метод Хойна (Рунге-Кутта 2-го порядку / Модифікований Ейлер)
    k1_h = f(x_i, y_heun[i])
    k2_h = f(x_i + h, y_heun[i] + h * k1_h)
    y_heun[i + 1] = y_heun[i] + (h / 2) * (k1_h + k2_h)

    # 3. Метод Рунге-Кутта 3-го порядку
    k1_3 = f(x_i, y_rk3[i])
    k2_3 = f(x_i + h / 2, y_rk3[i] + (h / 2) * k1_3)
    k3_3 = f(x_i + h, y_rk3[i] - h * k1_3 + 2 * h * k2_3)
    y_rk3[i + 1] = y_rk3[i] + (h / 6) * (k1_3 + 4 * k2_3 + k3_3)

    # 4. Метод Рунге-Кутта 4-го порядку
    k1_4 = f(x_i, y_rk4[i])
    k2_4 = f(x_i + h / 2, y_rk4[i] + (h / 2) * k1_4)
    k3_4 = f(x_i + h / 2, y_rk4[i] + (h / 2) * k2_4)
    k4_4 = f(x_i + h, y_rk4[i] + h * k3_4)
    y_rk4[i + 1] = y_rk4[i] + (h / 6) * (k1_4 + 2 * k2_4 + 2 * k3_4 + k4_4)

    # Точний розв'язок
    y_exact[i + 1] = exact_solution(x_values[i + 1])


print(f"{'x':<5}  {'Ейлер':<10}  {'Хойн':<10}  {'РК-3':<10}  {'РК-4':<10}  {'Точний (y*)':<10}")
for i in range(n):
    print(
        f"{x_values[i]:<5.1f}  {y_euler[i]:<10.6f}  {y_heun[i]:<10.6f}  {y_rk3[i]:<10.6f}  {y_rk4[i]:<10.6f}  {y_exact[i]:<10.6f}")