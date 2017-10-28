Persistent Bugger
https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

def persistence(n):
    n = str(n)
    x = 1
    count = 0
    if len(n) == 1:
        return (0)
    else:
        while len(n) != 1:
            count += 1
            for i in n:
                x *= int(i)
            n = str(x)
            x = 1
    return count
