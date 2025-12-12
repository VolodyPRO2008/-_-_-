print("Метод Гаусса - решение системы")
n = int(input("Кол-во уравнений: "))

# Ввод матрицы
M = []
for i in range(n):
    row = list(map(float, input(f"Строка {i + 1}: ").split()))
    M.append(row)

# Решение
for i in range(n):
    # Нормализуем строку i
    div = M[i][i]
    for j in range(i, n + 1):
        M[i][j] /= div

    # Вычитаем из других строк
    for k in range(n):
        if k != i:
            factor = M[k][i]
            for j in range(i, n + 1):
                M[k][j] -= factor * M[i][j]

# Вывод результата
print("\nРешение:")
for i in range(n):
    print(f"x{i + 1} = {M[i][n]:.4f}")