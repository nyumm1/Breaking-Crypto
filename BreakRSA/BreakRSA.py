import builtins
from math import isqrt


def is_perfect_square(n: int) -> bool:
    """Check if a number is a perfect square"""
    x = isqrt(n)
    return x * x == n


def integer_sqrt(n: int) -> int:
    """Compute the integer square root using Newton's method"""
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def fermat_factor(n: int) -> tuple[int, int]:
    """
    Perform Fermat's factorization on n.
    Assumes n is a product of two close prime numbers... hopefully
    """
    a = integer_sqrt(n) + 1
    b2 = a * a - n

    while not is_perfect_square(b2):
        a += 1
        b2 = a * a - n

    b = integer_sqrt(b2)
    return a + b, a - b


def modinv(a: int, m: int) -> int:
    """
    Compute the modular inverse of a modulo m using the Extended Euclidean Algorithm
    """
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def decrypt_rsa_integer(c: int, d: int, n: int) -> bytes:
    """
    Decrypt an RSA-encrypted integer
    Returns the plaintext as bytes
    """
    m = builtins.pow(c, d, n)
    return m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')


def main():
    # RSA Modulus (replace with actual 2048-bit value)
    n = 0  # TODO: Replace with RSA modulus value

    if is_perfect_square(n):
        print("n is a perfect square, Fermat's method may not be applicable.")
        return

    # Step 1: Factor n
    p, q = fermat_factor(n)
    print("p:", p)
    print("q:", q)
    print("n check:", p * q == n)

    # Step 2: Compute totient
    tot = (p - 1) * (q - 1)
    print("ϕ(n):", tot)

    # Step 3: Compute private exponent d
    e = 65537
    d = modinv(e, tot)
    print("d:", d)

    # Step 4: Decrypt ciphertext
    c = 0  # TODO: Replace with actual ciphertext
    plaintext_bytes = decrypt_rsa_integer(c, d, n)

    try:
        print("Decrypted message:", plaintext_bytes.decode())
    except UnicodeDecodeError:
        print("Decrypted raw bytes:", plaintext_bytes)


if __name__ == "__main__":
    main()
