#! /usr/bin/env python
__author__ = 'Mohamed'


def is_palindrome(num):
    return num == reverse_num(num)


def reverse_num(num):
    r = 0
    while num > 0:
        r = r * 10 + num % 10
        num /= 10
    return r


def main():
    start_range = 100
    end_range = 1000
    max_palindrome = 0
    for i in range(start_range, end_range):
        for j in range(i, end_range):
            product = i * j
            if is_palindrome(product):
                max_palindrome = max(max_palindrome, product)
    print max_palindrome


if __name__ == "__main__":
    main()