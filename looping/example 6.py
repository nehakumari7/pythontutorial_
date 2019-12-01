if __name__=='__main__':
    n=int(input("enter the value of n"))
    copy=n
    arm=0
    while(n!=0):
        temp=n%10
        arm=(temp*temp*temp)+arm
        n=n//10
    print(arm)
    if(copy==arm):
        print("yes it is amstrong")
    else:
        print("no it is not amstrong")
