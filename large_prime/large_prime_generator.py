from random import randrange, getrandbits

def is_prime(n, k=128):
    """ Test if a number is prime
        Args: 
            int n = the number to test
            int k = the number of tests to do 
            return True if n is prime
    """
    #Test if n is not even. But care, 2 is prime
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r & s
    """ I don't really understand this part """
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

def generate_prime_candidate(length):
    """ Generate an odd integer randomly 
        Args: 
            int length the length of the number to generate, in bits

        return an integer
    """

    # generate random bits
    p = getrandbits(length)
    # apply a mast to set MSB and LSB to 1
    """ Is this binary operator or something? """
    p |= (1 << length - 1) | 1
    return p

def generate_prime_number(length=1024):
    """ Generate a prime 
        Args: 
            int length = length of the prime to generate, in bits

        return a prime
    """
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p

# will generate prime with 127 ~ 128 digits
""" prime = generate_prime_number(420)
print(len(str(prime)))
print(prime) """

p = generate_prime_number(1024)
print(p)


