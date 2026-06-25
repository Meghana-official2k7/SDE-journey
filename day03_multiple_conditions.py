VOTE CHECKER:
Age =int(input("your Age="))



if  Age  >=  18 :	
           print("Eligible for vote")
else :	
           print( "not eligible")


ODD OR EVEN:
Number = int(input("Number= "))
if Number  % 2 == 0 :
    print("Even")
else :
	print("odd")


PASS OR FAIL:
Marks = int(input("Marks obtained="))
if Marks >= 35:
	print("passed")
else:
	print("failed")


GREATER NUMBER:
a = int(input("number1="))
b = int(input("number2:"))
if a > b :
	print("number1 Greater than number2")
elif a == b :
	print("both are equal")
else:
	print("number1 lesser than number2")


DREAM PACKAGE:
a = int(input("Dream package in lpa:"))
if a>=50:
	print("Google/Microsoft")
elif a>=30:
	print("Amazon/Wipro")
else :
	print("First step- keep grinding")


JOB ELIGIBILITY1:
age = int(input("Enter age="))
exp = int(input("enter experience in years="))
if age >=20 and age <40 and exp>=2:
	print("Eligible")

else:
	print("Not Eligible - Keep Grinding")


JOB ELIGIBILITY2 WITH REASON:
age = int(input("Age ="))
exp = int(input("experience in years= "))
if age<20:
	print("Not Eligible-20+age Needed")
elif age>=40:
	print("Not Eligible-under 40age Needed")
elif exp<2:
	print("Not Eligible-2+Exp Needed")
else:
	print("Eligible-you can Apply")
