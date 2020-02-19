# Python program that
# inputs a list of words, separated by whitespace, and outputs how many
# times each word appears in the list


x = input().split()

d = dict()
for i in range(len(x)):
    if x[i]in d.keys():
        d[x[i]]+=1
    else:
        d[x[i]] = 1
        d.update()
print(d)
