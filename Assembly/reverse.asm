section .data
    input db 'SuperDuperProgram', 0   ; The string to reverse
    input_len equ $-input             ; Length of the string
    output db 0                       ; Placeholder for the output string

section .bss
    reversed resb input_len           ; Reserve space for the reversed string

section .text
    global _start

_start:
    mov esi, input                    ; Load address of input string
    mov edi, reversed                 ; Load address for reversed string
    mov ecx, input_len                ; Set loop counter to string length

reverse_loop:
    dec ecx                           ; Decrease counter
    mov al, [esi + ecx]               ; Load byte from end of input string
    mov [edi], al                     ; Store it in reversed string
    inc edi                           ; Move to next position in reversed string
    cmp ecx, 0                        ; Check if we have reached the beginning
    jnz reverse_loop                  ; If not, continue loop

    mov edx, input_len                ; Set the length of the string to output
    mov ecx, reversed                 ; Load the address of the reversed string
    mov ebx, 1                        ; File descriptor (stdout)
    mov eax, 4                        ; System call number (sys_write)
    int 0x80                          ; Call kernel

    mov eax, 1                        ; System call number (sys_exit)
    xor ebx, ebx                      ; Exit code 0
    int 0x80                          ; Call kernel
