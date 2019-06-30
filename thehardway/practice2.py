
#练习运算符,继续进行打印

def main():
    print("I will now count my chickens")
    print("Hens", 25+30/6,20)
    print("Roosters", 100-25*3%4)
    print(3+2<5-7)
    x = "I am a boy, I am %d year old" % 10
    print(x)

    print("."*10)
    print('''I 'd like "said" I am boy''')


    format = "%r %r %r %r"
    print(format % (1,2,3,4))
    print(format % ("a","b",3,'d'))


if __name__ == "__main__":
    main()