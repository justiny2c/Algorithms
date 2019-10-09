#!/usr/bin/python

import argparse


def find_max_profit(prices):

    if len(prices) < 2:
      return print("It's only been 1 day")

    max = prices[1] # you can only sell if you've bought before, which is why index starts at [1]
    max_i = 0
    for i in range(2, len(prices)-1):
        if prices[i] > max:
            max = prices[i]
            max_i = i

    least = prices[0]
    for j in range(1, max_i):
        if prices[j] < least:
            least = prices[j]

    return max - least


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
