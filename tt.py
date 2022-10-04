print('ax^2+bx+c')
a=float(input('a = '))
b=float(input('b = '))
c=float(input('c = '))
d=b**2-4*a*c
print('discriminant = ', d)
if d>0:
	x1=(-b+d**0.5)/(2*a)
	x2=(-b-d**0.5)/(2*a)
	print('x1 = ', str(x1))
	print('x2 = ', str(x2))
if d==0:
	x=-b/(2*a)
	print('x = ', str(x))
else:
	print('korney net')
