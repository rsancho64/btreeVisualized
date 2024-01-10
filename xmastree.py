import btree_oo
import random


def rg():
    # random in range 1-100
    return random.randint(1, 100)


if __name__ == "__main__":

    xt = btree_oo.Bt()

    n = 5
    # n = input("cuantas bolas? ")
    # print(f"{n} ...")

    for i in range(int(n)+1):
        xt.insert(rg())
        print(xt)

    xt.visu()
