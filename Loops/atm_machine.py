print("""***************

Transactions

1-) Balance Questioning

2-) Depositing

3-) Withdrawal

Press 'q' to exit


********************""")


money=1000

while True:
	trans=input("Enter Transactions : ")

	if(trans=="q"):
		print("Exit from Atm")
		break;
	elif(trans=="1"):
		print("Balance Questioning {} Tl".format(money))
	elif(trans=="2"):
		depomoney=int(input("Enter Deposit Money Value : "))
		money=money+depomoney
		print("Depositing succesful")
	elif(trans=="3"):
		withmoney=int(input("Enter Withdrawal Money Value : "))

		if(money-withmoney<0):
			print("You can't Withdraw This Money")
			continue
		money=money-withmoney
		print("Withdrawal succesful")
	else:
		print("Wrong Transactions")

	


