

weight=int(input("Enter Weight(kg) Value : "))
size=float(input("Enter Size(m) Value : "))

index=weight/(size*size)

print("Body Mase İndex : ",index)


if(index<18.5):
	print("Weak")
elif(index>=18.5 and index<25):
	print("Normal")
elif(index>=25 and index<30):
	print("Overweight")
elif(index>30):
	print("Obese")