import matplotlib.pyplot as plt

def calculate_f(func_str, x_val):
    return eval(func_str, {"x": x_val})


#для пошуку початкового проміжку
def dsk_method(func_str, x0, h=0.1):


    f_center = calculate_f(func_str, x0)
    f_right = calculate_f(func_str, x0 + h)
    f_left = calculate_f(func_str, x0 - h)

    # Визначаємо напрямок убування функції
    if f_left >= f_center >= f_right:
        delta = h
        print(f"Функція спадає вправо. Крок: {delta}")
        x_prev = x0
        xk = x0 + h
        fk = f_right
    elif f_left <= f_center <= f_right:
        delta = -h
        print(f"Функція спадає вліво. Крок: {delta}")
        x_prev = x0
        xk = x0 - h
        fk = f_left
    elif f_left >= f_center <= f_right:
        print("Мінімум знайдено одразу навколо початкової точки.")
        return min(x0 - h, x0 + h), max(x0 - h, x0 + h)
    else:
        print("Помилка: Функція опукла або крок h занадто великий.")
        return None, None

    k = 1
    while True:
        # Збільшуємо крок удвічі на кожній ітерації: 2^k * delta
        step = (2 ** k) * delta
        x_next = xk + step
        f_next = calculate_f(func_str, x_next)

        print(f"Ітерація {k}: x = {x_next:.4f}, f(x) = {f_next:.4f}")

        # Якщо функція почала зростати ми перескочили мінімум — проміжок знайдено
        if f_next >= fk:
            a = min(x_prev, x_next)
            b = max(x_prev, x_next)
            print(f"Знайдено проміжок: [{a:.4f}, {b:.4f}]")
            return a, b

        x_prev = xk
        xk = x_next
        fk = f_next
        k += 1


def dichotomy_method(func_str, a, b, eps):

    delta = eps / 2.0
    step = 1

    # Зберігаємо історію зміни відрізка для побудови графіка
    history = [(a, b)]

    while (b - a) / 2.0 > eps:
        mid = (a + b) / 2.0
        x1 = mid - delta
        x2 = mid + delta

        f1 = calculate_f(func_str, x1)
        f2 = calculate_f(func_str, x2)

        print(f"Крок {step:2d} [a, b] = [{a:.5f}, {b:.5f}], Довжина = {b - a:.5f}")

        if f1 < f2:
            b = x2
        else:
            a = x1

        history.append((a, b))
        step += 1

    print(f"Крок {step:2d} [a, b] = [{a:.5f}, {b:.5f}], Довжина = {b - a:.5f}")

    x_min = (a + b) / 2.0
    f_min = calculate_f(func_str, x_min)
    return x_min, f_min, history



def visualize_process(func_str, history, x_opt, f_opt):
    # Визначаємо межі графіка на основі першого (найширшого) знайденого відрізка
    a_init, b_init = history[0]
    margin = (b_init - a_init) * 0.3  # Додаємо трохи місця по краях
    x_start = a_init - margin
    x_end = b_init + margin

    # Генеруємо точки для побудови кривої функції
    num_points = 200
    step = (x_end - x_start) / num_points
    x_vals = [x_start + i * step for i in range(num_points + 1)]
    y_vals = [calculate_f(func_str, x) for x in x_vals]

    # Створюємо вікно з двома графіками (функція зверху, звуження відрізків знизу)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), gridspec_kw={'height_ratios': [2, 1]})

    # --- Верхній графік: Сама функція ---
    ax1.plot(x_vals, y_vals, label=f"f(x) = {func_str}", color="blue", linewidth=2)
    ax1.scatter([x_opt], [f_opt], color="red", zorder=5, label=f"Мінімум (x*={x_opt:.4f})")
    ax1.axvline(x=x_opt, color='red', linestyle='--', alpha=0.4)
    ax1.set_title("Графічна інтерпретація пошуку мінімуму", fontsize=14)
    ax1.set_ylabel("f(x)")
    ax1.grid(True, linestyle="--", alpha=0.7)
    ax1.legend()

    # --- Нижній графік: Процес дихотомії (звуження проміжку) ---
    for i, (a, b) in enumerate(history):
        # Малюємо горизонтальні відрізки для кожної ітерації
        ax2.plot([a, b], [-i, -i], marker='|', color="green", linewidth=2.5, markersize=8)

    ax2.axvline(x=x_opt, color='red', linestyle='--', alpha=0.4)
    ax2.set_title("Процес звуження відрізка [a, b] методом дихотомії", fontsize=12)
    ax2.set_xlabel("x")
    ax2.set_ylabel("Крок (ітерація)")

    # Налаштовуємо підписи осі Y для відображення номерів кроків
    ax2.set_yticks([-i for i in range(len(history))])
    ax2.set_yticklabels([f"Крок {i}" for i in range(len(history))])
    ax2.grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.show()




print("Введіть функцію (використовуйте 'x', наприклад: (x-2)**2 + 3):")
func_input = input("f(x) = ")

try:
    x0_input = float(input("Введіть початкове значення для методу ДСК (x0): "))
    eps_input = float(input("Введіть точність (eps > 0): "))

    # 1. Шукаємо проміжок
    a, b = dsk_method(func_input, x0_input)

    if a is not None and b is not None:
        # 2. Шукаємо мінімум та збираємо історію кроків
        x_opt, f_opt, history = dichotomy_method(func_input, a, b, eps_input)

        print(f"Точка мінімуму: x* = {x_opt:.6f}")
        print(f"Мінімум функції: f(x*) = {f_opt:.6f}")

        # 3. Викликаємо графічну візуалізацію
        visualize_process(func_input, history, x_opt, f_opt)

except Exception as e:
    print(f"Сталася помилка (перевірте правильність введення функції): {e}")