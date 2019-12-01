if __name__=='__main__':
    n=int(input("enter the value of n"))
    sum=0
    while (n!=0):
        a=n%10
        print(a)
        sum=sum+a
        n=n//10
    print(sum)
