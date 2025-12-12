import math


def f(x):
    # Уравнение из задания 1: x*sin(x) - 1 = 0
    return x * math.sin(x) - 1


def bisection_with_Nh(a, b, h):
    # Проверяем, что корень есть на отрезке
    if f(a) * f(b) >= 0:
        print("Ошибка: функция должна иметь разные знаки на концах отрезка.")
        return None, 0

    # Теоретическое количество итераций N(h)
    N = math.ceil(math.log((b - a) / h) / math.log(2))
    print(f"Теоретическое количество итераций N(h) = {N}")

    # Цикл с параметром (ровно N итераций)
    for _ in range(N):
        c = (a + b) / 2
        if f(c) == 0:
            return c, N
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    root = (a + b) / 2
    return root, N


def main():
    print("Решение уравнения x*sin(x) - 1 = 0 методом половинного деления")
    print("Известный интервал для наименьшего положительного корня: [1.0, 1.5]")

    # Ввод данных
    a = float(input("Введите левую границу a (например, 1.0): "))
    b = float(input("Введите правую границу b (например, 1.5): "))
    h = float(input("Введите точность h (например, 0.0001 для 10^-4): "))

    root, N = bisection_with_Nh(a, b, h)

    if root is not None:
        print(f"\nПриближенный корень: {root:.10f}")
        print(f"Количество итераций (расчетное): {N}")
        print(f"Значение функции в корне: f(root) = {f(root):.10f}")


if __name__ == "__main__":
    main()