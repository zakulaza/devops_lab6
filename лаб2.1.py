import math


def f(x, y):
    return y + math.exp(x) / x


def y_exact(x):
    return math.exp(x) * math.log(abs(x)) + math.exp(x - 1)


x0 = 1.0
y0 = 1.0
h = 0.1
N = 10

# Списки для збереження результатів (початкове значення y0 всюди однакове)
x_vals = [x0 + n * h for n in range(N + 1)]
y_euler = [y0] * (N + 1)
y_heun = [y0] * (N + 1)
y_rk3 = [y0] * (N + 1)
y_rk4 = [y0] * (N + 1)

for n in range(N):
    xn = x_vals[n]

    # Метод Ейлера I-го порядку
    # y_{n+1} = y_n + h * f(x_n, y_n)
    y_euler[n + 1] = y_euler[n] + h * f(xn, y_euler[n])

    # Метод Хойна II-го порядку
    # k1 = h * f(x_n, y_n)
    # k2 = h * f(x_n + h, y_n + k1)
    k1_h = h * f(xn, y_heun[n])
    k2_h = h * f(xn + h, y_heun[n] + k1_h)
    y_heun[n + 1] = y_heun[n] + (k1_h + k2_h) / 2

    # Метод Рунге-Кутта III-го порядку
    # k1 = h * f(x_n, y_n)
    # k2 = h * f(x_n + h/2, y_n + k1/2)
    # k3 = h * f(x_n + h, y_n - k1 + 2*k2)
    k1_3 = h * f(xn, y_rk3[n])
    k2_3 = h * f(xn + h / 2, y_rk3[n] + k1_3 / 2)
    k3_3 = h * f(xn + h, y_rk3[n] - k1_3 + 2 * k2_3)
    y_rk3[n + 1] = y_rk3[n] + (k1_3 + 4 * k2_3 + k3_3) / 6

    # Метод Рунге-Кутта IV-го порядку
    # k1 = h * f(x_n, y_n)
    # k2 = h * f(x_n + h/2, y_n + k1/2)
    # k3 = h * f(x_n + h/2, y_n + k2/2)
    # k4 = h * f(x_n + h, y_n + k3)
    k1_4 = h * f(xn, y_rk4[n])
    k2_4 = h * f(xn + h / 2, y_rk4[n] + k1_4 / 2)
    k3_4 = h * f(xn + h / 2, y_rk4[n] + k2_4 / 2)
    k4_4 = h * f(xn + h, y_rk4[n] + k3_4)
    y_rk4[n + 1] = y_rk4[n] + (k1_4 + 2 * k2_4 + 2 * k3_4 + k4_4) / 6

print(f"{'x':>5} | {'Точний':>10} | {'Ейлер':>10} | {'Хойн':>10} | {'РК-3':>10} | {'РК-4':>10}")
print("-" * 70)

for i in range(N + 1):
    exact = y_exact(x_vals[i])
    print(
        f"{x_vals[i]:5.1f} | {exact:10.5f} | {y_euler[i]:10.5f} | {y_heun[i]:10.5f} | {y_rk3[i]:10.5f} | {y_rk4[i]:10.5f}")