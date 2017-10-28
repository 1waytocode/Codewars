IQ Test
https://www.codewars.com/kata/552c028c030765286c00007d

def iq_test(numbers):
    i = 0
    countodd = 0
    counteven = 0
    new = numbers.split()
    for i in new:
        if int(i)%2==0:
            counteven += 1
            if counteven < 2:
                even = new.index(i)+1
        else:
            countodd += 1
            if countodd < 2:
                odd = new.index(i)+1
    if counteven > countodd:
        return odd
    else:
        return even
