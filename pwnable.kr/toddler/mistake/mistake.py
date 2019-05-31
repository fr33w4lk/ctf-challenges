from pwn import *

context.log_level = "DEBUG"

s = ssh(host='pwnable.kr', port=2222, user='mistake', password='guest')
s.download_file('mistake')
s.download_file('mistake.c')

##p = s.process("./leg")
#
#print p.recv()
#
#key = ""
#p.sendline(key)
#
#print p.recv()
#
#p.close()
