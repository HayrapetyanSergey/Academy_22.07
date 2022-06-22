def oneword(list:list):
    list1 = [None] * len(list)
    for i in range(len(list)):
    
            list1[i] = list[i]
    return list1



data = list(input("word is" ))
print (oneword(data))