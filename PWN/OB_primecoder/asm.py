from pwn import *

context.arch = "amd64"
print(asm("xor ebx,ebx"))
print(
    chr(0x68)
    + chr(0x73)
    + chr(0x2F)
    + chr(0x2F)
    + chr(0x6E)
    + chr(0x69)
    + chr(0x62)
    + chr(0x2F)
)
# 小端序
# 凑满2byte-空指令
shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

print(disasm(shellcode))