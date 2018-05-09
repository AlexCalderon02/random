	org 50000
last_k	equ 23560	;Checks last ASCII value
loop	ld hl, last_k	;Loads last_k memory location
	ld a, (hl)	;Loads hl into a
	cp 32		;Compares a and specified ASCII value
	jr z, start
	jp loop
start	ld hl, udgs	;Loads UDG into hl
	ld (23675), hl	;Loads memory location of hl
	ld a, 2		
	call 5633	;Expects 2 in register a
	ld de, begin	
	ld bc, eostr-begin
	call 8252	;Prints string
	ld a, 144	;Loads ASCII value for UDG
	rst 16		;Prints last register (a)
	ret
begin	defb 22, 4, 5, "RECTANGLE VOLUME CALC"
	defb 22, 4, 5, "Press Spacebar to Begin"
eostr	equ $	;Labels memory location
;start	defb 22, 6, 0, "Enter Width, Length, then Height"
udgs	defb 56, 56, 16, 56, 84, 146, 40, 68
;smile	defb 102, 102, 0, 24, 153, 66, 36, 24
