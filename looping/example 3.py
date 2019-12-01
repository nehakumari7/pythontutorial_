if __name__=='__main__':
    n=int(input("enter the value of n"))
    i=1
    sum=0
    while i<=n:
        if i%2==0:
            sum=sum+i
        i=i+1
    print(sum)
