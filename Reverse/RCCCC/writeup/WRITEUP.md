## RCCCC

First use D-801 to remove confusion, and then this question is actually very simple to complete the confusion. It is RC4, but it is different from the previous RC4. Here, the original RC4 digits are set +1, but it can be solved dynamically

### exp

```python
import binascii
from Crypto.Util.number import *
def rc4_crypt(text,key):
    textlen=len(text)
    keylen=len(key)
    ciper=[]
    count=0
    s=list(range(256))
    for i in range(256):
        count=(count+s[i]+key[i%keylen])%256
        s[i],s[count]=s[count],s[i]
    i=0
    j=0
    for m in range(textlen):
        i=(i+1)%256
        j=(j+s[i]+1)%256
        s[i],s[j]=s[j],s[i]
        k=s[(s[i]+s[j])%256]
        ciper.append(k^text[m])
    ciper_text=''.join("%02x"%i for i in ciper)
    return ciper_text.upper()

if __name__ == "__main__":
    s = [0x54,0x89,0x61,0x10,0xd7,0xdf,0x33,0x11,0xc0,0x43,0xdf,0x76,0xdf,0x28,0xda,0xe6,0x13,0x45,0x81,0x6d,0x79,0x18,0xc7]
    data = 'BE3924244CD030697D071E65BEBE5BF050EE84D2C94611'
    key = '6b6579735f4c4c564d'
    print("rc4 result:", rc4_crypt(binascii.a2b_hex(data), binascii.a2b_hex(key.upper())))
    print(long_to_bytes(0x4D4F43534354467B6D315F4C4C564D5F7730726C64217D))

#
```

final flag is MOCSCTF{m1_LLVM_w0rld!}

