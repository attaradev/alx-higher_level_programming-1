#!/usr/bin/python3

if __name__ == "__main__":
    """A program that prints the addition of all arguments"""
    import sys

    ans = 0
    for i in range(len(sys.argv) - 1):
        ans += int(sys.argv[i + 1])
    print("{}".format(ans))
