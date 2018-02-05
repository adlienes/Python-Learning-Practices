
shapetype=input("Enter Shape Type Value(Dortgen-Ucgen) : ")


if(shapetype=="Dortgen"):
	x1=int(input("Enter X1 : "))
	x2=int(input("Enter X2 : "))
	x3=int(input("Enter X3 : "))
	x4=int(input("Enter X4 : "))

	if(x1==x2 and x1==x3 and x1==x4):
		print("Kare")
	elif(x1==x3 and x2==x4):
		print("Dikgörtgen")
	else:
		print("Dortgen")

elif(shapetype=="Ucgen"):
	a1=int(input("Enter A1 : "))
	a2=int(input("Enter A2 : "))
	a3=int(input("Enter A3 : "))

	if(a1==a2 and a1==a3):
		print("Eşkenar")
	elif((a1 == a2 and a1 != a3) or (a1 == a3 and a1 != a2) or (a2 == a3 and a2 != a1)):
		print("İkizkenar")
	else:
		print("Normal ücgen")
else:
	print("Yanlış seçim")


