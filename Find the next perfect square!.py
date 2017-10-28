Find the next perfect square!
https://www.codewars.com/kata/56269eb78ad2e4ced1000013

from math import sqrt
def find_next_square(sq):
    q = sqrt(sq)
    square = 1
    if q % 1 == 0 and q < sq:
        q += 1
        square = int(q**2)
    elif q == 0:
        return 0
    else:
        return -1
    return square
