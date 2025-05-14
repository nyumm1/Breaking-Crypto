This project demonstrates how RSA encryption can be broken when the prime factors of the modulus n are too close together.

How it works:

RSA security relies on the difficulty of factoring a large number n = p × q, where p and q are large prime numbers. If these primes are close in value, Fermat's Factorization Method can be used to efficiently recover them.

Steps involved:

Fermat’s Factorization:
We attempt to factor the modulus n using Fermat’s method, which is fast when p and q are close. It looks for integers a and b such that:

n = a² - b² ⇒ (a + b)(a - b)

Recover the Private Key:
Once we find p and q, we compute the totient:

ϕ(n) = (p - 1)(q - 1)

and then calculate the private key d as the modular inverse of the public exponent e modulo ϕ(n).

Decrypt the Ciphertext:
With d and n, we decrypt the ciphertext c using modular exponentiation:

m = c^d mod n

Why this is insecure:
If p and q are too close, n becomes vulnerable to Fermat’s attack. This violates a core requirement of RSA security: the primes must be sufficiently far apart to prevent easy factorization!

This project is intended solely for educational and ethical purposes.
