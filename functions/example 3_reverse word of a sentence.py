def reverse(n):
    return n[::-1]
#this is neha
sentence="this is neha"
wordlist=sentence.split(" ")
result= ""
for word in wordlist:
    result=result+ " " + reverse(word)
print(result)