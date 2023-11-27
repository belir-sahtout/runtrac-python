L = [10,20,30,20,10,50,60,40,80,50,40]
print("liste initial : " ,L)
l = []
for i in L:
    if i not in l:
        l.append(i)

print("liste sans les doublons :",l)
      