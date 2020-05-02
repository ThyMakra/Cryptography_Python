## Large Prime density
π(n) is the number ofprime numbers ≤ n
> π(10) = 4. [2, 3, 5, 7]
## Prime number theorem 
n/ln(n) is a good approximation of π(n) \
When n tends to infinity, π(n) / (n/ln(n)) = 1 \

That means the probability that a randomly chosen number is prime is = 1/ln(n). \
Because there are n positive integers ≤ n and approximately n/ln(n) primes, so (n/ln(n)) / n = 1/ln(n)
> Example:  the probability to find a prime number of 1024 bits is 1 / (ln(2¹⁰²⁴)) = (1 / 710)

Primes are odd (except 2), we can increase this probability by 2, so in average, to generate a 1024 bits prime number, we have to test 355 numbers randomly generated.

## Testing the number is prime
* Test sqrt(n), because if n = p*q (composite), p ≤ sqrt(n) or q ≤ sqrt(n).
> In the case where p = q, we have n = p*p with p = sqrt(n). In the other case, where p != q, either p > sqrt(n) and q < sqrt(n), or q > sqrt(n) and p < sqrt(n).
* We only have to test with 2 and all the odd numbers to sqrt(n) . 
> Because 2 divides all even numbers, so if 2 doesn’t divide n, the others even numbers will not.

# Probablisitc algorithm
## Fermat's Little theorem
* Given a prime number = n. a = integer that ( 1 ≤ a ≤ n-1 )
* Therefore : a^(n-1) = 1 (mod n).
> Proof : https://primes.utm.edu/notes/proofs/FermatsLittleTheorem.html
> Congruence - Number theory https://mathworld.wolfram.com/Congruence.html

So for an integer n, we just need to find a value __a__ for which __a^(n-1)__ != 1(mod n) to prove that n is composite (Fermat witness).

In the other hand, if we find a value of __a__ that verify the Fermat's theorem, we just show that n satisfies Fermat's theorem fot the base a, and appears to be prime. In this case, we said that n is pseudo-prime of base a.

## Carmichael numbers
Carmichael numbers are numbers that satisfies the Fermat’s little theorem for all possible values of __a__.
> The first 3 = 561, 1105, 1729
> Only 255 CN < 10⁸, and 20138200 < 10²¹ 
So if you generate a random number n < 10⁸, the probability that n is a CN is 2.55*10^(-6)
> It's very low. But the Fermat primality test is not perfect because of these numbers. Miller-Rabin is more advanced than Fermat's primality test, and CN are not a problem.

## Trivial and nontrivial square-root 
We define p > 2, a prime \
We know that 1 and -1 always give 1 when squared: 1² = (-1)² = 1 (mod p). They are called trivial square root. 
But sometimes, there are nontrivial square root of 1 modulo p. we define a, an integer, to be a nontrivial squaer root of 1 (mod p) if __a² = 1 (mod p)__
> For example: 3² = 9 = 1 (mod 8). So 3 is a non trivial square root of 1 modulo 8.
> Congruent: 13 === 1 (mod 12). x === 1 (mod N) does not work with negative number but (x - 1) === 0 (mod N) does.

If 1 has a square root other than 1 and -1 modulo n (a nontrivial square root), then n must be composite.
> Explanation: 5² = 25 divide 8 with remainder 1 then that means, a number other than 1 (mod 8) is congruent to 1 which means 5² -1 divides 8 so 8 is composite.

## Miller-Rabin 
Find a nontrivial square roots of 1 modulo n. \
Fermat's Little theorem: a^(n-1) = 1 (mod n) 

### This Last part is not understood yet??
For Miller-Rabin, we need to find r and s such that __(n-1) = r*(2^s)__, with r odd.\
Then we pick an integer in the range [1, n-1].
* If a^r != 1 (mod n) and a^((2^j)r) != -1 (mod n) \
for all j such that 0 ≤ j ≤ s-1,\ 
then n is not prime and a is called a strong witness to compositeness for n
* If a^r = 1 (mod n) or a^((2^j)r) = -1 (mod n) \
for some j such as 0 ≤ j ≤ s-1, then n is said to be a strong pseudo-prime to the base a, and a is called a strong liar to primality for n

# Algorithm to Generate big prime numbers
* Generate a prime candidate. Say we want a 1024 bits prime number. \
Start by generating 1024 bits randomly. \
Set the MSB to 1, to make sure that the number hold on 1024 bits. \
Set the LSB to 1 to make be sure that it’s an odd number
* Test if the generated number is prime with Miller-Rabin. Run the test many time to make it more efficient.
* If the number is not prime, restart from the beginning

> MSB is a bit of the highest digit, LSB is the lowest digit in binary


> https://medium.com/p/49e6e6af32fb/responses/show
### Response
* Found an error in the definition of Carmichael numbers. “There are some composite numbers that satisfies the Fermat’s little theorem for all possible values of a”. This is not correct, this “a” must be coprime to “n” (following your notation). Actually if you try to calculate all powers for the first Carmichael number 561 you will see that the exponentiation is not equal to 1 unless gcd(a,n)=1.