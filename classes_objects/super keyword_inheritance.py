class parent():
    def __init__(self):
        print("this is parent constructor")
    def display(self):
        print("this is parent")
class child(parent):
    def __init__(self):
        super().__init__()#super keyword to call constructor of immediate parent
        print("this is child constructor")
    def display1(self):
        print("this is child")

c=child()
c.display()