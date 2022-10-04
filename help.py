def degree(f):
    if ((f == []) or (f==[0])):
        return [0]
    while f[0] == 0 and len(f) != 1:
        del f[0]
    
