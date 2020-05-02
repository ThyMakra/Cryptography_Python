from large_prime.large_prime_generator import generate_prime_candidate, is_prime, generate_prime_number
from random import randrange, getrandbits
""" length = 1024
prime_q = generate_prime_number(length)

# is_p_prime = True
for _ in range(1024):
    random_r = generate_prime_candidate(length)
    prime_p = prime_q*random_r + 1
    is_p_prime = is_prime(prime_p, 128)
    if is_p_prime:
        print(f'q = {prime_q}')
        print(f'r = {random_r}')
        print(f'p = {prime_p}')
        break
print(is_p_prime) """


""" Find a prime : k. Find a random r that k * r + 1 = p and p is prime """
length = 1024
prime_k = generate_prime_number(length)

# is_p_prime = True
for _ in range(10 ** 5):
    random_length = randrange(2, length - 1)
    # random_r = generate_prime_candidate(random_length)
    random_r = getrandbits(random_length)
    
    prime_p = prime_k*random_r + 1
    is_p_prime = is_prime(prime_p, 128)
    if is_p_prime:
        print(f'k = {prime_k}')
        print(f'r = {random_r}')
        print(f'p = {prime_p}')
        break
print(is_p_prime)

k = 110147360880977326145454323208221071089784097565692230883406944964885283866809403126305248705095738645969886839883972829698185023465616223853188508575646895119112813982949306635369092626464429143567242208129503631864031757968830572178817452781169212310750061873270404450233561253396099991206848635615097818383
p = 43082051866405784268948008360239663371476383135695473540552891195307856350251150004363160861540864492690236763621355192274027092576551112340323465734825985622409182429611461053257718176197766147966093597607140010120892130855358598001143531843921797726275980046817650188458876441923529364987308191285520342628934557842563964004452802050717206851017049458919
