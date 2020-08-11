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
if fname is not None:
    words=list()
    cod=dict()
    for ln in fname:
        if ln.startswith('From '):
            words=ln.split()
            if words[2] not in cod:
                cod[words[2]]=1
            else:
                cod[words[2]]+=1
        
    print(cod)
