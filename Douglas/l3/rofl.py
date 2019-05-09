import struct

## mov    eax,ds:0x804988c
## cmp    eax,0x40
## 0x40 == 64

fmt = "%1$64x%7$n\0 "
m = struct.pack("<I", 0x804988c)
print fmt + m
