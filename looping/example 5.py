if __name__=='__main__':
   ''' n=int(input("enter the value of n"))
    b=n
    pali=""
    while(n!=0):
        a=n%10
        pali=pali + str(a)
        n=n//10
    print(pali)
    if pali==str(b):
        print("palindrome")
    else:
        print("not palindrome")
    '''
   n=int(input("enter the value of n"))
   rev=0
   copy=n
   while(n!=0):
       temp=n%10
       rev=(rev*10)+temp
       n=n//10
   print(rev)
   if(rev==copy):
       print("yes palindrome")
   else:
        print("not plaindrome")
