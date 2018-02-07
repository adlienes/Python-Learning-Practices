print("""**********

	Prime Number Example

	Press "q" to Exit
************""")

def isPrime(number):
	if(number==1):
		return False
	elif(number==2):
		return True
	else:
		for i in range(2,number):
			if(number%i==0):
				return False
			else:
				return True


while True:
	a=input("Enter Value Number : ")

	if(a=="q"):
		break
	else:
		a=int(a)

		if(isPrime(a)):
			print("Number is Prime Number")
		else:
			print("Number isn't Prime Number")