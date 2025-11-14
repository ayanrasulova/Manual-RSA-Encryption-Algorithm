from math import gcd
import random

# must output p q e d 

# we get two random numbers for p and q using the random library 
def random_number():
    global random1
    global random2
    random1 = random.randint(1, 10**100)
    random2 = random.randint(1, 10**100)

# checks if these random numbers are prime, helper function for make_prime
def prime_check(number):
    prime_check = 0
    for i in range(2, number): # if no remainder, then its not prime
        if number % i == 0:
            prime_check += 1
    if prime_check != 0: # no remainder
        return False
    else: # remainders, must be prime
        return True
    
# get closest prime number by recursively calling 
def make_prime(number):
    if prime_check(number): # if number is prime, just return number
        return number
    else: # otherwise, keep adding 1, recursively call to get actual prime number
        number = number + 1
        make_prime(number)

# needed for key generation, checks for "positive integers less than or equal to n that are relatively prime to n"
def euler_totient_function (number):
    result = 1
    for i in range(2, number):
        if gcd(i, number) == 1:
            result += 1 # counts for each coprime
    return result

# get encryption exponent e 

    
def image_classification(m):

    # get p and q values 
    prime_check(random1)
    p = make_prime(random1)
    prime_check(random2)
    q = make_prime(random2)

    # multiply together
    n = p*q

    # get n value 


    pass

# sources: 
# https://www.reubenbinns.com/blog/self-sufficient-programming-rsa-cryptosystem-with-plain-python/
# https://www.geeksforgeeks.org/computer-networks/rsa-algorithm-cryptography/

