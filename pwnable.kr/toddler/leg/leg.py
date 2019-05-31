#from pwn import *
#import time
#
#context.log_level = "DEBUG"
#
#s = ssh(host='pwnable.kr', port=2222, user='leg', password='guest')
##s.download_file('leg')
#
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

print str(0x00008ce4 + 0x00008d08 +4 + 0x00008d80)
