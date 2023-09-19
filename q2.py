def spiral(n):
    def indexer(size, shift):
        return(4*size - 4 + shift)  #4*size - 4 + shift - 1
    #indexer(prev. size - 2, prev. index)
    def printf(n, end = '\n', reverse = False):
        if len(str(n)) == 1:
            if reverse:
               print(' ' + str(n), end = end)
            else:
                print(str(n) + ' ', end = end)
        else:
            print(n, end = end)
    l, s, l1 = [], 0, []
    k = -1
    for j in range(1, n):
        printf(j, end = '')
    printf(n, reverse = True)
    for i in range(1, n):
        #print('#'*i)
        for i1 in range(0, len(l)):
            #print(l)
            printf(l[i1] - i + i1 + 1, end = '')
        if i <= n//2:
            s = indexer(n + 2 - 2*i, s)
            printf(s, end = '')
            if i != n//2 or n%2 != 0:
                l.append(s)
                k += 1
            s1 = l[k] - i + k + 1
        elif i >= n//2 + 1:
            s1 = l[k] - i + k + 1
            if len(l) != 0:
                del l[-1]
                k -= 1
        #s2 = s
        for i2 in range(1, n - 2*i + 1):
            s1 += 1
            printf(s1, end = '')
        for i3 in range(1, 2*i + 1 -n):
            s1 -= 1
            printf(s1, end = '')
        for i4 in range(len(l1), 0, -1):
            printf(l1[i4 - 1] + i - i4, end = '')
        if i <= n//2:
            if i != n//2:
                l1.append(s1)
            elif n%2 != 0:
                ...
            else:
                del l1[-1]
        elif i > n//2:
            if len(l1) != 0:
                del l1[-1]
        printf(i + n, reverse = True)
spiral(int(input('enter no.:')))

