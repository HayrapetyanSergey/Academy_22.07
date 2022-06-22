def is_perfect(a):
    sum = 0
    for i in range(1,a):
        if a % i == 0:
            sum += i

    if sum == a:
        return True
    return False

print (is_perfect(24))                
