print("""**************

User Login Example

*********************""")


sys_user_name="adlienes"
sys_password="123456"
login_rigt=3


while True:
	user_name=input("Enter UserName Value : ")
	password=input("Enter Password Value : ")

	if(user_name!=sys_user_name and password==sys_password):
		print("Username is incorrect")
		login_rigt-=1
	elif(user_name==sys_user_name and password!=sys_password):
		print("Password is incorrect")
		login_rigt-=1
	elif(user_name!=sys_user_name and password!=sys_password):
		print("Username and Password is incorrect")
		login_rigt-=1
	else:
		print("User Login succesful")
		break

	if(login_rigt==0):
		print("Login Rigt End")
		break

