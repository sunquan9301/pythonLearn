import itertools


def main():
    permutations = itertools.permutations('ABCD')
    itertools.combinations('ABCDE', 3)
    itertools.product('ABCD', '123')


if __name__ == "__main__":
    main()
