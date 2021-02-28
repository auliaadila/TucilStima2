#MAKE DICTIONARY
#Fungsi untuk membuat dictionary graf dari 
#  masukan teks yang diterima pertama kali
#Key: mata kuliah (unik); 
#Value: mata kuliah prasyarat terkait
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
#Fungsi untuk membuat dictionary 
#   count mata kuliah prasyarat
#Key: mata kuliah (unik); 
#Value: jumlah mata kuliah prasyarat
def count(dict):
    dict_c = dict.copy()
    for k in dict_c:
        dict_c[k] = len(dict.get(k))
    return dict_c

#SELECT KEY TO BE DELETED
#Fungsi untuk menghapus mata kuliah yang 
#   tidak memiliki mata kuliah prasyarat
#Akan mengembalikan dictionary graf yang baru 
# serta array berisi list mata kuliah yang 
# di delete (memiliki nol prasyarat)
def delkey (dict1,dict_c):
    eachsem = []
    for k in dict_c:
        if dict_c.get(k) == 0:
            delete = k
            eachsem.append(delete)
            dict1.pop(delete)

            for v in iter(dict1.values()):
                for element in v: 
                    if element == delete:
                        v.remove(element)

    count(dict1)
    dict_c.clear() #works!
    return dict1,eachsem

#UPDATE THE PRINT
#Membentuk dictionary dari array 
# list mata kuliah dengan nol prasyarat
def update(idx,value):
    prereq = {}
    key = "Semester " + str(idx)
    prereq[key] = value
    return prereq

#PRINT DICTIONARY
#Print dictionary sesuai output yang diinginkan 
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
        
#USER INTERACTION
def welcome():
    name = input("Hallo, what's your name? ")
    yesno = input("Do you have any trouble in defining your subjects prerequisites? (Y/N) ")
    printname = name+","
    
    return yesno,printname


#MAIN
yesno = welcome()

if ((yesno[0] == "Y") or (yesno[0] == "y")):
    print("Well",yesno[1],"I'm here to help you!","\n")
    #Meminta masukan file teks
    file = input("Insert your list of subjects in filename.txt format : ")
    print("\n")

    f = open("../test/"+file, "r")
    dict = makedict(f)

    print("=============",yesno[1][:-1].upper()+"'S","LIST OF SUBJECTS =============","\n")

    emptydict = {}
    prereq = {}
    idx = 1

    #Iterasi hingga dictionary graf awal menjadi empty ( {} )
    while dict != emptydict:
        dict_c = count(dict)
        new = delkey(dict,dict_c)
        updating = update(idx,new[1])
        prereq.update(updating)
        idx += 1

    printd(prereq)

else:
    print("Good then! See u next time!!")