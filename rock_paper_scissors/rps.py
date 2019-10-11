#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    rps = ["rock", "paper", "scissors"]
    rounds = []
    each_round = []

    if n == 0:
        return [[]]

    def round(each_round, n):
        if n == 0:
            return rounds.append(each_round)
        else:
            for play in rps:
                print(play)
                round(each_round + [play], n-1) # each_round + [rock] // each_round = [rock, paper]

    round(each_round, n)
    return rounds

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
