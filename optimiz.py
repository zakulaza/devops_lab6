import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


def dsk_method(f, x0, h=0.1):

    f0 = f(x0)
    f_plus = f(x0 + h)
    f_minus = f(x0 - h)

    if f_minus >= f0 and f0 >= f_plus:
        delta = h
        a = x0
        x1 = x0 + h
        f1 = f_plus
    elif f_minus <= f0 and f0 <= f_plus:
        delta = -h
        x1 = x0 - h
        f1 = f_minus
        a = x1
    else:

        return min(x0 - h, x0 + h), max(x0 - h, x0 + h)

    x_prev = x0
    k = 1

    while True:
        x_next = x1 + (2 ** k) * delta
        f_next = f(x_next)

        if f_next >= f1:
            break

        x_prev = x1
        x1 = x_next
        f1 = f_next
        k += 1

    return min(x_prev, x_next), max(x_prev, x_next)


def fibonacci_method(f, a, b, eps):
    F = [1, 1]
    while (b - a) / F[-1] > eps:
        F.append(F[-1] + F[-2])
    n = len(F) - 1

    history = [(a, b)]

    x1 = a + (F[n - 2] / F[n]) * (b - a)
    x2 = a + (F[n - 1] / F[n]) * (b - a)
    f1 = f(x1)
    f2 = f(x2)

    for k in range(1, n - 1):
        if f1 <= f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (F[n - k - 2] / F[n - k]) * (b - a)
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (F[n - k - 1] / F[n - k]) * (b - a)
            f2 = f(x2)
        history.append((a, b))

    x_min = (a + b) / 2
    return x_min, f(x_min), history




func_str = input("Введіть функцію f(x) (наприклад, x**2 - 4*x + 4): ")
func_str = func_str.replace('^', '**')

x0_str = input("Введіть початкову точку x0 для методу ДСК: ")
eps_str = input("Введіть точність eps (наприклад, 0.001): ")

x0 = float(x0_str)
eps = float(eps_str)

x_sym = sp.Symbol('x')
sympy_expr = sp.sympify(func_str)
f = sp.lambdify(x_sym, sympy_expr, 'numpy')

a, b = dsk_method(f, x0, h=0.1)
print(f"Знайдений інтервал: [{a:.4f}, {b:.4f}]")

x_min, f_min, history = fibonacci_method(f, a, b, eps)
print(f"Точка мінімуму: x* = {x_min:.6f}")
print(f"Значення функції: f(x*) = {f_min:.6f}")
print(f"Кількість ітерацій: {len(history)}")

# Створюємо масив X для побудови графіка (трохи ширше за знайдений інтервал [a, b])
margin = (b - a) * 0.5
X = np.linspace(a - margin, b + margin, 400)
Y = f(X)

plt.figure(figsize=(10, 6))
plt.plot(X, Y, label=f"f(x) = {func_str}", color='blue')

# Відображаємо початковий інтервал ДСК
plt.axvline(a, color='gray', linestyle='--', label=f'ДСК інтервал [{a:.2f}, {b:.2f}]')
plt.axvline(b, color='gray', linestyle='--')

# Відображаємо звуження інтервалів (малюємо горизонтальні лінії для кожної ітерації)
y_offset = min(Y) + (max(Y) - min(Y)) * 0.1  # Відступ знизу для ліній
step = (max(Y) - min(Y)) * 0.05

for i, (int_a, int_b) in enumerate(history):
    plt.hlines(y=y_offset + i * step, xmin=int_a, xmax=int_b, colors='orange',
               alpha=0.7, linewidth=2)

# Ставимо точку мінімуму
plt.scatter([x_min], [f_min], color='red', zorder=5, label=f'Мінімум ({x_min:.3f}, {f_min:.3f})')

plt.title("Пошук мінімуму методом Фібоначчі")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
