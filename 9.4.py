def entfname():
    c=0
    while c==0:
        name=input('Enter the file name(::xap:: to end): ')
        if name=='xap':
            c=-1
            return None
        else:    
            try:
                fname=open(name)
                c=-1
                return fname
            except:
                print('Invalid File name')
    

fname=entfname()

mails=dict()
words=list()
if fname is not None:
    for line in fname:
        if line.startswith('From '):
            words=line.split()
            if words[1] not in mails:
                mails[words[1]]=1
            else:
                mails[words[1]]+=1
#print(mails)
maxmails= None
keyn=None
for key in mails:
    print(key,mails[key])
for key in mails:
    if maxmails is None:
        maxmails=mails[key]
    else:
        if(mails[key]>maxmails):
            maxmails=mails[key]
            keyn=key
        else:
            continue
print('Max is : ',keyn,mails[keyn])
