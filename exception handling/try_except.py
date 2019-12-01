li=[1,2,3]
index=int(input("enter the index"))
try:
    print(li[index])
    raise ArithmeticError
except IndexError as err:
    print(err)
except Exception as err:
    print(err)
finally:
    print("this is neha")

#we can have multiple except in try block
#try block for handling exception handling
#Exception is super calss of all exceptions
#we can try block without except or finally block consider that atleast except or finally block is there
#finally keyword that will excute for sure
# Class will start with Capital letter