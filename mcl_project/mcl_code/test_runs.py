from phcpy.solver import *
from phcpy.solutions import *
#import matplotlib.pyplot as plt 
from numpy import arange


def main():
	
'''
	f = ['x^2 + y^2 - 1;','(x-.5)^2 + y^2 - 1;']
	s = solve(f, silent = True)
	step = .5
	initial = .5
	final  = 2
	

	list_of_tuples = [(1,1,"Hello"),(1,2,"How"),(2,1,"Are"),(2,2,"You")]


	new_list = []

	for i in list_of_tuples:
		
		new_list.append(i[2])

	print new_list


	d = []
	for i in range(len(s)):
		d.append(strsol2dict(s[i]))	
		
	
	 	

	for i in range(len(d)):
		for j in variables(d[i]):
			print j
			z = d[i].get(j)
			print z
			if abs(z.imag) < .000001:
				print "Real"
			else:
				print "Imaginary"

	z = d[0].get('y')
	print z
	w = z.imag 
	print w

	if z.imag < .000001:
		print "Less"
	else:
		print "More"

	t = abs(z.imag)
	print t






	counter = 0
	
	if abs(imag(y)) < .00000001:
		counter = counter + 1
	else:
		counter = counter	

	print counter

 
	
	v = convert_to_dict
	print v

def convert_to_dict(s):
	d = []

	for i in range(len(s)):
		d[i] = strsol2dict(s[i])
	return d
main()

