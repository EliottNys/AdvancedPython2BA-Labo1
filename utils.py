# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
import math

def fact(n):	#renvoie le factoriel de n
	if n < 0:
		resultat = ValueError
	elif n == 0:
		resultat = 1
	else:
		resultat = n
		while n > 1:
			n -= 1
			resultat *= n
	return resultat

def roots(a, b, c):		#renvoie les racines de l'equation ax^2 + bx + c = 0 sous forme de tuple
	D = b**2 - 4*a*c
	if D < 0:
		return ()
	if D == 0:
		x = (-b + math.sqrt(D))/(2*a)
		return (x)
	if D > 0:
		x1 = (-b + math.sqrt(D))/(2*a)
		x2 = (-b - math.sqrt(D))/(2*a)
		return (x1, x2)

def integrate(function, lower, upper):		#renvoie l'integrale de lower à upper de l'equation function
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	# I was unable to import the scipy mudule, further research necessary.
	pass

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
