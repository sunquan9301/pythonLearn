def add(*args):
    total = int(0)
    for val in args:
        total += val
    return int(total)


def swap(a, b):
    return (a, b) if a > b else (b, a)


if __name__ == '__main__':
    print(add(3, 4.2, 6.5))
    print('package is %s; file is %s' % (__package__, __file__))

    print(swap(3, 4))
