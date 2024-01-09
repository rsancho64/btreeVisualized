def a():
    print("soy a")


def b():
    a()


def c():
    a()
    b()


if __name__ == "__main__":
    c()
