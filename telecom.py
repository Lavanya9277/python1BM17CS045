class CallDetail:
   def __init__(self,calling,called,duration,type):
      self.calling=calling
      self.called=called
      self.duration=duration
      self.type=type

  
class Util:
  def __init__(self):
    self.list_of_call_objects=None

  def parse_customer(self,list_of_call_string):
     self.list_of_call_string=list_of_call_string
     self.call_details=[]
     for x in self.list_of_call_string:
       x=x.split(",")
       self.call_details.append(CallDetail(x[0],x[1],x[2],x[3]))

  def print_details(self):
     print("details:")
     for call in self.call_details:
        print("caller:"+call.calling,"\n","Receiver:",call.called,"\n","Duration:",call.duration,"\n","type:",call.type) 
call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'
list_of_call_string=[call,call2,call3]
u=Util()
u.parse_customer(list_of_call_string)
u.print_details()
