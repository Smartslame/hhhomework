from core.decorators import cache_decorator


@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    if operation in ['+', '-', '/', '*', '**']:
        if operation == '+':
            return a + b
        if operation == '-':
            return a - b
        if operation == '/':
            if b == 0:
                raise ZeroDivisionError()
            return a / b
        if operation == '*':
            return a * b
        if operation == '**':
            return a ** b
    else:
        raise Exception('Unsupported operation')


def safe_input(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Необходимо ввести корректное число")


if __name__ == '__main__':
    # Тут было бы неплохо обрабатывать ошибку в случае передачи некорректных символов
    a = safe_input('Введите первое число: ')
    b = safe_input('Введите второе число: ')

    operation = input('Введите операцию: ')

    print('Результат: ', calculator(a, b, operation))
