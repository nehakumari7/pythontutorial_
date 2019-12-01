def neha():
    print("hello")
neha()

def add(a,b):
    c=a+b
    print(c)

add(1,2.2)

def total(m1,m2,m3,m4,m5):
    total=m1+m2+m3+m4+m5
    return total

t=total(1,2,3,4,5)
print(t)

def total_1(m1,m2=0,m3=0):
    total_1=m1+m2+m3
    return(total_1)

t_1=total_1(1,2)
print(t_1)

#default parameter can be defined
#if one is default parameter then subsequent parameter should also be default parameter

t_1=total_1(1,m2=3,m3=6)
print(t_1)
