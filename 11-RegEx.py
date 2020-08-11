import re

fname=input("Enter file name:")
fhandle=open(fname,'r')
l=list()
p=list()

for line in fhandle:
    y=re.findall("[0-9]+",line)
    if(len(y)>0):
        for v in y:
            l.append(v)
for v in l:
    t=int(v)
    p.append(t)
print(sum(p))

