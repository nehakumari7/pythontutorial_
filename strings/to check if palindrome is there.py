if __name__=="__main__":
    name="testst"
    ans=name
    length=len(name)
    print(length)
    i=0
    while(i<length):
        for j in range(i+1,length):
            if(name[i]==name[j]):
                ans=ans.replace(ans[i],"0",2)
                print(ans)
                break
        i=i+1
    k=len(ans)-1
    m=0
    while k>=0 :
        if (ans[k]!="0") :
            m=m+1
        k=k-1

    if (m==0 or m==1) :
        print("yes")
    else:
        print("no")



