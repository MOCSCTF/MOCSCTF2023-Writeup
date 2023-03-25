```
First use 4.01 upx to unpack

Correspondingly, it will be input into pushvector

Then there is a simple escape XOR

The editor-in-chief is to scramble the order of the bits in the exception or the following string by two-by-one bitwise operation, and then throw it into the tea and encrypt it. encrypted

The result is compared with the known ciphertext. Compare two bits at a time.
```



### exp

```python
def decrypt(v, k):
    v0 = v[0]
    v1 = v[1]
    x = (0x12345678*32)&0xffffffff
    delta = 0x12345678
    k0 = k[0]
    k1 = k[1]
    k2 = k[2]
    k3 = k[3]
    for i in range(32):
        v1 -= ((v0 << 4) + k2) ^ (v0 + x) ^ ((v0 >> 5) + k3)
        v1 = v1 & 0xFFFFFFFF
        v0 -= ((v1 << 4) + k0) ^ (v1 + x) ^ ((v1 >> 5) + k1)
        v0 = v0 & 0xFFFFFFFF
        x -= delta
        x = x & 0xFFFFFFFF
    v[0] = v0
    v[1] = v1
    return v
if __name__ == '__main__':
    plain = [0x53d5c338,0x3a3bd468,0x639dfa0,0x4b21ae83,0xa22978f3,0x9a503149,0x6245d5a2,0xeb1b3894,0xe91c7431,0xefa82ff8,0x84102a18,0x6276bf7a,0xac1d4eaf,0x1545a345,0x7e14f1c3,0x961a6041,0xf2864e31,0xc7e0537f,0xf3e2e4c6,0xa9baf698,0xfe39dc26,0x5238dcf7,0xb40dd177,0x9a13445,0xb1ab02bb,0x5c88e313,0x1f49d959,0x662e6383,0x2e842449,0xbdd7200c,0xf2864e31,0xc7e0537f,0x9ea28242,0xb22a138c]
    key = [0x61656574,0x79656b5f,0x5f73695f,0x65726568]
    f2 = []
    for i in range(len(plain)//2):
        temp = plain[:2]
        decrypted = decrypt(temp, key)
        f2.append(decrypted[0])
        f2.append(decrypted[1])
        plain = plain[2:]
    f3 = []
    for i in range(len(f2)//2):
        f3.append(((f2[2*i]&0xf)<<4)|((f2[i*2+1]&0xf)))
        f3.append(((f2[2*i])>>4)|(((f2[2*i+1])>>4)<<4))
    for i in f3:
        print(chr((i^15)&0xff),end="")

# MOCSCTF{no_cpp_re_but_you_made_it}
```

