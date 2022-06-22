def average(data):
    list1 = []
    list2 = []
    list3 = []
    res = sum(data) / len(data)
   
    for i in range(len(data)):
        if data[i] < res:
            list1.append(data[i])
        elif data[i] > res:
            list2.append(data[i])
        else:
            list3.append(data[i])
    return (f"this is average {res}", f"numbers < average {list1}")


data = list(input())
print(average(data))