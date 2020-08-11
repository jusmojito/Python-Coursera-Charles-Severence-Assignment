import fname

fname=fname.entfname()
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
