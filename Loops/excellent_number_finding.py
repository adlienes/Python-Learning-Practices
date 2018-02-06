print("""*******

Pres "q" to exit Example

**********""")



while True:
	number=input("Enter Number Value : ")

	if(number=="q"):
		print("Example from Exit")
		break;
	else:
		number=int(number)
		sum=0

		for i in range(1,number):
			if(number%i==0):
				sum+=i
			else:
				continue

		if(sum==number):
			print("Excellent Number")
		else:
			print("Not Excellent Number")



