n= int(input().strip())

a = dict()
#make a key for each input
#as keys are not repeted in a dict
for _ in range(n):
    w = input().strip()
    a.setdefault(w,0) # init a key
    a[w] += 1 # add 1 to the value

print(len(a.keys()))
print(*a.values())
