from pwn import *

r=remote('127.0.0.1', 21030)

#get data
known_password=int((r.recvuntil("password:").decode()).split('\n')[0])


def babyhash(key: str) -> int:
    hash_value = 0
    prime = 31
    max_value = 5000000
    for i in range(len(key)):
        char = key[i]
        hash_value += (ord(char) - 96) * (prime ** i)
    return hash_value % max_value

#known_password = "3662096"

for i in range(0,100000000):
    trystr = "MOCSCTF" + str(i)
    if int(babyhash(trystr)) == int(known_password):
        r.sendline(trystr)
        break

r.interactive()
