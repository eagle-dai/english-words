import os
from os.path import dirname, abspath
import pandas as pd
import itertools


class Globals:
    words = set()


g = Globals()


def _get_root():
    root = dirname(abspath(__file__))
    if root.endswith('src'):
        root = dirname(root)
    return root


def _get_data_dir():
    return os.path.join(_get_root(), 'data')


def _read_words():
    csv = os.path.join(_get_data_dir(), 'CET4+6_edited.txt')
    df = pd.read_csv(csv, header=None, names=['word'], comment='#')

    global g
    for _, raw in df.iterrows():
        g.words.add(raw['word'])
    # print(g.words)


def _anagram(word: str):
    results = []

    p = list(itertools.permutations(word, len(word)))
    for l in p:
        new_word = ''.join(l)
        if new_word in g.words and new_word != word and new_word not in results:
            results.append(new_word)

    return results


def main():
    _read_words()
    print(_anagram('thicken'))


if __name__ == "__main__":
    main()
