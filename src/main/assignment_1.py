from decimal import *
import math

def truncate(number: Decimal, digits: Decimal) -> Decimal:
    # Improve accuracy with floating point operations, to avoid truncate(16.4, 2) = 16.39 or truncate(-1.13, 2) = -1.12
    nbDecimals = len(str(number).split('.')[1]) 
    if nbDecimals <= digits:
        return number
    stepper = Decimal(10.0) ** digits
    return math.trunc(stepper * number) / stepper

def problem1(starting_num: str):
    s: Decimal = Decimal(starting_num[0])
    c: Decimal = 0
    f: Decimal = 0

    ## loop to find c
    for i in range(1, 12):
        exp: Decimal = 11-i
        digit: Decimal = Decimal(starting_num[i])
        c += digit * (Decimal(2)**(exp))
    ## loop to find f
    for i in range(12, len(starting_num)):
        exp: Decimal = i-11
        digit: Decimal = Decimal(starting_num[i])
        f += (digit / 2) ** exp
    
    ## -1^s * 2^c-1023 * 1+f
    answer: Decimal = Decimal(-1) ** s
    answer = answer * (Decimal(2) ** (c-Decimal(1023)))
    answer = answer * (Decimal(1) + f)

    print(f'{answer:.4f}', end='\n\n')
    return answer

def problem2(num: Decimal, k: Decimal):
    ## take the answer from problem 1 and apply 3 digit chopping
    ## first loop to normalize
    temp: Decimal = num
    while int(temp%10) != 0:
        temp = temp/10
    print(truncate(temp, k))
    print()
    return temp
    

def problem3(num: Decimal, k: Decimal):
    ## take the answer from problem 1 and apply 3 digit rounding
    ## first, loop to normalize
    temp: Decimal = num
    while int(temp%10) != 0:
        temp = temp/10
    ## next, add 5 to the k+1th digit and truncate
    temp += (Decimal(5) * Decimal(10**(-k-1)))
    print(truncate(temp, k))
    return temp

if __name__ == "__main__":
    ans1 = problem1("010000000111111010111001")
    ans2 = problem2(ans1, 3)
    ans3 = problem3(ans1, 3)
    #problem4()
    #problem5()
    #problem6()