name=input('Enter the file name: ')
fname=open(name)
sum=0
pos=0
count=0
for line in fname:
    if(line.startswith('X-DSPAM-Confidence:')):
       pos=line.find("dence:")
       print(pos)
       '''
       numberf=line[pos+1:]
       numberf=numberf.rstrip()
       numberf=float(numberf)
       sum=numberf+sum
       count+=1
print('Average spam confidence: ',sum/count)'''
