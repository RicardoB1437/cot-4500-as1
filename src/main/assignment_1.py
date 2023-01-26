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
    count: int = 0
    while int(temp%10) != 0:
        temp = temp/10
        count+=1
    ## next, add 5 to the k+1th digit and truncate
    temp += (Decimal(5) * Decimal(10**(-k-1)))
    print(truncate(temp, k))
    print()
    return truncate(temp, k)

def problem4(exact_num: Decimal, round_num: Decimal):
    ##absolute error = abs(exact - round)
    temp: Decimal = exact_num
    while int(temp%10) != 0:
        temp = temp/10

    abs_error: Decimal = abs(temp - round_num)
    abs_error = truncate(abs_error, 7)
    print(abs_error)
    
    ##relative error = abs error / exact
    rel_error: Decimal = abs_error / abs(temp)
    print(rel_error)
    print()

def problem5(x_val: float, exponent: float):
    # x_val / (n + 1)**3 < 10**exponent
    n: int = 10**float(abs(exponent)/3) - 1
    if float(n%1) != 0:
        n = int(n+1)
    print(n)
    print()

def func(x):
    return float((x**3) + (4*(x**2)) - 10)

def derivative(x):
    return float((3*(x**2)) + (8*x))

def bisection(start: int, end: int, accuracy: float):
    left: float = start
    right: float = end
    i: int = 0
    while abs(right - left) > accuracy:
        i += 1
        mid_x: float = (left + right) / 2
        if (func(left) < 0 and func(mid_x) > 0) or (func(left) > 0 and func(mid_x) < 0):
            right = mid_x
        else:
            left = mid_x
        #mid_y: float = func(mid_x)
    print(i)
    return i

def newton(initial_approx: float, accuracy: float):
    i: int = 1
    ## p1 = p0 - f(p0) / f'(p0)

    f_prev: float = initial_approx
    f_curr: float = 0
    while(i<=10000):
        if float(derivative(f_prev)) != 0:
            f_curr = f_prev - float(func(f_prev) / derivative(f_prev))
            if float(abs(f_curr - f_prev)) < accuracy:
                print(i)
                return i
            i += 1
            f_prev = f_curr
        else:
            print("zero derivative")
            return i
    print("max iter reached")
    print(i)
    return i


def problem6(start: int, end: int, accuracy: float, initial_approx: float):
    ##bisection method
    bisection(start, end, accuracy)
    print()

    ##newton method
    newton(initial_approx, accuracy)


if __name__ == "__main__":
    ans1 = problem1("010000000111111010111001")
    ans2 = problem2(ans1, 3)
    ans3 = problem3(ans1, 3)
    problem4(ans1, ans3)
    ans4 = problem5(1, -4)
    problem6(-4, 7, 10**(-4), 7)