# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
from random import randint


def gen(N):
    for i in range(N):
        yield randint(1, 100)


# написать генераторное выражение, которое делает то же самое

oneline_gen = lambda N: (randint(1, 100) for i in range(N))

if __name__ == '__main__':
    for num in gen(5):
        print(num)
    print()
    for num in oneline_gen(5):
        print(num)
