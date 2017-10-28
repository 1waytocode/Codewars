Growth of a Population
https://www.codewars.com/kata/563b662a59afc2b5120000c6

def nb_year(p0, percent, aug, p):
    n = 0
    result = 0
    percent = float(percent/100)
    while result < p:
        result = p0 + (p0 * percent) + aug
        p0 = result
        n += 1
    return n
