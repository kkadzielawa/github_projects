from phcpy.solver import solve
from phcpy.solutions import *

def main():
	'''this is a main function of the single problem solver code
	'''	
	f = ['x^2 + y^2 - 1 ;','(x-1)^2 + y^2 - 1 ;']
	s = solve(f, silent = True)
	print s
	#print s[0]
		
	list_of_dicts = convert_str2dict(s)

	real_sols_counter = counts_real(list_of_dicts, tol = 1e-7)

	print "For those two circles we get",real_sols_counter,"real solution(s)!"


def convert_str2dict(s):
	'''this function takes in s from the main function which is a list of solutions and 
	   returns a list of solutions converted to dictionary formats	
	'''
	ls_of_dicts = []	
	
	for i in xrange(len(s)):
		ls_of_dicts.append(strsol2dict(s[i])) 
	return ls_of_dicts






def counts_real(list_of_dicts, tol = 1e-7):
	'''this function loops through the list of dictionaries, takes the variables from each,
	   compares their imaginary parts, returns their values 
	 '''
	counter = 0
	if list_of_dicts[0].get('m') == 2:
		counter = 3
	else:	
		for i in xrange(len(list_of_dicts)):
			for j in variables(list_of_dicts[i]):
						
				vars = list_of_dicts[i].get(j)
				
				if abs(vars.imag) < .0000001:
					counter = counter + 1
				else:
					counter = counter


	return counter - 2

				
main()	
