class calcarea:
    def area(self,x,y=None):
        if y is not None:
            print(x*y)
        else:
            print(x*x)


c1=calcarea()
c1.area(5)
c2=calcarea()
c2.area(5,8)

#overloading:same name bbut different in characteristics(have different parameters in functions)
#overriding:same name and same in characteritics

