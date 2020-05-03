from prime_root_pair import generated_pair
from modular_exponentiation.power_mod import power_mod

from time import sleep
from random import choice, getrandbits, randrange

def prints(text, delay=0.4):
    for t in text.split(' '):
        print(t, end=' ', flush=True)
        sleep(delay)
    print()


prints('#### '*4)
prints(f'Diffie-Hellman Key exchange!')
print('My only weakness is Man-In-The middle attack where the hacker masqurade as both parties and owns both the parties\' secret keys.\n')
prints(f'Please enter your name:')
user_name = input()
prints(f'\nName recorded. Establishing connection between user {user_name} and user Meak!!')

keepGoing = True
while keepGoing:
    global_pair = choice(generated_pair)
    prime = global_pair['prime']
    primitive_root = choice(global_pair['primitive_root'])
    print(f'Both parties agree on:\n')

    prints(f'Prime (n): {prime}\n', 1)

    prints(f'Primitive root(g): {primitive_root}\n', 1)

    print(f"\n{'#'*44}\n")
    print('Note: The following information is a sensitive information only known to the 2 parties:')
    key_len = randrange(128, 1024)
    a = getrandbits(key_len)
    b = getrandbits(key_len)

    prints('Both parties have generated their own secret key a and b.\n')
    prints(f'a: {a}\n', 1)

    prints(f'b: {b} \n\n', 1)

    sent_key = power_mod(primitive_root, a, prime)
    prints(f'The generated g^a mod n: \n{sent_key}')
    prints('You send the generated key to the other user.\n')

    recieved_key = power_mod(primitive_root, b, prime)
    prints(f'You received the generated key from Meak.\nThe generated g^b mod n: \n{recieved_key}\n')

    session_key_1 = power_mod(sent_key, b, prime)
    session_key_2 = power_mod(recieved_key, a, prime)
    prints(f'The session key on your side is {session_key_1}')

    print(f'The session key on the party is {session_key_2}')

    prints(f'\nProgram checked: {session_key_1 == session_key_2}')
    prints('The key exchange has been done!\n\n')

    prints('Do you want to exchange again? [y/n]')
    option = input()
    print('\n')
    if option == 'n':
        keepGoing = False
