def ack(m, n):
    '''Computes the Ackermann function, A(m, n)
        n, m : non-negative integers
    '''

    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))
    else:
        print("Sorry, invalid input !")
        return

ack(3, 4)

