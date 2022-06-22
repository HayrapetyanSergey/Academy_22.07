from types import TracebackType


def is_sorted(data):
    max = data[0]
    for i in range(1, len(data)):
        if data[i] > max :
            max = data[i]

    if max == data[0]:
        return "Is sorted"
    elif max == data[-1]:
        return "Is sorted, too"
    elif max != data[0] or max != data[-1]:
        return False

data = list(input())
print (is_sorted(data))