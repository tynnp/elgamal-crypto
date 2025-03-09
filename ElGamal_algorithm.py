import random
import math
import os

# Kiểm tra số nguyên tố 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Sinh số nguyên tố trong khoảng [min_val, max_val]
def generate_prime(min_val, max_val):
    while True:
        p = random.randint(min_val, max_val)
        if is_prime(p):
            return p

# Lấy các ước nguyên tố của n
def prime_factors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2

    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.add(i)
            n //= i
        i += 2

    if n > 1:
        factors.add(n)
    return factors

# Tìm phần tử sinh alpha của Zp*
def find_primitive_root(p):
    phi = p - 1
    factors = prime_factors(phi)

    for alpha in range(2, p):
        check = True
        for q in factors:
            if pow(alpha, phi // q, p) == 1:
                check = False
                break
        if check:
            return alpha  
    return None  

# Sinh khóa ElGamal
def generate_keys(min_prime=10000, max_prime=70000):
    p = generate_prime(min_prime, max_prime)
    alpha = find_primitive_root(p)
    a = random.randint(1, p - 2)
    beta = pow(alpha, a, p)
    return p, alpha, beta, a

# Mã hóa: 
def encrypt(plaintext, p, alpha, beta):
    ciphertext = []
    for m in plaintext:
        k = random.randint(1, p - 2)
        gamma = pow(alpha, k, p)
        delta = (m * pow(beta, k, p)) % p
        ciphertext.append(gamma)
        ciphertext.append(delta)
    return ciphertext

# Giải mã:
def decrypt(ciphertext, p, a):
    plaintext = []
    for i in range(0, len(ciphertext), 2):
        gamma = ciphertext[i]
        delta = ciphertext[i + 1]
        s = pow(gamma, p - 1 - a, p)
        m = (delta * s) % p
        plaintext.append(m)
    return plaintext
