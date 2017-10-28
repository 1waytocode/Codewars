Take a Ten Minute Walk
https://www.codewars.com/kata/54da539698b8a2ad76000228

def isValidWalk(walk):
    if len(walk) == 10 and walk[0] == walk[9]:
        return True
    else:
        return False
