def factorial(n):
	if(n==0):
		return 1
	else:
		return n*factorial(n-1)


def e_cuadratica(n):
	i=0
	resp=0
	while(i<n):
		resp+=(1/factorial(i))
		i+=1
	return resp
#print(e_cuadratica(100))


def e_lineal(n):
	fact=1
	i=1
	resp=0
	while(i<=n):
		fact=fact*i
		resp+=(1/fact)
		i+=1
	return resp+1

#print(e_lineal(100000))
