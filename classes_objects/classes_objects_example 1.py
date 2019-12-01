#property->data members->variables
#behaviuor->member functions->functions

#self to access variables inside a class using functions
#to access variables outside calss we have to create objects

class student:
    name=""
    roll_no=0
    def display(self):
        print(self.name,self.roll_no)

s1=student()
s2=student()
s1.name="neha"
s1.roll_no=1
s2.name="vivek"
s2.roll_no=2
s1.display()
s2.display()