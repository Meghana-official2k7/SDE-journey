ODD OR EVEN:
num= int(input("Enter Number:"))
if num % 2 == 0:
 	print(num," is an even number")
else:
 	print(num," is an odd number")

--------------------------------

GRADE CALCULATOR:
marks = int(input("Enter Marks 0-100:"))
if marks <0 or marks >100:
	print("ERROR - marks should be in btw 0-100")
elif marks >=90:
	print("GRADE - A")
elif marks >=80:
	print("GRADE - B")
elif marks >=70:
	print("GRADE - C")
elif marks >=60:
	print("GRADE - D")
elif marks >=50:
	print("GRADE - E")
else:
	print("FAILED")

--------------------------------

LEAP OR NON LEAP YEAR:
year= int(input("Enter year:"))
 
if year % 400 ==0:
	print(year, "is a leap year")
elif year % 100== 0:
	print(year,"is not a leap year")
elif year % 4== 0:
	print(year,"is a leap year")
else:
	print(year,"is not a leap year")
