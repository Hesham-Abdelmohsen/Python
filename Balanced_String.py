

str = input()

lst = []
temp = []
counter = 0

if len(str)%2 == 0:
    for i in range(len(str)):
        lst.append(ord(str[i]))

    for i in range(len(lst)):
        if counter == len(lst):
            print('true')
            exit()

        if i in temp:
            continue

        if (lst[i]+1) in lst[i+1:]:
            temp.append(lst.index((lst[i]+1)))
            lst[lst.index((lst[i]+1))] = 0
            counter += 2

        elif  (lst[i]+2) in lst[i+1:]:
            temp.append(lst.index((lst[i] + 2)))
            lst[lst.index((lst[i] + 2))] = 0
            counter += 2

        else:
            break

print('false')

