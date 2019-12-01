if __name__=='__main__':
    age=input("please enter age group")
    if age >= "18":
        pan=input("please enter pan status(yes/no")
        if pan=="yes":
            print("eligible")
        else:
            print("apply")

    else:
        print("not eligible")
