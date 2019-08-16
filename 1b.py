def fib(n):
 if n in [0,1]:
  return 1
 else:
  return(fib(n-1)+fib(n-2))
number=int(input("enter the number"))
for i in range(number):
 print(fib(i))

     

