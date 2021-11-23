N = int(input())
list_pos = []
list_neg = []
for i in range(N):
    n = int(input())
    if(n >= 0):
        list_pos.append(n)
    else:
        list_neg.append(n)
list_pos.sort()
list_neg.sort()
list_neg.reverse()
list_all = list_pos + list_neg
s = ''
for i in range (len(list_all)):
    s += str(list_all[i]) + ' '
print(s)
