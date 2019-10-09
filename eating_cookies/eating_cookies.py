#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
# def eating_cookies(n, cache=None):

counter = 0


def eating_cookies(n):
    global counter
    if n == 0:
        return counter

    four_ways = [1, 2, 3]
    # N = number of cookies
    # 3 ways to subtract a cookie
    # Each time we subtract a cookie (meaning he ate the cookie(s)), we increase the counter += 1
    if n > 0:
        print("before n", n)
        for i in four_ways:
            n = n - i
            print("i", i)
            counter += 1
            print(counter)
            print("n", n)
            return eating_cookies(n)

    return counter


print(eating_cookies(3))

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_cookies = int(sys.argv[1])
#     print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
#   else:
#     print('Usage: eating_cookies.py [num_cookies]')
