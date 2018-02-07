print("""*************

	Number Reading Example

	Press "q" to Exit
 
**************""")

birler=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
onlar=["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]

def number_reading(number):
	
	birinci=number%10
	ikinci=number//10

	return onlar[ikinci]+ " " + birler[birinci]


while True:
	a=input("Enter Value Number : ")

	if(a=="q"):
		break
	else:
		a=int(a)
		print(number_reading(a))