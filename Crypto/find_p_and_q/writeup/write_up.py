from Crypto.Util.number import bytes_to_long,long_to_bytes, getPrime,inverse
from pwn import *
import gmpy2

r=remote('127.0.0.1', 21011)
#get data
def get_data():
    data = str(r.recvuntil('========================================================='))
    c = int(data.split('c = ')[1].split('\n')[0])
    N = int(data.split('N = ')[1].split('\n')[0])
    e = int(data.split('e = ')[1].split('\n')[0])
    hints = int(data.split('Hints: |p - q| = ')[1].split('\n')[0])
    return c, N, e, hints

c, N, e, Hints = get_data()

p = ((-1) * Hints + gmpy2.iroot((Hints ** 2 + 4 * N), 2)[0]) // 2
q = N//p

print("p=",p)
print("q=",q)
n = p * q
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
m = pow(c, d, n)

r.sendlineafter('Please input the \'m\' in 5 second:\n', str(m))
r.interactive()
