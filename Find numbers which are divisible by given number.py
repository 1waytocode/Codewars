Find numbers which are divisible by given number
https://www.codewars.com/kata/55edaba99da3a9c84000003b

def divisible_by(numbers, divisor):
    x = []
    for i in numbers:
        if i%divisor==0:
            x.append(i)
    return x
