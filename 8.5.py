name=input('Enter a file name: ')
fname=open(name)
datareq=list()

for line in fname:
    if line.startswith('From '):
        linewords=line.split()
        datareq.append(linewords[1])
#print(datareq)

for names in datareq:
    print(names)
print("There were ",len(datareq),"lines in the file with From as the first word")
