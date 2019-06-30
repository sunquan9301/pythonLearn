def main():
    # age = input("How old are you?")
    # print("I am %s year old" % age)
    file = open("demo1")
    lines = file.readlines()
    print("lines",lines)

    for i in range(len(lines)):
        print(lines[i])
    file.close()

    c,d = addOne(1,2)
    print(c,d)


def addOne(a,b):
    return a+1, b+1

if __name__ == '__main__':
    main()
