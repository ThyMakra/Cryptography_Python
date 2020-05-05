## Pycryptodome
Generate random RSA key-pair. Encrypt a short message and decrypt it back using PSA-OAEP padding scheme.
* package of low-level cryptographic primitives (hashs, MAC codes, key-derivation, digital signatures, symmetric, and asymmetric ciphers)
    ```
    pip install pycryptodome
    ```
__Link__: https://cryptobook.nakov.com/asymmetric-key-ciphers/rsa-encrypt-decrypt-examples

Import / Key-pair
> Generate RSA 1024-bits keys and print them as hex numbers, PKCS#8 PEM ASN.1
```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(3072)
```

Public Key
```python
pubKey = keyPair.publickey()
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
```
```
(
    n=0xa9eb161553916df2af993c4bf909e5e69c4a9ca7bcecfa5aa7f964721995a0c389ba5e598ae26ab5d8d6ac7227051d173a89787e9f1b062511103e2dae2d2b461c5553b344f08f086480d495af8e8a73ef8a3451b36add839cacf0a155addff3ef58ad884f184ec06ee3d7c803df2ba2778f82fa4f9cc204e7dde2952d14115c2e89c5a7300d3819c05f2e1c4c12985dda7725815143bc7564a77743f782da13869b72ed56fe912c7c10a5d5d67921fca050a134814636d7b7776b7e34c5ede6a3c7f0a4255f954870b2323fd45d9a24eaf07ef95c5d5deae1a6c817cd02df4af0d0d54b6e9e3f596bdd37ca1c0ee2d35e824f86df40e9efc09b8b07c872afae799f279a5f6e4244afaec0e653199e757fc46e6b5aedae8ee5287e457dad1c8584cd71081ed9f0650365e50c3c1036078efac979ef0cb7306b7d7662de35e7b210c043a294a0617c41003763020a86a82e84da46d79f43df09e24923867f0c1e6621e536c8e8853ae30b6502e4b9b1c77583eb1d51715b74c8a1d70b661f4d1f, 
    e=0x10001
)
```


Begin Public key
```python
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))
```
```
-----BEGIN PUBLIC KEY-----
MIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEAqesWFVORbfKvmTxL+Qnl
5pxKnKe87Ppap/lkchmVoMOJul5ZiuJqtdjWrHInBR0XOol4fp8bBiURED4tri0r
RhxVU7NE8I8IZIDUla+OinPvijRRs2rdg5ys8KFVrd/z71itiE8YTsBu49fIA98r
onePgvpPnMIE593ilS0UEVwuicWnMA04GcBfLhxMEphd2nclgVFDvHVkp3dD94La
E4abcu1W/pEsfBCl1dZ5IfygUKE0gUY217d3a340xe3mo8fwpCVflUhwsjI/1F2a
JOrwfvlcXV3q4abIF80C30rw0NVLbp4/WWvdN8ocDuLTXoJPht9A6e/Am4sHyHKv
rnmfJ5pfbkJEr67A5lMZnnV/xG5rWu2ujuUofkV9rRyFhM1xCB7Z8GUDZeUMPBA2
B476yXnvDLcwa312Yt4157IQwEOilKBhfEEAN2MCCoaoLoTaRtefQ98J4kkjhn8M
HmYh5TbI6IU64wtlAuS5scd1g+sdUXFbdMih1wtmH00fAgMBAAE=
-----END PUBLIC KEY-----
```

Private Key
```python
print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
```
```
(
    n=0xa9eb161553916df2af993c4bf909e5e69c4a9ca7bcecfa5aa7f964721995a0c389ba5e598ae26ab5d8d6ac7227051d173a89787e9f1b062511103e2dae2d2b461c5553b344f08f086480d495af8e8a73ef8a3451b36add839cacf0a155addff3ef58ad884f184ec06ee3d7c803df2ba2778f82fa4f9cc204e7dde2952d14115c2e89c5a7300d3819c05f2e1c4c12985dda7725815143bc7564a77743f782da13869b72ed56fe912c7c10a5d5d67921fca050a134814636d7b7776b7e34c5ede6a3c7f0a4255f954870b2323fd45d9a24eaf07ef95c5d5deae1a6c817cd02df4af0d0d54b6e9e3f596bdd37ca1c0ee2d35e824f86df40e9efc09b8b07c872afae799f279a5f6e4244afaec0e653199e757fc46e6b5aedae8ee5287e457dad1c8584cd71081ed9f0650365e50c3c1036078efac979ef0cb7306b7d7662de35e7b210c043a294a0617c41003763020a86a82e84da46d79f43df09e24923867f0c1e6621e536c8e8853ae30b6502e4b9b1c77583eb1d51715b74c8a1d70b661f4d1f, 
    d=0x501bb2be1c3780a7fd6c979653d37c4d845ad2cf6c0d279cecfb71852f95b104ef1e6bd3f85bf5a645143499ded694d7fa338c98d9c72257005bf18c94c4dbd5828f21d66f46a0907add981bf7f8124345681971794e851fc3126fa2086460a4bf2f4624f0f14b5383142d0bb1f399bd4f73dbf2c9ece435eee0d7adafe279aac590139cd6552d214ae634b58791eebeb4bc1e7500cc98019a922f72de329540c661ec458411a17ce102f2444608b6e2c4ec2e8c33f457efcca1e30e4db0110fba4ffce79e65db09dbfcd72d38b3e629f56d388240e4dcb7e49bc27e3f70cad4815967cf0271454463612826adb732da024b80820ef385eed2da5da78e003408536327df4d6ed8ee932379a495271efd85beb26107de257302c24353896d8f947b24bb1e903926b6ef25313becf79ccdc831b99938c173c06ce3a6909cece7662d4e8f6ff9ba07822841cc3e6f19fc5ef4b840b372b63bf6a1110e41ab85e4abf3989b21a88ab5ede83dceaeadcd3c2639da49498da693fa52860de9aebe3599
)
```

Begin Private Key
```python
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))
```
```
-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----
```

Encrypt the message using RSA-OAEP encryption scheme 
(RSA with PKCS#1 OAEP padding) with the RSA public key
```python
msg = b'A message for encryption'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
print("Encrypted:", binascii.hexlify(encrypted))
```
```
b'76d2ae010576a801bdeb25dfc385d4940a6acfd753056a048805bf62e4a8b0f29d1eb96ecc461ba80f8efcf2c557dd1141b306b4e1df20023daee3276ef2a15a28e28ad5cdd3cd016f06362c43c1ae8375d79d7e1bbdbbc4361ea2fb35a485fadb46a655b1187c8b66bb3775f261b9918197035f09cbfa09665ea2685591ec2d9fbb63bec7eeb55a2e50779a93d711fe71bf8880a71c622791c4a8858776e811be7ba846cbda216bcb355ea36660d41b6327710c2768636f2a75cc11a78a0518fab56eca7770b76844b16d0ece1bed0530adae8b1813e80e01522f3cecca0909cc91559b35f9d3facb35f79a8bc5a34c127cf385e588ad490d5ca5c48ac4ed61149ec3dfca6880875ab2cc6edb21d0e37f21d5e9966672a0439ff020e469aa94680fa250a775dc4c31d45fdbbd29f7c512fa3886e3cb5c6ae3bf00078ed3601edc475bfcd03770853e48b16006fd356b38d010ee3373ca1f638e74f063487e6d2ae87f410c2945d50d8dd52b3bf1b1a0f111b7f3c3caf3560429bac9755eb609'
```

Decrypt message using using RSA-OAEP 
with the RSA private key
```python
decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted)
```
```
b'A message for encryption'
```