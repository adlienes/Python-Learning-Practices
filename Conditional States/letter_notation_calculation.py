

exam1=int(input("Enter Exam 1 Note Value : "))
exam2=int(input("Enter Exam 2 Note Value : "))
final=int(input("Enter Final Note Value : "))


sum_note=(exam1*(3/10))+(exam2*(3/10))+(final*(4/10))

print("Note Avarage : ",sum_note)

if(sum_note<55):
	print("Letter Note : FF")
elif(sum_note>=55 and sum_note<60):
	print("Letter Note : FD")
elif(sum_note>=60 and sum_note<65):
	print("Letter Note : DD")
elif(sum_note>=65 and sum_note<70):
	print("Letter Note : DC")
elif(sum_note>=70 and sum_note<75):
	print("Letter Note : CB")
elif(sum_note>=75 and sum_note<80):
	print("Letter Note : BB")
elif(sum_note>=80 and sum_note<85):
	print("Letter Note : BA")
elif(sum_note>=85):
	print("Letter Note : AA")