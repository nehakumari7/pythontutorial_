if __name__=="__main__":
    name="madam"
    '''
    x=name[::-1]
    if x==name :
        print("yes it is palindrome")
    else :
        print("no it is not palindrome")
    '''
    length=len(name)
    print(length)
    rev=""
    i=length-1
    while(i>=0):
        rev=rev+name[i]
        i=i-1
    print(rev)
    if (name==rev):
        print("yes it is palindrome")
    else:
        print("no it is not palindrome")
