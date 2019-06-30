import sys


def main():
    a = "hello world"
    # print(len(a))
    # print(a.center(
    #     50, '*'
    # ))
    #
    # print(a.ljust(50, '*'))
    # print(a.rjust(50, '='))

    list1 = ['hello'] * 5
    # print(list1)

    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # 循环遍历列表元素
    # for fruit in fruits:
    # title()就是说所有单词都是以大写开始，其余字母均为小写
    # print(fruit.title(), end=' ')

    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1, reverse=True)
    # sorted 不会改变list1, 会返回一个新的list
    # list1.sort()会直接在list1的基础上进行排序
    # print(list1)
    # print(list2)

    f = [x ** 2 for x in range(1, 1000)]
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数

    f = (x ** 2 for x in range(1, 1000))
    print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


if __name__ == '__main__':
    for val in fib(20):
        print(val)
