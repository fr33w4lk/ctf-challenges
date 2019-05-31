from pwn import *

context.log_level = "DEBUG"

s = ssh(host='pwnable.kr', port=2222, user='random', password='guest')
#s.download_file('random')
#s.download_file('random.c')
p = s.process("./random")
#p = process("./random")

# rand() does not generate a random number if there is no seed in $HOME/.rnd
rand_num = int('0x6b8b4567', 16)

deadbeef_int = int('0xdeadbeef', 16)
key = rand_num ^ deadbeef_int

p.sendline(str(key))

print p.recv()

p.close()

