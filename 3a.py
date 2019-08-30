num=int(input("enter a number"))
li=[]
for i in range(1,num+1):
    if num%i==0:
       li.append(i)
print(li)
