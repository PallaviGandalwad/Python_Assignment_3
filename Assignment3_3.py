#3.Write a program which accept N numbers from user and store it into List. Return Minimum
#number from that List.
#Input : Number of elements : 4
#Input Elements : 13 5 45 7
#Output : 5
arr=list()

num =input("Enter how many element you want:")
print("Enter number in Array:")

for i in range(0,int(num)):
 	no=input("num:")
 	arr.append(int(no))
print("Inserted Elements are",arr)

 
Minimun=min(arr)

print("Minimun Number from the list is->",Minimun)