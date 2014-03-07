__author__ = "Mohamed Elsherif"
from AutoMeasure import AutoMeasure
from utils import gcd, lcm, lcm_list
import itertools



def f(G, L, N):
    count = 0
    possible_numbers = [i for i in range(G, L + 1)]
    for p in itertools.permutations(possible_numbers, N):
        if gcd(p) >= G and lcm_list(p) <= L:
            count += 1
    return count


@AutoMeasure
def main():
    print f(10, 100, 1)
    print f(10, 100, 2)
    print f(10, 100, 4) #% 101**4)


if __name__ == "__main__":
    main()