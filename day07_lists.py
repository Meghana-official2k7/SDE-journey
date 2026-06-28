MY LIST:
movies=["salaar","RRR", "SVSC"]
print("My List has:", len(movies)) 

--------------------------------

APPEND,POP:
movies=["Salaar","RRR"]
print("start",movies)
movies.append("DEVARA")
print("After adding:",movies)
movies.pop()
print("After pop",movies)

--------------------------------

EVEN COUNT:
nums = [2,4,5,7,9,11]
even_count=0
for n in nums:
    if n%2==0:
        even_count= even_count +1
print("THE EVEN NUMBER:",even_count)

--------------------------------

ODD COUNT:
nums = (1,2,3,4,5,6,7,8,9,10)
odd_count=0
for n in nums:
    if n%2==1:
        odd_count= odd_count +1
print("THE ODD NUMBER:",odd_count)

--------------------------------

REVERSE NAME:
friends=["Seshma","Suma","Rojitha"]
friends.reverse()
print(friends)
