PRINT 1 TO n:
for i in range(1,101):
    print(i)

 --------------------------------
   
PRINT IN REVERSE:
for i in range(   100,0,-1):
	print( i)

--------------------------------

ODD/EVEN:
even = 0
odd = 0
 
for i in range(1,51):
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
        
print("Even =", even, "Odd =", odd)  

--------------------------------

MATH TABLES:
n = int(input("Enter Table number:"))
for i in range(1,21):
	print(n,"x",i,"=",n*i)

--------------------------------

SUM OF DIGITS:
n = int(input("Enter number: "))
sum = 0

while n > 0:
    digit = n % 10        
    sum = sum + digit     
    n = n // 10           
    
print("Sum =", sum)

--------------------------------

FACTORIALS:
n =int(input("Enter Number:"))
fact = 1
for i in range(1,n+1):
	fact=fact*i
	
print("factorial:",fact)

--------------------------------

FACTORIALS 2:
n = int(input("Enter Number: "))

if n < 0:
    print("Sorry - there is no factorial for negative numbers")
elif n == 0:
    print("factorial: 1")
else:
    fact = 1                    
    for i in range(1, n+1):       
        fact = fact * i         
    print("factorial:", fact)   

--------------------------------

STAR PATTERN 1:
n= int(input("enter number of rows:"))
for i in range(n):
	for j in range(n):
		print("*" ,end=" ")
	print( )

--------------------------------

STAR PATTERN 2(RT):
n= int(input("enter number of rows:"))
for i in range(n):
	for j in range(i+1):
		print("*" ,end=" ")
	print( )

--------------------------------

STAR PATTERN 3(PYRAMID):
n= int(input("enter number of rows:"))
for i in range(n):
	for k in range(n-1-i):
		print(" ",end=" ")
	
	for j in range(i+1):
		print(" * " ,end=" ")
	print( )

--------------------------------

STAR PATTERN 4(LT):
n = int(input("enter number of rows: "))

for i in range(n):
    for k in range(n-1-i):
        print("      ", end="")     
    
    for j in range(i+1):
        print("    * ", end="")    
    
    print()

--------------------------------

PRIME NUMBER:
num = int(input("Enter number:"))
is_prime = True

if num<=1:
	is_prime = False
else:
	for i in range(2,num):
		if num % i==0:
			is_prime= False
			break
	    	
if is_prime:
	print(num,"is a prime number")
else:
	print(num,"not a prime number")

--------------------------------

FIBONACCI:
	n = int(input("Enter Number :"))
a=0
b=1
if n <= 0:
	print("NOTHING")
elif n == 1:
	print(a)
elif n == 2:
	print(a,b)
else:
    print(a,b,end=" ")
    for i in range(2,n):
        	c=a+b
        	print(c,end=" ")
        	a=b
        	b=c

