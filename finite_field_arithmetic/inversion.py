def inversion(mod,h,f):

    g,a,y= extended_euclidian(mod,h,f)
    if (g != 1):
        answer= "error"
        return answer

    else:
        return a

