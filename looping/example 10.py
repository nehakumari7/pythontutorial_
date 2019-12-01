if __name__=='__main__':
    for i in range(6):
        for j in range(5,i,-1):
            print(" ",end =' ')
        for k in range(i+2):
            if k>0 :
                print(k,end =" ")
        for j in range(i+1):
            if j>0:
                print(j,end =" ")
        print()

