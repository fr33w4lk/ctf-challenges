from pwn import *

#0x21DD09EC
num = 568134124

n1 = num - 4 * (num / 5)
n2 = num / 5

if n1 + n2*4 != num:
    print "incorrect %s + %s = %s" % (n1, n2*4, (n1+n2*4))

payload = 4 * p32(n2) + p32(n1)

print repr(payload)

s = ssh(host='pwnable.kr', port=2222, user='col', password='guest')

sh = s.process(['./col', payload])
print repr(sh.recvall())
