class student():
   def __init__(self):
     self.id=None
     self.marks=None
     self.age=None
   
   def setdata(self,studentid,marks,age):
      self.id=studentid;
      self.marks=marks;
      self.age=age;
  
   def validate_marks(self):
       if self.marks<0 and self.marks>100:
           return False
       else:
           return True

   def validate_age(self):
      if self.age<=20:
        return False
      else:
         return True

   def check_qualification(self):
      if self.validate_age() and self.validate_marks():
         if self.marks>=65:
           return True
         else:
           return False
    
   def getdata(self):
      print(self.id)
      print(self.marks)
      print(self.age)

n=int (input("enter no of students"))
x=[]
for i in range (n):
  print("enter details")
  x.append(student())
  id=int(input("enter the id"))
  marks=int(input("enter marks:"))
  age=int(input("enter age:"))
  x[i].setdata(id,marks,age)
for i in range (n):
 if x[i].check_qualification():
   x[i].getdata()
 else:
   print("not qualified") 


        
