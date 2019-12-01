dict={"name":"neha",1:5,"city":44.5}
print(dict)

print(dict["name"])
print(dict[1])

dict["ofc"]="tcs"
print(dict)

dict.pop(1)

for k in dict.keys():
    print(dict[k])
    print(dict.get(k))

#for k in dict.values():
   # print(dict[k])