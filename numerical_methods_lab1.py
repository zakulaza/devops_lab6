import math
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return math.log(x + 5) - x + 5

def df(x):
    return 1 / (x + 5) - 1


def newton_method(x0, eps):
    x_prev = x0
    steps = 0
    while True:
        fx_prev = f(x_prev)
        dfx_prev = df(x_prev)

        # Робимо крок
        x_curr = x_prev - fx_prev / dfx_prev
        steps += 1

        if x_curr <= -5:
            x_curr = -4.999999

        if abs(x_curr - x_prev) < eps:
            break
        x_prev = x_curr
    return x_curr, steps


def chord_method(x0, x1, eps):
    x_prev = x0
    x_curr = x1
    steps = 0
    while True:
        fx_prev = f(x_prev)
        fx_curr = f(x_curr)

        x_next = x_curr - fx_curr * (x_curr - x_prev) / (fx_curr - fx_prev)
        steps += 1

        if x_next <= -5:
            x_next = -4.999999

        if abs(x_next - x_curr) < eps:
            break
        x_prev = x_curr
        x_curr = x_next
    return x_next, steps



eps = 0.001

print("x1")
r1_n, iter1_n = newton_method(-4.9, eps)
print(f"Метод дотичних: x1 = {r1_n:.6f} (кроків: {iter1_n})")

r1_c, iter1_c = chord_method(-4.9, -4.99, eps)
print(f"Метод хорд:     x1 = {r1_c:.6f} (кроків: {iter1_c})\n")


print("x2")
r2_n, iter2_n = newton_method(8.0, eps)
print(f"Метод дотичних: x2 = {r2_n:.6f} (кроків: {iter2_n})")

r2_c, iter2_c = chord_method(7.0, 8.0, eps)
print(f"Метод хорд:     x2 = {r2_c:.6f} (кроків: {iter2_c})\n")






x_plot = np.linspace(-4.99, 10, 500)
y1_plot = np.log(x_plot + 5)
y2_plot = x_plot - 5

plt.figure(figsize=(10, 6))
plt.grid(True, linestyle='--', alpha=0.7)

plt.plot(x_plot, y1_plot, label='y = ln(x + 5)', color='blue', linewidth=2)
plt.plot(x_plot, y2_plot, label='y = x - 5', color='red', linewidth=2)
plt.axvline(x=-5, color='gray', linestyle=':', label='Асимптота x = -5')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Ставимо точки для ОБОХ коренів (для простоти беремо результати дотичних)
plt.scatter(r1_n, r1_n - 5, color='darkgreen', marker='X', s=100, zorder=5, label=f'Корінь 1 (x ≈ {r1_n:.5f})')
plt.scatter(r2_n, r2_n - 5, color='orange', marker='X', s=100, zorder=5, label=f'Корінь 2 (x ≈ {r2_n:.5f})')

plt.title(f"Графічний метод: ln(x + 5) = x - 5\nТочність eps = {eps}", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.legend(fontsize=10)
plt.xlim(-6, 10)
plt.ylim(-10, 5)

plt.show()