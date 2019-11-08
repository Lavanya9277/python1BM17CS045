from tkinter import *
class Tapp(Frame):
	def __init__(self,master):
		super(Tapp,self).__init__(master)
		self.grid()
		self.wid()
	def wid(self):
		Label(self,text="Movie Booking").grid(row=0,column=0,columnspan=10,sticky="W")
		Label(self,text="Select Any One").grid(row=1,column=0,columnspan=10,sticky="W")
		self.mov=StringVar()
		self.mov.set(None)
		Radiobutton(self,text="Kannada",variable=self.mov,value="Kannada",command=self.kan).grid(row=2,column=0,columnspan=8,sticky="W")
		Radiobutton(self,text="Hindi",variable=self.mov,value="Hindi",command=self.hin).grid(row=2,column=3,columnspan=8,sticky="W")
		Radiobutton(self,text="English",variable=self.mov,value="English",command=self.eng).grid(row=2,column=5,columnspan=8,sticky="W")
		Button(self,text="Book Ticket", command=self.book).grid(row=7,column=0,columnspan=2, sticky="W")
		self.txt=Text(self, width=40, height=5,wrap=WORD)
		self.txt.grid(row=8,column=0, columnspan=8,sticky="W")
	def kan(self):
		self.l4=Label(self,text="Jaguar")
		self.l4.grid(row=3,column=0,sticky="W")
		self.kan1=BooleanVar()
		Checkbutton(self,variable=self.kan1).grid(row=3,column=1,sticky="W")
		self.l5=Label(self,text="U Turn")
		self.l5.grid(row=3,column=2,sticky="W")
		self.kan2=BooleanVar()
		Checkbutton(self,variable=self.kan2).grid(row=3,column=3,sticky="W")
		self.l6=Label(self,text="Milana")
		self.l6.grid(row=3,column=4,sticky="W")
		self.kan3=BooleanVar()
		Checkbutton(self,variable=self.kan3).grid(row=3,column=5,sticky="W")
	def hin(self):
		self.l7=Label(self,text="Kushi")
		self.l7.grid(row=3,column=0,sticky="W")
		self.h1=BooleanVar()
		Checkbutton(self,variable=self.h1).grid(row=3,column=1,sticky="W")
		self.l8=Label(self,text="Shivaay")
		self.l8.grid(row=3,column=2,sticky="W")
		self.h2=BooleanVar()
		Checkbutton(self,variable=self.h2).grid(row=3,column=3,sticky="W")
		self.l9=Label(self,text="Sultan")
		self.l9.grid(row=3,column=4,sticky="W")
		self.h3=BooleanVar()
		Checkbutton(self,variable=self.h3).grid(row=3,column=5,sticky="W")
	def eng(self):
		self.l10=Label(self,text="Matrix")
		self.l10.grid(row=3,column=0,sticky="W")
		self.e1=BooleanVar()
		Checkbutton(self,variable=self.e1).grid(row=3,column=1,sticky="W")
		self.l11=Label(self,text="Universe")
		self.l11.grid(row=3,column=2,sticky="W")
		self.e2=BooleanVar()
		Checkbutton(self,variable=self.e2).grid(row=3,column=3,sticky="W")
		self.l9=Label(self,text="Mind")
		self.l9.grid(row=3,column=4,sticky="W")
		self.e3=BooleanVar()
		Checkbutton(self,variable=self.e3).grid(row=3,column=5,sticky="W")
	def book(self):
		msg=""
		if self.mov.get()=="Kannada":
			if self.kan1.get():
				msg="You Booked for Jaguar was successful"
			elif self.kan2.get():
				msg="You Booked for U Turn was successful"
			elif self.kan3.get():
				msg="You Booked for Milana was successful"
			else:
				msg="Please select the Movie"
		elif self.mov.get()=="Hindi":
			if self.h1.get():
				msg="You Booked for Kushi was successful"
			elif self.h2.get():
				msg="You Booked for Shivaay was successful"
			elif self.h3.get():
				msg="You Booked for Sultan was successful"
			else:
				msg="Please select the Movie"
		elif self.mov.get()=="English":
			if self.e1.get():
				msg="You Booked for Matrix was successful"
			elif self.e2.get():
				msg="You Booked for Universe was successful"
			elif self.e3.get():
				msg="You Booked for Mind was successful"
			else:
				msg="Please select the Movie"
		self.txt.delete(0.0,END)
		self.txt.insert(0.0,msg)
r=Tk()
r.title("Movie Ticket")
a=Tapp(r)
r.mainloop()
