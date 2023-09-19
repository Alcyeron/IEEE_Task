def bal(s1, s2):
    for i in s1:
        if i not in s2:
            print('not balanced')
            break
    else:
        print('balanced')
s1 = input('enter string 1: ')
s2 = input('enter string 2: ')
bal(s1, s2)