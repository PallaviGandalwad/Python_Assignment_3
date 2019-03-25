def count(brr,search):
	count=0;
	for i in brr:
		if(i==search):
			count+=1;
	return count;
	
	
arr= list();

N=input("Enter Number of elements in the array: ");

print("Enter elements in the array");

for i in range(0,int(N)):
	element=input("Element : ");
	arr.append(int(element));
	
search=input("Element to search : ");

ret=count(arr,search);
print(ret);