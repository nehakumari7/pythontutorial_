class parent1():
    def display(self):
        print("this is parent1")

class parent2():
    def display(self):
        print("this is parent2")

class child(parent1,parent2):#parent1 will be called since it is declared first\
    def display1(self):
        print("this is child")

c=child()
c.display()

#single inheriantance
#multiple level inheriantance
#hiearchical inheritance
#mutiple inheritance(this is supported only in python)
#hybrid inheritance