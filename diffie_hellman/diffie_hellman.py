from prime_root_pair import generated_pair
from modular_exponentiation.power_mod import power_mod

from random import choice, getrandbits, randrange

print('#'*80)
print(f'Diffie-Hellman Key exchange!')
print('My only weakness is Man-In-The middle attack where the hacker masqurade as both parties and owns both the parties\' secret keys.')
print(f'Please enter your name: ')
# user_name = input()
# print(f'Name recorded. Establishing connection between user {user_name} and user Meak!!')
global_pair = choice(generated_pair)
prime = global_pair['prime']
primitive_root = choice(global_pair['primitive_root'])
print(f'Both parties agree on: ....')

print(f'Prime(n): {prime}')

print(f'Primitive root(g): {primitive_root}')

print('Note: The following information is a sensitive information only known to the 2 parties:')
key_len = randrange(128, 1024)
a = getrandbits(key_len)
b = getrandbits(key_len)

print('Both parties have generated their own secret key a and b.')
print(f'a: {a}')

print(f'b: {b}')

sent_key = power_mod(primitive_root, a, prime)
print(f'The generated g^a mod n: \n{sent_key}')
print('You send the generated key to the other user.')

recieved_key = power_mod(primitive_root, b, prime)
print(f'You received the generated key from Meak.\nThe generated g^b mod n: \n{recieved_key}')

session_key_1 = power_mod(sent_key, b, prime)
session_key_2 = power_mod(recieved_key, a, prime)
print(f'The session key on your side is {session_key_1}')

print(f'The session key on the party is {session_key_2}')

print(f'Program checked: {session_key_1 == session_key_2}')
print('The key exchange has been done!')

