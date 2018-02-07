print("""*********

Number Full Factor

Press "q" to Exit

**********""")

def full_factor(number):
	full_factor_list=[]

	for i in range(1,number+1):
		if(number%i==0):
			full_factor_list.append(i)

	return full_factor_list


while True:
	a=input("Enter Number Value : ")

	if(a=="q"):
		break
	else:
		a=int(a)
		print("Full Factor List : ",full_factor(a))