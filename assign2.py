#Swap the First and Last Value of a List.
a=[]
n=int(input("Enter the number of elements:"))
 
for i in range(n):
    a.append(int(input("enter new element:")))
    print("the list is:")
    print(a)
temp=a[n-1]
a[n-1]=a[0]
a[0]=temp
print("the new list is:")
print(a)


