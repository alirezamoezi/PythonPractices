def strobog(x):
    answer = func(x, x)
    return answer

def func(x, length):
    if (x == 0):
        return [""]
    if (x == 1):
        return ["1", "0", "8"]
    middle = func(x-2, length)
    r = []
    for m in middle:
        if (x != length):
            r.append("0" + m + "0")
        r.append("8" + m + "8")
        r.append("9" + m + "6")
        r.append("6" + m + "9")
    return r

print("For 2: ", strobog(2))
print("For 3: ", strobog(3))
print("For 4: ", strobog(4))