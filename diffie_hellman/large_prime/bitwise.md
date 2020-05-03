## Bitwise operator
* __x << n__ : Left shift value x by n bits
* __x|n__ : Perform OR between x and n in binary

### Code
```python
from random import getrandbits
length = 3
p = getrandbits(length)
print(p)

p |= (1 << length - 1) | 1 # p = p | ((1 << length - 1) | 1)
""" This will left shift 1 by (length - 1) 0's. Then it will perform OR with 1 it will get something like : 10000....001 """
print(p)
```