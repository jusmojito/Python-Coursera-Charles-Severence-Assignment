name=input('Enter File: ')
fname=open(name)
count=0
toprint=list()
for line in fname:
    lwords=line.split()
    for word in lwords:
        count=count+1
        if word in toprint:
            continue
        toprint.append(word)
toprint.sort()
print(count)
print(toprint)
print(len(toprint))
