if __name__=='__main__':

    for i in range(100,800):
        copy=i
        arm = 0
        while (i != 0):
            temp = i % 10
            arm = (temp * temp * temp) + arm
            i = i // 10
        #print(arm)
        if (copy == arm):
            print(arm)
