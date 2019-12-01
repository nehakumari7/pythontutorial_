def sum(n):
    sum=0
    while(n!=0):
        temp=n%10
        sum=sum+temp
        n=n//10
    return sum

def length(n):
    l=0
    while(n!=0):
        l=l+1
        n=n//10
    return l

num=1234
while(length(num)!=1):
    num=sum(num)

print(num)