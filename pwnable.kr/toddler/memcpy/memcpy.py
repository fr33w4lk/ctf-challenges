from pwn import *

context.log_level = "DEBUG"

s = ssh(host='pwnable.kr', port=2222, user='memcpy', password='guest')

p = s.process(["nc", "0", "9022"])
#p = process("./memcpy")

"""
MOVNTPS stores data from a SIMD floating-point register to memory. The memory address must be aligned to a 16-byte boundary; if it is not aligned, a general protection exception will occur. The instruction is implicitly weakly ordered, does not write-allocate, and minimizes cache pollution. 
http://www.tommesani.com/index.php/component/content/article/2-simd/56-sse-cacheability-control.html

https://stackoverflow.com/questions/10224564/what-does-alignment-to-16-byte-boundary-mean-in-x86

https://www.felixcloutier.com/x86/movntps

http://www.jaist.ac.jp/iscenter-new/mpc/altix/altixdata/opt/intel/vtune/doc/users_guide/mergedProjects/analyzer_ec/mergedProjects/reference_olh/mergedProjects/instructions/instruct32_hh/vc197.htm

http://www.jaist.ac.jp/iscenter-new/mpc/altix/altixdata/opt/intel/vtune/doc/users_guide/mergedProjects/analyzer_ec/mergedProjects/reference_olh/mergedProjects/instructions/instruct32_hh/vc183.htm
"""

# we need to make sure the buffers are aligned to 16byte boundaries

p.recvuntil("specify the memcpy amount between ")
p.sendline('8')

p.recvuntil("specify the memcpy amount between ")
p.sendline('16')

p.recvuntil("specify the memcpy amount between ")
p.sendline('32')

p.recvuntil("specify the memcpy amount between ")
p.sendline('72')

p.recvuntil("specify the memcpy amount between ")
p.sendline('136')

p.recvuntil("specify the memcpy amount between ")
p.sendline('264')

p.recvuntil("specify the memcpy amount between ")
p.sendline('536')

p.recvuntil("specify the memcpy amount between ")
p.sendline('1064')

p.recvuntil("specify the memcpy amount between ")
p.sendline('2056')

p.recvuntil("specify the memcpy amount between ")
p.sendline('4160')

p.recvall()

p.close()
