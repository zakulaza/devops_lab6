import math


# Визначення функцій системи: y' = f(x, y, z) та z' = g(x, y, z)
def f(x, y, z):
    return 8 * z - y


def g(x, y, z):
    return y + z


def y_exact(x):
    return 2 * math.exp(3 * x) + 4 * math.exp(-3 * x)


def z_exact(x):
    return math.exp(3 * x) - math.exp(-3 * x)


x0, y0, z0 = 0.0, 6.0, 0.0
h = 0.05
N = 10

x_vals = [x0 + i * h for i in range(N + 1)]

res_euler = [(y0, z0)] * (N + 1)
res_heun = [(y0, z0)] * (N + 1)
res_rk3 = [(y0, z0)] * (N + 1)
res_rk4 = [(y0, z0)] * (N + 1)

for n in range(N):
    xn = x_vals[n]

    # МЕТОД ЕЙЛЕРА
    yn, zn = res_euler[n]
    res_euler[n + 1] = (yn + h * f(xn, yn, zn),
                        zn + h * g(xn, yn, zn))

    # МЕТОД ХОЙНА
    yn, zn = res_heun[n]
    k1 = h * f(xn, yn, zn)
    l1 = h * g(xn, yn, zn)
    k2 = h * f(xn + h, yn + k1, zn + l1)
    l2 = h * g(xn + h, yn + k1, zn + l1)
    res_heun[n + 1] = (yn + (k1 + k2) / 2,
                       zn + (l1 + l2) / 2)

    # МЕТОД РУНГЕ-КУТТА (III порядок)
    yn, zn = res_rk3[n]
    k1 = h * f(xn, yn, zn)
    l1 = h * g(xn, yn, zn)

    k2 = h * f(xn + h / 2, yn + k1 / 2, zn + l1 / 2)
    l2 = h * g(xn + h / 2, yn + k1 / 2, zn + l1 / 2)

    k3 = h * f(xn + h, yn - k1 + 2 * k2, zn - l1 + 2 * l2)
    l3 = h * g(xn + h, yn - k1 + 2 * k2, zn - l1 + 2 * l2)

    res_rk3[n + 1] = (yn + (k1 + 4 * k2 + k3) / 6,
                      zn + (l1 + 4 * l2 + l3) / 6)

    # МЕТОД РУНГЕ-КУТТА (IV порядок)
    yn, zn = res_rk4[n]
    k1 = h * f(xn, yn, zn)
    l1 = h * g(xn, yn, zn)

    k2 = h * f(xn + h / 2, yn + k1 / 2, zn + l1 / 2)
    l2 = h * g(xn + h / 2, yn + k1 / 2, zn + l1 / 2)

    k3 = h * f(xn + h / 2, yn + k2 / 2, zn + l2 / 2)
    l3 = h * g(xn + h / 2, yn + k2 / 2, zn + l2 / 2)

    k4 = h * f(xn + h, yn + k3, zn + l3)
    l4 = h * g(xn + h, yn + k3, zn + l3)

    res_rk4[n + 1] = (yn + (k1 + 2 * k2 + 2 * k3 + k4) / 6,
                      zn + (l1 + 2 * l2 + 2 * l3 + l4) / 6)

print(f"{'x':>4} | {'Точний y':>12} | {'Ейлер':>10} | {'Хойн':>10} | {'РК-4':>10}")
print("-" * 60)
for i in range(N + 1):
    print(
        f"{x_vals[i]:4.1f} | {y_exact(x_vals[i]):12.6f} | {res_euler[i][0]:10.5f} | {res_heun[i][0]:10.5f} | {res_rk4[i][0]:10.5f}")

print("Таблиця значень y(x):")
print(f"{'x':>4} | {'Точний y':>12} | {'Ейлер y':>12} | {'Хойн y':>12} | {'РК-3 y':>12} | {'РК-4 y':>12}")
print("-" * 75)
for i in range(N + 1):
    ex_y = y_exact(x_vals[i])
    print(
        f"{x_vals[i]:4.1f} | {ex_y:12.6f} | {res_euler[i][0]:12.6f} | {res_heun[i][0]:12.6f} | {res_rk3[i][0]:12.6f} | {res_rk4[i][0]:12.6f}")

print("\n" + "=" * 75 + "\n")

print("Таблиця значень z(x):")
print(f"{'x':>4} | {'Точний z':>12} | {'Ейлер z':>12} | {'Хойн z':>12} | {'РК-3 z':>12} | {'РК-4 z':>12}")
print("-" * 75)
for i in range(N + 1):
    ex_z = z_exact(x_vals[i])
    print(
        f"{x_vals[i]:4.1f} | {ex_z:12.6f} | {res_euler[i][1]:12.6f} | {res_heun[i][1]:12.6f} | {res_rk3[i][1]:12.6f} | {res_rk4[i][1]:12.6f}")

print("\n" + "=" * 75 + "\n")
print("Похибки для y(x):")
print(f"{'x':>4} | {'Пх Ейлер':>12} | {'Пх Хойн':>12} | {'Пх РК-3':>12} | {'Пх РК-4':>12}")
print("-" * 65)
for i in range(N + 1):
    ex_y = y_exact(x_vals[i])
    err_euler = abs(ex_y - res_euler[i][0])
    err_heun = abs(ex_y - res_heun[i][0])
    err_rk3 = abs(ex_y - res_rk3[i][0])
    err_rk4 = abs(ex_y - res_rk4[i][0])
    print(f"{x_vals[i]:4.1f} | {err_euler:12.6f} | {err_heun:12.6f} | {err_rk3:12.6f} | {err_rk4:12.6f}")

print("\nПохибки для z(x):")
print(f"{'x':>4} | {'Пх Ейлер':>12} | {'Пх Хойн':>12} | {'Пх РК-3':>12} | {'Пх РК-4':>12}")
print("-" * 65)
for i in range(N + 1):
    ex_z = z_exact(x_vals[i])
    err_euler = abs(ex_z - res_euler[i][1])
    err_heun = abs(ex_z - res_heun[i][1])
    err_rk3 = abs(ex_z - res_rk3[i][1])
    err_rk4 = abs(ex_z - res_rk4[i][1])
    print(f"{x_vals[i]:4.1f} | {err_euler:12.6f} | {err_heun:12.6f} | {err_rk3:12.6f} | {err_rk4:12.6f}")