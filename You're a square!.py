You're a square!
https://www.codewars.com/kata/54c27a33fb7da0db0100040e

def is_square(n):
    try:
        if n**(1/2) == int(n**(1/2)) and n>0:
            return True
        return False
    except:
        return False 
