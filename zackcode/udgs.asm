	org 50000
	ld hl, udgs
	ld (23675), hl
	ld a, 2
	call 5633
	ld de, string
	ld bc, eostr-string
	call 8252
	ld a, 144
	rst 16
	ret
string	defb "hello"
eostr	equ $
udgs	defb 56, 56, 16, 56, 84, 146, 40, 68
smile	defb 102, 102, 0, 24, 153, 66, 36, 24
