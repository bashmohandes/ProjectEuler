#! /usr/bin/env python
from AutoMeasure import AutoMeasure

__author__ = 'Mohamed.Elsherif'


@AutoMeasure
def main():
    g = T9Generator("C-large-practice.in", "output.out")
    g.solve()


class T9Generator:

    KeyMap = {' ':'0',
              'a':'2', 'b':'22', 'c':'222',
              'd':'3', 'e':'33', 'f':'333',
              'g':'4', 'h':'44', 'i':'444',
              'j':'5', 'k':'55', 'l':'555',
              'm':'6', 'n':'66', 'o':'666',
              'p':'7', 'q':'77', 'r':'777', 's':'7777',
              't':'8', 'u':'88', 'v':'888',
              'w':'9', 'x':'99', 'y':'999', 'z':'9999'}

    def __init__(self, input_file_name, output_file_name):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name

    def _get_keys(self, word):
        prev_key = None
        result = []
        for c in word:
            r = self.KeyMap[c]
            if prev_key and r[0] == prev_key[0]:
                result.append(' ')
            result.append(r)
            prev_key = r
        return ''.join(result)


    def solve(self):
        with open(self.input_file_name, 'r') as input_file:
            with open(self.output_file_name, 'w') as output_file:
                n = int(input_file.readline())
                for i in range(n):
                    word = input_file.readline().rstrip('\n')
                    output_file.write(format("Case #%d: %s\n" % (i + 1, self._get_keys(word))))


if __name__ == "__main__":
    main()