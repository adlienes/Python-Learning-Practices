print("""********************

Factoriyel Example

Press 'q'  to Exit

********************""")



while True:
	value=input("Enter Value : ")
	
	if(value=="q"):
		print("Example from Exit")
		break
	else:
		value=int(value)
		fact=1

		for i in range(2,value+1):
			fact*=i
		print("Factoriyel : ",fact)
