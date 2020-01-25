def cache_decorator(calculator):
    # Реализовать декоратор который кэширует результаты вызова функции (есть в лекции)
    # Применить для функции calculator (в calculator.py уже есть import функции cache_decorator)
    # Настоятельно прошу написать декоратор руками, а не копировать, т.к. важно запомнить как это работает
    cache = {}

    def calculator_wrapper(*args):
        if args not in cache:
            print('not in cache')
            cache[args] = calculator(*args)

        return cache[args]

    return calculator_wrapper
