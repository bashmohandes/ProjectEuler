#! /usr/bin/env python
from AutoMeasure import AutoMeasure
from Problem_38 import is_pandigital

__author__ = 'Mohamed.Elsherif'

'''
x * y = product
for str(x) + str(y) + str(product) to be 9 digits

x is either 1 or 2 digits
y is either 3 to 5 digits
product is 4 digits
'''

@AutoMeasure
def main():
    products = set()
    for x in range(1, 100):
        for y in range(100, 10000):
            product = x * y
            if product in products:
                continue
            candidate = int(str(x) + str(y) + str(product))
            if candidate > 987654321:
                break
            if is_pandigital(candidate):
                print "%d => %d * %d = %d" % (candidate, x, y, product)
                products.add(product)
    print sum(products)


if __name__ == "__main__":
    main()

