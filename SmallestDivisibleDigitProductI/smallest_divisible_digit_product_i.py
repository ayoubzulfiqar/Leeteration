import sys

def digit_product(num):
    s_num = str(num)
    product = 1
    for digit_char in s_num:
        digit = int(digit_char)
        if digit == 0:
            return 0
        product *= digit
    return product

def solve():
    n = int(sys.stdin.readline())
    t = int(sys.stdin.readline())

    current_num = n
    while True:
        prod = digit_product(current_num)
        if prod % t == 0:
            sys.stdout.write(str(current_num) + '\n')
            return
        current_num += 1

solve()