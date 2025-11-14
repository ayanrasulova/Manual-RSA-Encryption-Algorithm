from math import gcd
import random

# must output p q e d 

# we get two random numbers for p and q using the random library 
def random_number():
    global random1
    global random2
    random1 = random.randint(10000, 50000)
    random2 = random.randint(10000, 50000)

# checks if these random numbers are prime, helper function for make_prime
def prime_check(number):
    prime_check = 0

    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1): # if no remainder, then its not prime
        if number % i == 0:
            return False
    return True
    
# get closest prime number by recursively calling 
def make_prime(number):
    if prime_check(number): # if number is prime, just return number
        return number
    else: # otherwise, keep adding 1, recursively call to get actual prime number
        return make_prime(number+1)

# get encryption exponent e, d, also n
def getting_keys():
    # making global so i can print
    global e, n, d, p, q

    # get p and q values
    p = make_prime(random1)
    q = make_prime(random2)

    # multiply together for n 
    n = p*q

    # e must 1 < e < Φ(n) AND gcd(e, Φ(n)) = 1 
    etf = (p - 1) * (q - 1) # Φ(n)
    e = 0
    d = 0 

    e = random.randrange(2, etf) # firts condition.. in the range 
    while gcd(e, etf) != 1:
        e = random.randrange(2,etf) # keep recalling it randomly

    # to get d, (d * e) ≡ 1 mod Φ(n)
    for i in range(1, etf):
        if (i * e) % etf == 1:
            d = i
            break

    return n, e, d
    # public key = (n, e), private key = (n, d)
     
# the message is encrypted using the public key, which is (n, e)
def encrypt(message, e, n): 
    encrypted_list = [] 

    for i in message:
        msg_char = ord(i) # need to convert from string to unicode in order to use in equation
        C = (pow(msg_char, e, n)) # then with each char, can get C value
        encrypted_list.append(C) # then add to the encrypted list!

    return encrypted_list

# the message is decrypted using the private key, which is (n, d)
def decrypt(cipher, d, n): 
    message = ""

    for i in cipher:
        message += chr(pow(i, d, n))
    return message

def main():
    M = input("Enter message: ") # input!

    random_number()
    getting_keys()

    encrypted = encrypt(M, e, n)
    decrypted = decrypt(encrypted, d, n) 

    print("p:", p)
    print("q:", q)
    print("e:", e)
    print("d:", d)
    
    print("Ciphertext:", encrypted)
    print("Decrypted message:", decrypted)

main()

# sources: 
# https://www.reubenbinns.com/blog/self-sufficient-programming-rsa-cryptosystem-with-plain-python/
# https://www.geeksforgeeks.org/computer-networks/rsa-algorithm-cryptography/

