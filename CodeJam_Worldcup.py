#! /usr/bin/env python

from AutoMeasure import AutoMeasure

__author__ = 'Mohamed.Elsherif'


@AutoMeasure
def main():
    problems = parse_file("B-small-practice.in")
    write_output_file(solve(problems))


def solve(problems):
    result = []
    for problem in problems:
        result.append(problem.solve())
    return result


def parse_file(file_name):
    result = []
    with open(file_name, 'r') as input:
        T = int(input.readline().rstrip('\n'))
        for i in range(T):
            p = int(input.readline().rstrip('\n'))
            m = [int(s) for s in input.readline().rstrip('\n').split(' ')]
            tickets = {}
            for l in range(p):
                tickets[l] = [ int(price) for price in input.readline().rstrip('\n').split(' ')]
            result.append(Problem(p, m, tickets))
    return result

def write_output_file(result):
    with open("worldcup.out", "w") as output:
        for i in range(len(result)):
            output.write(format("Case #%d: %d\n" % (i + 1, result[i])))

class Problem:
    def __init__(self, p, m, tickets):
        self._M = m
        self._tickets = tickets
        self._p = p
        self._teams = 1 << p
        self._team_matches = self._get_team_matches()

    @property
    def M(self):
        return self._M

    @property
    def Tickets(self):
        return self._tickets

    @property
    def P(self):
        return self._p

    def solve(self):
        cost = 0
        for l in range(self.P):
            must = self._get_min_and_decrease()
            must_matches = set()
            for m in must:
                must_matches.add(self._team_matches[m][l])
            for m in must_matches:
                cost += self._tickets[l][m]
        return cost

    def _get_team_matches(self):
        result = []
        for t in range(self._teams):
            matches = []
            for l in range(self._p):
                matches.append(t / (1 << (l + 1)))
            result.append(matches)
        return result

    def __repr__(self):
        return format("P=%d, M=%s, tickets=%s, matches=%s" % (self.P, self.M, self.Tickets, self._team_matches))

    def _get_min_and_decrease(self):
        result = []
        for i in range(len(self.M)):
            if self.M[i] == 0:
                result.append(i)
            if self.M[i] > 0:
                self.M[i] -= 1
        return result


if __name__ == "__main__":
    main()
