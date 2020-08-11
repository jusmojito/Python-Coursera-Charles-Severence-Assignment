
import fname

fname=fname.entfname()

mails=dict()
words=list()
address=list()
if fname is not None:
    for line in fname:
        if line.startswith('From '):
            words=line.split()
            address=words[1].split('@')
            if address[1] not in mails:
                mails[address[1]]=1
            else:
                mails[address[1]]+=1
print(mails)
maxmails= None
keyn=None
for key in mails:
    if maxmails is None:
        maxmails=mails[key]
    else:
        if(mails[key]>maxmails):
            maxmails=mails[key]
            keyn=key
        else:
            continue
print(keyn,mails[keyn])
