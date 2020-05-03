from random import getrandbits, randrange
""" 
length = 1024

k = 110147360880977326145454323208221071089784097565692230883406944964885283866809403126305248705095738645969886839883972829698185023465616223853188508575646895119112813982949306635369092626464429143567242208129503631864031757968830572178817452781169212310750061873270404450233561253396099991206848635615097818383
p = 43082051866405784268948008360239663371476383135695473540552891195307856350251150004363160861540864492690236763621355192274027092576551112340323465734825985622409182429611461053257718176197766147966093597607140010120892130855358598001143531843921797726275980046817650188458876441923529364987308191285520342628934557842563964004452802050717206851017049458919

random_length = randrange(2, length - 1)
# random_r = generate_prime_candidate(random_length)
random_g = getrandbits(random_length)

pow_1 = random_g % p
pow_2 = (random_g ** 2) % p
pow_k = (random_g ** k) % p

print(pow_1, pow_2, pow_k) 

print(5 ** 2 % 23)

print(5 ** 23 % 23)

"""

# from diffie_hellman import power_mod
# from large_prime.large_prime_generator import generate_prime_number, is_prime


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
    p |= (1 << length - 1) | 1 # p = p | ((1 << length - 1) | 1)
    """ perform OR with p and a number 
    that number is created by 
    left shift 1 by (length - 1) 0's. Then it will perform OR with 1 it will get something like : 10000....001 """
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




def get_prime_pair(length):
    find_pair = True
    while find_pair:
        k = generate_prime_number(length)
        p = 2*k + 1
        print(0)
        if is_prime(p):
            find_pair = False
            return p, k
""" 
prime, generator = get_prime_pair(512)
print(f'prime: {prime},\n Generator:  {generator}')
 """


""" 
Test 128: 
prime: 662590704546746579177520582797363203019,
Generator:  331295352273373289588760291398681601509

Test 512:
prime: 25342186783511241806771184827200829501926346464468403412193165448792919674256241637744277471612635721250820070404552212076222711645377007845780993667472959
Generator:  12671093391755620903385592413600414750963173232234201706096582724396459837128120818872138735806317860625410035202276106038111355822688503922890496833736479

Test 512
prime: 22278935310900897950969221810035027399242802508698875371631264428385367068721489540632395578045195793568786687563216368180596753200193027258015890961143067
Generator:  11139467655450448975484610905017513699621401254349437685815632214192683534360744770316197789022597896784393343781608184090298376600096513629007945480571533

Test 512
prime: 24668418058127200912392399093246362133003037865320217743023517188692919250076973028530675047315079154723898183408402554743278294067223362905835459585950207
 Generator:  12334209029063600456196199546623181066501518932660108871511758594346459625038486514265337523657539577361949091704201277371639147033611681452917729792975103

Test 512
prime: 20726339147787459700534571833857808938086533223341350480377029904295271383581740915247302659997511694276104711427888150212637649728927118050209635390719587
 Generator:  10363169573893729850267285916928904469043266611670675240188514952147635691790870457623651329998755847138052355713944075106318824864463559025104817695359793
 """



def get_primitive_root(prime, generator):
    while True:
        bits_range = randrange(len(bin(generator)[2:]))
        primitive = getrandbits(bits_range)
        # minus 1 to check if any of the 3 results in 1
        mod_one = power_mod(primitive, 1, prime) - 1
        mod_two = power_mod(primitive, 2, prime) - 1
        mod_gen = power_mod(primitive, generator, prime) - 1
        if mod_one & mod_two & mod_gen: # False, if any is 0
            return primitive


prime = 20726339147787459700534571833857808938086533223341350480377029904295271383581740915247302659997511694276104711427888150212637649728927118050209635390719587
generator = 10363169573893729850267285916928904469043266611670675240188514952147635691790870457623651329998755847138052355713944075106318824864463559025104817695359793
primitive = get_primitive_root(prime, generator)
print(primitive)
root = [
    1517115413108769533573520934540341108,
    140012848153374422489010,
    5540477747737136559951823962244140304766742850817168658245984094946089153423794248722542958223402215140882540177609853474268457650256911501,
    2463366029890128908959506254292262148565409283943093684177083806291840474764567955144918339512359,
]



