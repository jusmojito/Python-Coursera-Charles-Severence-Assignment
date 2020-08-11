name=input('Enter File Name: ')
fname=open(name)
for line in fname:
    line=line.rstrip()
    print(line.upper())
	
