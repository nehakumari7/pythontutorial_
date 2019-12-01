class student:
    name=""
    roll=0
    def __init__(self,n,r):
        self.name=n
        self.roll=r
    def display(self):
        print(self.name,self.roll)
    def __del__(self):
        print("destructor")

s1=student("neha",1)
s2=student("vivek",3)
s1.display()
s2.display()

#constructor will be called whenever object is created
#destructor will be called when we are done with program