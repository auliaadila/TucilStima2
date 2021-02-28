#MAKE DICTIONARY
def makedict(f):
    dict = {}
    for line in f:
        i = 0
        for word in line.split():
            word1 = word.rstrip(",.")
            i += 1
            if (i==1):
                key = word1
                dict[key] = []
            else:
                dict[key].append(word1)
    return dict

#COUNT VALUE PER KEYS
def count(dict):
    dict_c = dict.copy()
    for k in dict_c:
        dict_c[k] = len(dict.get(k))
    return dict_c

#SELECT KEY TO BE DELETED
def delkey (dict1,dict_c):
    eachsem = []
    for k in dict_c:
        if dict_c.get(k) == 0:
            delete = k
            eachsem.append(delete)
            dict1.pop(delete)

            for v in iter(dict1.values()):
                for v1 in v: 
                    if v1 == delete:
                        v.remove(v1)

    count(dict1)
    dict_c.clear() #works!
    return dict1,eachsem

#UPDATE THE PRINT
def update(idx,value):
    prereq = {}
    key = "Semester " + str(idx)
    prereq[key] = value
    return prereq

#PRINT DICTIONARY
def printd(dict):
    for k,v in dict.items():
        print(k,"  : ",end="")
        count = 0
        for item in v:
            print(item,end="")
            count += 1
            if count != len(v):
                print(", ",end="")
        print("\n")
        
#ITERATE UNTIL EMPTY DICT
def welcome():
    name = input("Hallo, what's your name? ")
    yesno = input("Do you have any trouble in defining your subjects prerequisites? (Y/N) ")
    printname = name+","
    
    return yesno,printname


#MAIN
yesno = welcome()

if (yesno[0] == "Y" or "y"):
    print("Well",yesno[1],"I'm here to help you!","\n")
    file = input("Insert your list of subjects in filename.txt format : ")
    print("\n")

    f = open(file, "r")
    dict = makedict(f)

    print("=============",yesno[1][:-1].upper()+"'S","LIST OF SUBJECTS =============","\n")

    emptydict = {}
    prereq = {}
    idx = 1

    while dict != emptydict:
        dict_c = count(dict)
        new = delkey(dict,dict_c)
        updating = update(idx,new[1])
        prereq.update(updating)
        idx += 1

    printd(prereq)

else:
    print("Good then! See u next time!!")
