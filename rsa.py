import math # for random values

# must output p q e d 

# checks if prime
def prime_check(number):
    prime_check = 0
    for i in range(2, number):
        if number % i == 0:
            prime_check += 1
    if prime_check != 0:
        return False
    else: 
        return True
    
# get closest prime number by recursively calling 
def make_prime(number):
    if prime_check(number):
        return number
    else: 
        number = number + 1
        make_prime(number)
    
def image_classification(m):

    pass

# sources: 
# https://www.reubenbinns.com/blog/self-sufficient-programming-rsa-cryptosystem-with-plain-python/

