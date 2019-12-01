class parent():
    def __display(self):#_ is used to make it private but we can able to use,__ is used to make it strongly private that means we cannot use outside the class
        print("this is neha")

class child(parent):
    def display1(self):
        print("this is neha1")

c=child()
c.__display()

#python doesnt support protected
