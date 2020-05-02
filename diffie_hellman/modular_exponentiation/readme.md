# Modular Exponentiation
(a^b) % c = ?
where b is large
> Example: 2^35236 can not be calculate

## Multiplication Property 
(a*b)%c = ((a%c)(b%c)) % c \
a^b = a^(b/2).a^(b/2) \
(a^b)%c = ((a^(b/2) % c)()a^(b/2) % c) % c \
a^b = a^(b-1).a
a^b % c = ((a %c)(a^(b-1) % c)) % c

## Program - modular_exponentia.py
* In the program, it will likely to cause recursion depth limit exceeded due to too big of the exponent, other factors are the base of the exponent or the modulo will not affect the program.
    * It can handle to up to 2.. decimal digits and for the decimal numbers generated from 1024 bits are around 308~309 digits.

## Program - power_mod 
For this algorithm, it relies on the power of modular with the help of binary. 
> See explanation in the reference.

In this program, it uses loop rather than recursion which solve the above limitation. Still, the number of loops depends on the number of binary digits of the exponent and since Python start slowing down when reaching 10^6 loops, the same applies to the maximum number of binary-digits for the input exponent thus, exponent limit = 10^6 binary digits ~ 3*10^5 decimal 
> Reference: https://www.nku.edu/~christensen/1002mat584%20modular%20exponentiation.pdf 

* Code
```python
""" (base^k) mod p """
def power_mod(base, k, p):
    k_bin = bin(k)[2:-1][::-1] # remove prefix, last bit and reversed binary
    total = base % p
    expand = total
    for bi_di in k_bin: # ignore first digit
        expand = (expand ** 2) % p
        if bi_di == "1":
            total = (total * expand) % p
    return total

```
* Futher improvement
    * complexity of this algorithm relies solely on the number of the binary digits of the exponent. If there is a way to shortcut that, the complexity will decrease.
    * The way it checks digits ( == "1"). "total" and "expand" variables are almost the same





