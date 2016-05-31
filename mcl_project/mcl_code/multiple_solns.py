from phcpy.solver import solve
from phcpy.solutions import *
from sympy import symbols
from numpy import arange


def main():
	'''this is main function'''

	print "Welcome to the root finding program for a unit circle and a given circle: "
	
	c_i = raw_input("Please enter the initial coordinate of the circle (other than 0) : ")
	c_f = raw_input("Please enter the final x coordinate of the circle: ")
	r_i = raw_input("Please enter the initial radius of the circle: ")
	r_f = raw_input("Please enter the final radius of the circle: ")
	step = raw_input("Please enter the interval/step size by which you would like to travel: ")
	
	float(c_i),float(c_f),float(r_i),float(r_f),float(step) #converts to float

	compound_sols_list = return_solns(c_i,c_f,r_i,r_f,step)#create a list of lists of solutions
	
	print compound_sols_list	

	solution_list = []

	while compound_sols_list:
		solution_list.extend(compound_sols_list.pop(0))

	list_of_dicts = convert_str2dict(solution_list)
	
	
	
	total_sols = counts_real(list_of_dicts, tol = 1e-7)

	print "The total is",total_sols," real solution(s)!"


def return_solns(c_i,c_f,r_i,r_f,step):

	my_sols_list = []
	for i in arange(c_i,c_f + step,step):
		for j in arange(r_i,r_f + step,step):
			x, y = symbols('x y')
			coeff = float(i)
			rad = float(j)
			f1 = str(x**2 + y**2 - 1) +';'
			f2 = str(x**2 - 2*coeff*x + coeff**2 + y**2 - rad**2) + ';'
			f = [f1, f2]
			s = solve(f, silent = True)
			my_sols_list.append(s)
	return my_sols_list


def convert_str2dict(solution_list):
	'''this function takes in s from the main function which is a list of solutions and 
	   returns a list of solutions converted to dictionary formats	
	'''
	ls_of_dicts = []	
	
	for i in xrange(len(solution_list)):
		ls_of_dicts.append(strsol2dict(solution_list[i])) 
	return ls_of_dicts






def counts_real(list_of_dicts, tol = 1e-7):
	'''this function loops through the list of dictionaries, takes the variables from each,
	   compares their imaginary parts, returns their values 
	 '''
	counter = 0
	
	for i in xrange(len(list_of_dicts)):
		if list_of_dicts[i].get('m') == 2:
			counter = counter + 1
		else:	
			for j in variables(list_of_dicts[i]):
					
				vars_value = list_of_dicts[i].get(j)
				
					
				
				if abs(vars_value.imag) < .0000001:
					counter = counter + 1
				else:
					counter = counter
				
			

	return counter - 2

				
main()	
