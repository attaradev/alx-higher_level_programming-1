#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as cals

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, cals.add(a, b)))
    print("{} - {} = {}".format(a, b, cals.sub(a, b)))
    print("{} * {} = {}".format(a, b, cals.mul(a, b)))
    print("{} / {} = {}".format(a, b, cals.div(a, b)))
