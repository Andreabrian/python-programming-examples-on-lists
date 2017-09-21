#find the largest number in the list.
a=[]
n=int(input("Enter the number of elements:"))
 
for i in range(n):
    a.append(int(input("enter new element:")))
    print(a)    
s=a[0]
for i in range(1,len(a)):
    if a[i]>s:
        s=a[i]
        y=("the largest number is: ")
        print(y,s)

