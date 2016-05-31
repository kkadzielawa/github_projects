from phcpy.solver import solve
from phcpy.solutions import *
from sympy import symbols
import random
import json
def main():
	'''this is main function'''


	my_random_list_of_lists = random_nums_list_generator(.8,1.5,6,5) #generate a list of 9 floats, will be assigned to a1,a2 etc respectiveliy

	#print my_random_list_of_lists #print a random floats list

	final_list = pop_list_of_lists(my_random_list_of_lists)

	#my_random_list = []

	
	#print final_list

	#print my_random_list

	#final_list_of lists = []

	#final_list_of_lists.append(

	#print my_random_list_of_lists

	#initial_sols_list = return_solns(my_random_list_of_lists) #this contains a list of solutions given 9 parametrs from random_list
	
	#print initial_sols_list

	#final_list = take_tuple_return_list(initial_sols_list)
	
	#dict_list = convert_str2dict(initial_sols_list) # this convert the list of solutions to dictionary format

	#print dict_list

	#final_list = counts_real_total(dict_list) # this counts the number of real sols for the given list in dict format


	# of reals sols
	
	print final_list
	string_of_values = final_printout(final_list)	
	
	print string_of_values

def pop_list_of_lists(my_random_list_of_lists):

	outer_list = []
	
	for i in xrange(len(my_random_list_of_lists)):
		
		inner_list = []		

		inner_list = my_random_list_of_lists[i]
			
		inner_list.append(counts_real_total(convert_str2dict(return_solns(inner_list))))
		
		outer_list.append(inner_list)

	return outer_list
	

def random_nums_list_generator(low, high, size,trials):

	list_of_lists_of_nums = [] 

	for i in range(trials):
		
		list_of_lists_of_nums.append([random.uniform(low,high) for _ in xrange(size)])

	return list_of_lists_of_nums

def final_printout(final_list):

	num_of_real_sols = []

	for i in range(len(final_list)):
		print "For the set of paramaters of:",final_list[i][0:6], "we get",final_list[i][6],"real solution(s)!"
		num_of_real_sols.append(final_list[i][6])
	return num_of_real_sols, max(num_of_real_sols)



'''
def take_tuple_return_list(tuple_sols_list):

	big_list = []

	for args in tuple_sols_list:

i		my_list = []
		my_list.append(args[0])
		my_list.append(args[1])
		my_list.append(counts_real_total(convert_str2dict(args[2])))
		big_list.append(my_list)

	return big_list
'''

def return_solns(my_random_list):


	a1,a2,a3,b2,b3,c3 = my_random_list
	r1 = .5
	r2 = .5
	r3 = .5
	v1,v2,v3,u1,u2,u3 = symbols(' v1 v2 v3 u1 u2 u3')

        p1 = str(v1**2 + v2**2 + v3**2 -1) + ';'
        p2 = str(u1*v1 + u2*v2 + u3*v3) + ';'
        p3 = str(u1**2 + u2**2 + u3**2 - 1) + ';'
        p4 = str(-2*u1*a1 - v1**2*a1**2 + a1**2 - r1**2 + 1) + ';'
        p5 = str(-2*u1*a2 - 2*u2*b2 - v1**2*a2**2 - 2*v1*v2*a2*b2 - v2**2*b2**2 + a2**2 + b2**2 - r2**2 + 1) + ';'
        p6 = str(-2*u1*a3 - 2*u2*b3 - 2*u3*c3 - v1**2*a3**2 - 2*v1*v2*a3*b3 - 2*v1*v3*a3*c3 - v2**2*b3**2 - 2*v2*v3*b3*c3 - v3**2*c3**2 + a3**2 + b3**2 + c3**2 - r3**2 + 1) + ';'

        system = [p1,p2,p3,p4,p5,p6]

        s = solve(system, silent = True)
			
	return s


def convert_str2dict(solution_list):
	#his function takes in s from the main function which is a list of solutions and 
	#   returns a list of solutions converted to dictionary formats	
	#
	ls_of_dicts = []	
	with open('outputspheres.txt','w') as my_file:	
		for i in xrange(len(solution_list)):
			print "For the solution number ",i, "we get", solution_list[i]
	
			json.dump(solution_list[i], my_file)

			ls_of_dicts.append(strsol2dict(solution_list[i])) 
	return ls_of_dicts



def counts_real_total(list_of_dicts, tol = 1e-7):
	#this function loops through the list of dictionaries, takes the variables from each,
	#  compares their imaginary parts, returns their values 
	#
	counter = 0

	big_list = []

	for i in xrange(len(list_of_dicts)):
		
		if list_of_dicts[i].get('m') == 2:
			
			counter = counter + 1 
		else:	
			
			is_real = True

			for j in variables(list_of_dicts[i]):
				
				each_var = list_of_dicts[i].get(j)				
			
				if abs(each_var.imag) > .00000001:
					is_real = False
					break	
				else:
					is_real = is_real
					

			if is_real == True:

				counter = counter + 1

	
	return counter 

				
main()	
