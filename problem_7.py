def is_Sublist(smaller, larger):
    if smaller == [] or smaller == larger or len(smaller) == 1:
        return True
    for i in range(len(smaller)):
        for j in range(len(larger)):
            if smaller[i] == larger [j] and smaller[i + 1] == larger[j + 1]:
                return True
            return False
s = [2, 3]
l = [1, 2, 3, 4, 5]
print (is_Sublist(s,l))