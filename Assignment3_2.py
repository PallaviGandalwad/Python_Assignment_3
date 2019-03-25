
#2.Write a program which accept N numbers from user and store it into List. Return Maximum
#number from that List.
#print("Input : Number of elements : 7")
#print("Input Elements : 13 5 45 7 4 56 34")
#print("Output : 56")
arr = list()
# Ask the user about the number of elements
num = input("Enter how many elements you want:")
print ("Enter numbers in array: ")
# Iterate the for loop to accept N numbers
for i in range(0,int(num)):
# Accept individual element from user
	no = input("num :")
# Insert that element into List
	arr.append(int(no))
	#arr.sort(int(no))
print ("Entered elements are",arr)

def Maximum(arr):
		max=0
		i=0
		for i in arr:
			if i >= max:
				max=i
		return max
#print("Maximum value from the List->",max) 
ret=Maximum(arr)
print("Maximum value from the List->",ret)
