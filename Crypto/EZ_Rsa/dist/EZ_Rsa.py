from Crypto.Util.number import *
from gmpy2 import *

flag=open('dist/flag.txt','r').readline().strip()


#assert len(flag)==48
flag1=flag[0:8].encode()
flag2=flag[16:int(2*len(flag)/3)].encode()
flag3=flag[int(2*len(flag)/3):].encode()

print(flag1+flag2+flag3)


print("=====================================flag1")
m=bytes_to_long(flag1)
p=getPrime(64)
q=getPrime(64)
e=65537
n=p*q
c=powmod(m,e,n)
print("n =",n)
print("e =",e)
print("c =",c)



print("=====================================flag2")
m=bytes_to_long(flag2)
p=getPrime(1024)
q=next_prime(p)
e=65537
n=p*q
c=powmod(m,e,n)
print("n =",n)
print("e =",e)
print("c =",c)


print("=====================================flag3")
m=bytes_to_long(flag3)
p=getPrime(1024)
q=getPrime(1024)
e1=65537
e2=12345
n=p*q
c1=powmod(m,e1,n)
c2=powmod(m,e2,n)
print("n =",n)
print("e1 =",e1)
print("e2 =",e2)
print("c1 =",c1)
print("c2 =",c2)
