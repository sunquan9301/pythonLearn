from urllib import request, error, parse, robotparser, response

def main():
    c = request.urlopen('http://baidu.com/')
    contents = c.read()
    print(contents)


if (__name__ == "__main__"):
    main()

