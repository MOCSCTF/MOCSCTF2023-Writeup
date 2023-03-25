from Crypto.Util.number import bytes_to_long, getPrime

flag = open('dist/flag.txt', 'rb').read().strip()

p, q = getPrime(512), getPrime(512)
n = (p-1)*(q-1)
e = 5

#s = pow(557*p - 127*q, n - p - q, n)

c = pow(bytes_to_long(flag), e, n)

print(f'n = {n}')
print(f'e = {e}')
print(f'c = {c}')
