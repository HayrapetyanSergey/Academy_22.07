def palindroms(str):
    for i in range(len(str)):
        if str[-1 - i] == str[i]:
           return "Is palindroms"
        else:
            return False


string = str(input())
print (palindroms(string))