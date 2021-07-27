print("Enter the marks")
marks=float(input())
if(marks<30):
	print("Fail")
elif(marks>30 and marks<60):
	print("B")
elif(marks>60 and marks<80):
	print("A")
else:
	print("A+")