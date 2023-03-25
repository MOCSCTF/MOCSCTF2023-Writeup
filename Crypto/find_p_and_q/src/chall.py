import random
from Crypto.Util.number import getStrongPrime, isPrime
from threading import Timer

count = 0
count_down = 5

flag = open('flag.txt', 'r').read()
m = random.randrange(1000000000000,9999999999999)

p = getStrongPrime(1024)
q = getStrongPrime(1024)
N = p * q
e = 65537
c = pow(m, e, N)
Hints = abs(p - q)

print(f'c = {c}')
print(f'N = {N}')
print(f'e = {e}')
print(f'Hints: |p - q| = {Hints}')

def print_time():
    global t, count
    count += 1
    if count < count_down:
        t = Timer(1, print_time)
        t.start()
    else:
        print("Time up")
        exit(0)
t = Timer(1, print_time)
t.start()

print("\n=========================================================")
print("Please input the 'm' in 5 second:")
try:
    ans = input()
    if int(ans) == m and count < count_down:
        print(flag)
    elif int(ans) == m and count >= count_down:
        print("Correct answer but time out")
except:
    print("Wrong answer!!!!!")
    exit(0)
