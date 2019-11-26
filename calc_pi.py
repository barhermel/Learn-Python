#This program will find pi to the n'th digit using the Chudnovsky algotirhm

from decimal import *

def chudnovsky(n):
    '''
    This function gets n as the number of decimal digits to print
    and return the pi number up to the Nth decimal digit.
    :param n: number of decimal digits n > 0
    '''
    getcontext().prec = n + 1
    c = Decimal(426880 * (10005) ** 0.5)
    sigma = Decimal(calc_sigma(n))
    sol = Decimal(c / sigma)
    print(sol)

def calc_sigma(n):
    '''
    This function is calculating the denominator of the Chudnovsky algorithm
    :param n: the number of repetition
    :return: the denominator of the Chudnovsky algorithm
    '''
    sol = 0
    for i in range(n):
        numerator = calc_numerator(i)
        denominator = calc_denominator(i)
        sol += Decimal(numerator/ denominator)
    return sol


def calc_numerator(n):
    '''
    This function calculate the numerator of the sigma in Chudnovsky algorithm
    :param n: number of repetition of the sigma
    :return: the numerator of the sigma in Chudnovsky algorithm
    '''
    fac = factorial(6 * n)
    return fac * (545140134 * n + 13591409)

def calc_denominator(n):
    '''
    This function calculate the denominator of the sigma in Chudnovsky algorithm
    :param n: number of repetition of the sigma
    :return: the denominator of the sigma in Chudnovsky algorithm
    '''
    fac = factorial(3 * n) * ((factorial(n)) ** 3)
    pow = (-262537412640768000) ** n
    return fac * pow

def factorial(n):
    '''
    This function calculate the factorial of n
    n! = 1 * 2 * 3 * ... * (n-1) *n
    wheres 1! = 1 , 0! = 1
    :param the last number to multiply
    :return: n: n! = 1 * 2 * 3 * ... * (n-1) *n, 1! = 1 , 0! = 1
    '''
    sol =1
    if n == 1 or n == 0:
        return sol
    else:
        for i in range(2, n+1):
            sol *= i

    return sol

def main():
     n = int(input("Enter the number of decimal dgits of pi: "))
     while n <= 0:
         print("n needs to be a natural number (n > 0)")
         n = int(input("Please enter a natural number: "))
     chudnovsky(n)


if __name__ == '__main__':
    main()