from functools import reduce


def run():
    my_list = [i for i in range(1, 11)]
    odd = list(filter(lambda x: x % 2 != 0, my_list))
    square = list(map(lambda x: pow(x, 2), my_list))
    square = list(reduce(lambda a, b: a * b, my_list))
    print(square)


if __name__ == '__main__':
    run()
