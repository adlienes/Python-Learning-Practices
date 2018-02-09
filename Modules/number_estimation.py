import random
import time

print("""*********

Number Estimation Game


Predict numbers from 1 to 100

************""")


number=random.randint(1,100)
tahmin_hakki=10

while True:

	tahmin=int(input("Enter Number Value : "))
	
	if(tahmin<number):
		print("Please Looding")
		time.sleep(1)

		print("Please enter a larger number")
		tahmin_hakki-=1

	elif(tahmin>number):
		print("Please Looding")
		time.sleep(1)

		print("Please enter a smaller number")
		tahmin_hakki-=1
	else:
		print("Please Looding")
		time.sleep(1)

		print("Congratulations, Our Count : ",number)
		break

	if(tahmin_hakki==0):
		print("Tahmin Hakkınız bitmiştir")
		print("Number : ",number )
		break

