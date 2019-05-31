from pwn import *

context.log_level = "DEBUG"

context.terminal = ['tmux', 'splitw', '-v']

key = "330d475b532f251c1d23303f0d49530f1c1d183b2c341b001b703b350b1b08452b00"

def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

password = "A"*100

binary_a = key.decode("hex")
binary_b = password.decode("hex")

xor_strings(binary_a, binary_b).encode("hex")

payload = "A"*100

#s = ssh(host='pwnable.kr', port=2222, user='blukat', password='guest')
#s.download_file('blukat')
#s.download_file('blukat.c')

#p = s.process("./blukat")
p = process("./blukat")

gdb.attach(p, '''
continue
''')

p.recvuntil("guess the password!")

p.sendline(payload)

p.recv()
#p.interactive()
