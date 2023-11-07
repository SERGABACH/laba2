def fibonacci(n):
    """
    Функция для определения n чисел Фибоначчи.
    Принимает n - количество чисел, которые нужно определить.
    Возвращает список чисел Фибоначчи.
    """
    if n <= 0:
        raise ValueError("n должно быть положительным числом.")

    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b

    return fib_list


def bubble_sort(arr):
    """
    Функция для сортировки списка чисел методом пузырька.
    Принимает arr - список чисел для сортировки.
    Возвращает отсортированную копию списка.
    """
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]

    return sorted_arr


def calculator(num1, num2, operation):
    """
    Функция-калькулятор для выполнения арифметических операций над двумя числами.
    Принимает num1 - первое число, num2 - второе число, operation - знак действия (+, -, *, /).
    Возвращает результат операции.
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("num1 и num2 должны быть числами.")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ZeroDivisionError("Деление на ноль недопустимо.")
        result = num1 / num2
    else:
        raise ValueError("Недопустимая операция.")

    return result
