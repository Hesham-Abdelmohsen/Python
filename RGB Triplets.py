input()
str = input()
lst_R = []
lst_G = []
lst_B = []
ans = 0


for i in range(len(str)):
    if str[i] == 'R':
        lst_R.append(i)

    elif str[i] == 'G':
        lst_G.append(i)

    else:
        lst_B.append(i)

def core():
    global ans
    for i in range(len(all[0])):

        for j in range(len(all[1])):
            if all[1][j] < all[0][i]:                   # condition is broken
                continue

            for k in range(len(all[2])):
                if all[2][k] < all[1][j]:
                    continue
                else:
                    if all[2][k] - all[1][j] != all[1][j] - all[0][i]:
                        ans += 1

all = [lst_R, lst_G, lst_B]

# return True if all of lst1 > of all lst2
def comparison(lst1, lst2):                #lst1 index < lst2 index
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst2[j]>lst1[i]:
                return False
    return True#lst1>lst2



def swap(i):
    if i != 2:
        all[0], all[2] = all[2], all[0]

for i in range(3):      # len(all)

    if comparison(all[0], all[1]) == True or comparison(all[0], all[2])== True:
        swap(i)
        continue

    # iterate process in order

    core()

    if comparison(all[1], all[2])== True:
        swap(i)
        continue

    all[1], all[2] = all[2], all[1]  # swap list order

    # iterate process in order
    core()

    swap(i)

print(ans)