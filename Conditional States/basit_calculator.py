print("""********************

İşlemler

1-) Toplama İşlemi
2-) Çıkarma İşlemi
3-) Çarpma İşlemi
4-) Bölme İşlemi


***********************	""")


a=int(input("Enter A Value : "))
b=int(input("Enter B Value : "))

islem=input("İşlem Giriniz : ")


if(islem=="1"):
	print("A+B : ",a+b)
elif(islem=="2"):
	print("A-B : ",a-b)
elif(islem=="3"):
	print("A*B : ",a*b)
elif(islem==4):
	print("A/B : ",a/b)
else:
	print("Geçersiz İşlem Girdiniz")		