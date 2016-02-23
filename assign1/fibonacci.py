def fibonacci_recursive(nth):
    '''returns the nth fibonacci number'''
    if nth==0:
        return 0
    elif nth==1:
        return 1
    else:
        return fibonacci_recursive(nth-1)+fibonacci_recursive(nth-2)

def fibonacci_iterative(nth):
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
            currval=lastsec+lastfir
            lastsec=lastfir
            lastfir=currval
        return currval

if __name__=='__main__':
    inpval=int(raw_input('Enter the index of fibonacci you want: '))
    #print fibonacci_recursive(inpval)
    print fibonacci_iterative(inpval)