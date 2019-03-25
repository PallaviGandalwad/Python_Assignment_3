#4.Write a program which accept N numbers from user and store it into List. Accept one another
#number from user and return frequency of that number from List.
#Input : Number of elements : 11
#Input Elements : 13 5 45 7 4 56 5 34 2 5 65
#Element to search : 5
#Output : 3

arr=list()

num=input("Enter how many element you want:")

print("Enter the number in list:")

def Freq(arr,no1):
	count1 = 0
	for i in arr:
		if (i == no1):
			count1=count1+1
	return count1

for i in range(0,int(num)):
	no=input("num:")
	arr.append(int(no))
	#arr.sort()

print("Inserted element in the List:",arr)

#print("enter the element tobe search",input((num)))

#print("Enter the element",no1)
no1=input("Eneter the element to find the frequency ->")

ret=Freq(arr,no1)
print("frequency of element ",no1,"is->",ret)







