from pwn import *

context.log_level = "DEBUG"

context.terminal = ['tmux', 'splitw', '-v']

#p = ssh(host='pwnable.kr', port=2222, user='otp', password='guest')
#p.download_file('otp')
#p.download_file('otp.c')

input = "-1"

p = process(["./otp", input])
#gdb.attach(p, '''
#continue
#''')

p.recv()
