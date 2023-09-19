def gcd_finder(n):
    if 0 in n:
        raise ValueError("cannot find gcd for 0")
    gcd, i = 1, 2
    while i <= max(n)//2:
        for j in n:
            if j%i != 0:
                i += 1
                break
        else:
            gcd *= i
            n = (k/i for k in n)
    return gcd
print(gcd_finder(eval(input("Enter 5 numbers, seperated by ',': "))))
