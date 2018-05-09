program geometrics
!Program for Geometric Sequences
implicit none
real :: r,a,sums,m,p,space
integer :: n,i
m = 0
sums = 0
print *, '-= Enter n, a, then r =-'
read *, n,a,r
p = a
do i=1,n
	sums = sums + p 
	m = m + 1
	p = a*(r**m)
end do
print *, sums
read *, space
end program geometrics