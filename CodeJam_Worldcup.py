#! /usr/bin/env python

from AutoMeasure import AutoMeasure
import sys

__author__ = 'Mohamed.Elsherif'


@AutoMeasure
def main():
    problems = parse_file("B-large-practice.in")
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
                tickets[l] = [ Ticket(int(price)) for price in input.readline().rstrip('\n').split(' ')]
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

    def solve(self):
        cost = 0
        for round in range(self._p):
            must_teams = self._get_min_and_decrease()
            for team in must_teams:
                if self._is_covered(team, round):
                    continue
                ticket = self._get_cheapest_ticket(team, round)
                if ticket:
                    cost += ticket.price
                    ticket.mark_purchased()
        return cost

    def _is_covered(self, team, round):
        return self._tickets[round][self._team_matches[team][round]].purchased

    def _get_cheapest_ticket(self, team, round):
        min_price = sys.maxint
        cheapest_ticket = None
        for r in range(round + 1):
            ticket = self._tickets[r][self._team_matches[team][r]]
            if not ticket.purchased and ticket.price < min_price:
                min_price = ticket.price
                cheapest_ticket = ticket
        return cheapest_ticket

    def _get_team_matches(self):
        result = []
        for t in range(self._teams):
            matches = []
            for l in range(self._p):
                matches.append(t / (1 << (l + 1)))
            result.append(matches)
        return result

    def _get_min_and_decrease(self):
        result = []
        for i in range(len(self._M)):
            if self._M[i] == 0:
                result.append(i)
            if self._M[i] > 0:
                self._M[i] -= 1
        return result


class Ticket:
    def __init__(self, price):
        self._price = price
        self._purchased = False

    @property
    def price(self):
        return self._price

    @property
    def purchased(self):
        return self._purchased

    def mark_purchased(self):
        self._purchased = True

if __name__ == "__main__":
    main()
