class student():
    name=""
    roll_no=0
    city=""
#static function can access only static menbers
#non static function can access static members also
    @staticmethod
    def setvalue(n,r):
        student.name=n
        student.roll_no=r
    @staticmethod
    def display():
        print(student.name,student.roll_no)

student.setvalue("neha",1)
student.setvalue("vivek",2)
student.display()
student.display()