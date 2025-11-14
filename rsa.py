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

# get encryption exponent e, d, also n
def getting_keys():
    # making global so i can print
    global e
    global n
    global d
    global p
    global q

    # get p and q values
    prime_check(random1)
    p = make_prime(random1)
    prime_check(random2)
    q = make_prime(random2)

    # multiply together for n 
    n = p*q

    # e must 1 < e < Φ(n) AND gcd(e, Φ(n)) = 1 
    etf = (p - 1) * (q - 1) # Φ(n)
    e = 0

    for e in range(2, etf): # first condition
        if gcd(e, etf) == 1: # second condition
            e = e

    # to get d, (d * e) ≡ 1 mod Φ(n)
    d = (1 % etf)/e

    return n, e, d
    # public key = (n, e), private key = (n, d)
     
# the message is encrypted using the public key, which is (n, e)
def encrypt(message, e, n): 
    global C
    global encrypted_list

    characters = []
    encrypted_list = [] 

    for i in message:
        new = ord(message) # need to convert from string to unicode in order to use in equation
        characters.append(new)

    for msg_char in characters:
        C = (msg_char ** e) % n
        encrypted_list.append(C)

    return encrypted_list

# the message is decrypted using the private key, which is (n, d)
def decrypt(C, d, n): 
    message = (C ** d) % n
    return message

def main():
    message = input("Enter message")

    random_number()
    getting_keys()

    encrypted = encrypt(message, e, n)
    decrypted = decrypt(C, d, n)
    print(p)
    print(q)
    print(e)
    print(d)
    
    print("Ciphertext: {encrypted}")
    print("Decrypted message: {decrypted}")

main()

# sources: 
# https://www.reubenbinns.com/blog/self-sufficient-programming-rsa-cryptosystem-with-plain-python/
# https://www.geeksforgeeks.org/computer-networks/rsa-algorithm-cryptography/

