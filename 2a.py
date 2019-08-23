def fun(li,num):
 if num in li:
  return 1
 else:
  return 0
li=[1,2,3,4,5,6]
num=int(input("enter a number to be searched"))
ans=fun(li,num)
if ans==1:
  print("number is present")
else:
  print("number is not present")

