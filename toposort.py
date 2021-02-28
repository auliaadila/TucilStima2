#READ FILE  
file = input("Insert your file (in filename.txt format) : ")
f = open(file, "r")

#MAKE DICTIONARY
dict = {}
for line in f:
    i = 0
    for word in line.split():
        i += 1
        if (i==1):
            key = word
            dict[key] = []
        else:
            dict[key].append(word)
print("ORIGINAL DICT")
print(dict)


#dict_c = dict.copy()

#COUNT VALUE PER KEYS
def count(dict):
    dict_c = dict.copy()
    for k in dict_c:
        dict_c[k] = len(dict.get(k))

    return dict_c
#print(dict_c)

#SELECT KEY TO BE DELETED
def delkey (dict1,dict_c):
    for k in dict_c:
        if dict_c.get(k) == 0:
            delete = k
            dict1.pop(delete)

            for v in iter(dict1.values()):
                for v1 in v: 
                    if v1 == delete:
                        v.remove(v1)
    print("NEW:")
    dict_c.clear() #works!
    return dict1

#FUNCTION TEST

dict_c = count(dict)
new = delkey (dict,dict_c)

print(new)
print(count(new))


#ITERATE UNTIL EMPTY DICT

emptydict = {}

while dict != emptydict:
    dict_c = count(dict)
    new = delkey (dict,dict_c)

    print(new)
    print(count(new))
    

#MAIN