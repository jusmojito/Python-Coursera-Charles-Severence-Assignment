import fname

fname=fname.entfname()

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
print(mails)
    
