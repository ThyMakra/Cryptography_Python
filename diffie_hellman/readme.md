# Diffie-Hellman
## Limitations
The strength of Diffie-Hellman relies solely on the size of its prime number and primitive roots and has raised 2 main limitations in this program :
1. Uses an already generated prime and primitive root pair. This limitation is due to the difficulty in generating new prime numbers and the probability that it could not find the prime number. Not to mention, to find the primitive root of the prime raises even more time complexity. 
Even though the pair does not have to be renewed every communication, their size limits have raised the second limitation.
2. The size of the generated prime number is only 512 bits which guarantee 256 bits of security. This is due to the primality check of this program slows down when it reaches 1024 to a few second to no longer work when reaching 2048 bits. The prime number's size has to be dropped down even more to 512 bits when finding for its primitive root due to its probability and time complexity
> Futher reading: \
> Primitive root searching need to find a more efficient generator(k): \
> https://cp-algorithms.com/algebra/primitive-root.html \
> Prime Factorization: finding factors of (prime - 1) to find the generator then find the primitive root.

## Cloning the project
1. In the github repository, you can download the zip files of the whole repository in "Clone or download".
2. Or using git command and clone the project:
    > $ git init \
    > $ git clone https://github.com/ThyMakra/Cryptography_Python.git

After cloning the repository, to execute the Diffie-Hellman key exchange, run the python file:\
diffie_hellman/diffie_hellman.py

## After Thoughts
During the writing of the program, I have divided in to 3 main steps:
1. How to generate big prime numbers (~up to 1024 bits)
2. How to raise a number to a big exponent (power_mod.py ~ 10^6 bits exponent)
3. How to check for the primitive root of the prime number (The most difficult part)

These 3 parts have been divided into its individual sub-folder which its own markdown. (Take a look at each folder to see the explanation of each topic).

__Comment:__
The the research took me 4 days of only reading about this topic which really took a lot of my time from doing anything else. Though the sense of accomplishment from being able to play with really big numbers is indescribable that I wouldn't regret any one bit spending all this time. \
You really feel more powerful the bigger the number you can work with, especially when you can raised a number to about a million bits exponent in a few seconds.\
I have took a liking to Diffie-Hellman since the first time I have heard about it during class. Watching computerphile videos really gave me a push in to loving its math and Crypto Exchange answers explaining these Number theory is the most helpful and really makes you fall in love with the algorithms that enabling you to compute numbers in a really fast way.\

Overall, This may have took a long time to finish but it opens up another door for me to look more into Number Thoery and its algorithm. I feel like I would be able to write a better program in competitive programming by learning all of these algorithm. The goal is to read more books about thoeries like these.

Adios!