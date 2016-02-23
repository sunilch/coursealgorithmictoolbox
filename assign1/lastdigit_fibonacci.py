
def lastdig_fibonacci_iterative(nth):
    '''returns the nth fibonacci number'''
    if nth==0:
        return 0
    elif nth==1:
        return 1
    else:
        lastsec=0
        lastfir=1
        currval=0
        for ind in xrange(nth-1):
            currval=(lastsec+lastfir)%10
            lastsec=lastfir
            lastfir=currval
        return currval

if __name__=='__main__':
    inpval=int(raw_input('Enter the index of fibonacci you want last digit for: '))
    #print fibonacci_recursive(inpval)
    print lastdig_fibonacci_iterative(inpval)