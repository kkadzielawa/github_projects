from phcpy.solver import solve
from sympy import symbols
from phcpy.solutions import strsol2dict



def main():


	v1,v2,v3,u1,u2,u3 = symbols(' v1 v2 v3 u1 u2 u3')

	a1 = 1
	a2 = 1
	a3 = 1
	b2 = 2
	b3 = 2
	c3 = 1
	r1 = 3
	r2 = 2
	r3 = 3

	p1 = str(v1**2 + v2**2 + v3**2 -1) + ';' 
	p2 = str(u1*v1 + u2*v2 + u3*v3) + ';'
	p3 = str(u1**2 + u2**2 + u3**2 - 1) + ';'
	p4 = str(-2*u1*a1 + v1**2*a1**2 + a1**2 - r1**2 + 1) + ';'
	p5 = str(-2*u1*a2 - 2*u2*b2 - v1**2*a2**2 - 2*v1*v2*a2*b2 - v2**2*b2**2 + a2**2 + b2**2 - r2**2 + 1) + ';'
	p6 = str(-2*u1*a3 - 2*u2*b3 - 2*u3*c3 - v1**2*a3**2 - 2*v1*v2*a3*b3 - 2*v1*v3*a3*c3 - v2**2*b3**2 - 2*v2*v3*b3*c3 - v3**2*c3**2 + a3**2 + b3**2 + c3**2 - r3**2 + 1) + ';'

	system = [p1,p2,p3,p4,p5,p6]

	s = solve(system, silent = True)

	print s[0]
	print s[1]








main()
