def number_gen():
    for i in range(5):
        yield (i)

for x in number_gen():
    print (x)

#return will not go back to function once it came out
#yeild will be able to get values from function which is incrementally done