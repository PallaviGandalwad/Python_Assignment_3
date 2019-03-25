#4.Write a program which accept N numbers from user and store it into List. Accept one another
#number from user and return frequency of that number from List.
#Input : Number of elements : 11
#Input Elements : 13 5 45 7 4 56 5 34 2 5 65
#Element to search : 5
#Output : 3

arr=list()

num=input("Enter how many element you want:")

print("Enter the number in list:")

for i in range(0,int(num)):
	no=input("num:")
	arr.append(int(no))
	

print("Inserted element in the List:",arr)

#print("enter the element tobe search",input((num)))
no1=input("Eneter the element to find the frequency ->")
#print("Enter the element",no1)
frequency=arr.count(int(no1))
print("Frequency of element " ,no1, "is->",frequency)








