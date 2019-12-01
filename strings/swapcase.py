if __name__=="__main__":
    name="This is Neha"
    change=name.swapcase()
    print(change)

    r=""
    i=0
    while(i<=len(name)-1) :
        if name[i].islower():
            r=r+name[i].upper()
        else :
            r=r+name[i].lower()
        i=i+1

    print(r)