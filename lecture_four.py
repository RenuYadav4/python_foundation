info  = { 
    "key": "value",
    "name": "Renu",
    "age": 22,
    "is_adult": True,
    "marks": 94.4
}

print(info)


# access elements 
print(info["name"])

# reassign the value
info["name"] = "riya"

# add a new key value
info["surname"] = "yadav"

print(info)

print(info.items())   

# we can typecast it to list 
pairs = list(info.items())
print(pairs[0])

print(info.get("key"))


# print(info["name2"])   # error 
print(info.get("name2"))  # no error --> None

#  update
info.update({"age": 32})

print(info)


# set 
collection = {2,1,2,1,1,"Hello", "world", "world", 4}

print(collection)
print(len(collection))   #total number of items



