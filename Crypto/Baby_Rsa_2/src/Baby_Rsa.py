from Crypto.Util.number import bytes_to_long,long_to_bytes, getPrime,inverse

flag = open('dist/flag.txt', 'rb').read().strip()

p, q = getPrime(1024), getPrime(1024)
n = p*q
phi_n = (p-1)*(q-1)
e = 65537
random_p=18
#s = pow(557*p - 127*q, n - p - q, n)
formula = f"{random_p}*d+c*phi_n-2*n-2023"
c = pow(bytes_to_long(flag), e, n)
d= inverse(e,phi_n)

#m=long_to_bytes(pow(c, d, n))

#print(m)

print(f'n = {n}')
print(f'c = {c}')
print(f'{formula} = {eval(formula)}')

#d=(eval(formula)+2*n+2023)//random_p
