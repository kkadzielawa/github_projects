from phcpy.solver import solve
from phcpy.solutions import *
from sympy import symbols
from numpy import arange
import random

def main():
	'''this is main function'''

	print "Welcome to the root finding program for a unit circle and a given circle: "

	c_i = float(raw_input("Please enter the initial x coordinate of the circle: "))
	c_f = float(raw_input("Please enter the final x coordinate of the circle: "))
	r_i = float(raw_input("Please enter the initial radius of the circle: "))
	r_f = float(raw_input("Please enter the final radius of the circle: "))
	step = float(raw_input("Please enter the distance/interval by which you would like to travel: "))
	

def generate_random_numbers(c_i,c_f,r_i,r_f):

	coeff = random.uniform(c_i,c_f)
	rad = random.uniform(r_i,r_f)
	x,y = symbols('x y')
	f1 = str(x**2 + y**2 - 1) +';'
	f2 = str(x**2 - 2*coeff*x + coeff**2 + y**2 - rad**2) +';'
	f = [f1,f2]
	sol = solve(f, silent = True)
	











	tuple_sols_list = return_solns(c_i,c_f,r_i,r_f,step)	

	print tuple_sols_list

	compound_sols_list = take_tuple_return_list(tuple_sols_list)
		
	print compound_sols_list	

	solution_list = []

	while compound_sols_list:
		solution_list.extend(compound_sols_list.pop(0))	

	
	

	list_of_dicts = convert_str2dict(solution_list)

	total_real_sols_counter = counts_real_total(list_of_dicts, tol = 1e-7)

	print "For those two circles we get a total of",total_real_sols_counter, "real solution(s)!"

#def count_real_sols_single_strs(one_solution)





def take_tuple_return_list(tuple_sols_list):

	
	coord_sols_list = []

	for i in range(len(tuple_sols_list)):
		tuple_sols_list[i][2].append(coord_sols_list)

	return coord_sols_list




#def return_num_sols(



def return_solns(c_i,c_f,r_i,r_f,step):

	my_sols_list = []
	my_tuple_list = ()
	for i in arange(c_i,step+c_f,step):
		for j in arange(r_i,step+r_f,step):
			x, y = symbols('x y')
			coeff = float(i)
			rad = float(j) 
			f1 = str(x**2 + y**2 - 1) +';'
			f2 = str(x**2 - 2*coeff*x + coeff**2 + y**2 - rad**2) + ';'
			f = [f1, f2]
			s = solve(f, silent = True)
			my_tuple_list = (i,j,s)
			my_sols_list.append(my_tuple_list)
			
	return my_sols_list


def convert_str2dict(solution_list):
	'''this function takes in s from the main function which is a list of solutions and 
	   returns a list of solutions converted to dictionary formats	
	'''
	ls_of_dicts = []	
	
	for i in xrange(len(solution_list)):
		ls_of_dicts.append(strsol2dict(solution_list[i])) 
	return ls_of_dicts



def counts_real_total(list_of_dicts, tol = 1e-7):
	'''this function loops through the list of dictionaries, takes the variables from each,
	   compares their imaginary parts, returns their values 
	 '''
	counter = 0

	for i in xrange(len(list_of_dicts)):

		if list_of_dicts[i].get('m') == 2:
			counter = counter + 1
		else:	
			for j in variables(list_of_dicts[i]):
						
				vars = list_of_dicts[i].get(j)
				
				if abs(vars.imag) < .0000001:
					counter = counter + 1
				else:
					counter = counter


	return counter - 2

				
main()	
