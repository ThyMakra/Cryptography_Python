""" from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii



keyPair = RSA.generate(3072)

public_key = keyPair.publicKey()
print(f'Public key: (n={hex(public_key.n)}, e = {hex(public_key.e)})')
public_keyPEM = public_key.exportKey()
print(f'Public Key PEM decode: {public_keyPEM.decode("ascii")}')

print(f'Private key: n={hex(public_key.n)}, d={hex(keyPair.d)}')
privateKeyPEM = keyPair.exportKey()
print(privateKeyPEM.decode("ascii"))
 """

""" generate RSA 1024-bits keys and print them 
as hex numbers, PKCS#8 PEM ASN.1  """

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(3072)

pubKey = keyPair.publickey()
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))

""" encrypt the message using RSA-OAEP encryption scheme 
(RSA with PKCS#1 OAEP padding) with the RSA public key: """
msg = b'A message for encryption'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
print("Encrypted:", binascii.hexlify(encrypted))

""" decrypt the message using using RSA-OAEP 
with the RSA private key """
decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted)