#!python

import sys

class Dejumbletron(object):
    def __init__(self):
        self.dict = self.sorted_dict()

    def sorted_dict(self):
        sortedic = {}
        with open('/usr/share/dict/words', 'r') as f:
            for i in f:
                i = i.strip().lower()
                sort = ''.join(sorted(i))
                sortedic[sort] = i
        return sortedic

    def dejumbletron(self, words):
        for word in words:
            word = word.strip().lower()
            sort_word = ''.join(sorted(word))
            if sort_word in self.dict:
                print(self.dict[sort_word])
            else:
                print('Impossible, perhaps The Archives are incomplete!')

if __name__ == "__main__":
    words = sys.argv[1:]
    jumble = Dejumbletron()
    jumble.dejumbletron(words)