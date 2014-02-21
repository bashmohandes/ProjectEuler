__author__ = 'mohamed.elsherif'
from utils import fact


def c(n, r):
    n_fact = fact(n)
    r_fact = fact(r)
    nr_fact = fact(n - r)
    return n_fact / (r_fact * nr_fact)


def main():
    count = 0
    for n in range(1, 101):
        for r in range(1, n):
            if c(n, r) >= 1000000:
                count += 1
    print count


if __name__ == "__main__":
    main()