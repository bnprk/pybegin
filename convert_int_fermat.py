'''The Fermat's Theorem states that there are no positive
    integers a,b and c such that :  a ** n + b ** n = c ** n
    for any values of n greater than 2
'''

def check_fermat(a, b, c, n):
    '''Check the validity of Fermat's Theorem for valid inputs of a,b,c and n'''

    if n <= 1:
        print("n needs to be greater than 1")
        return                                                                      # exit the function

    elif n >= 2 and a > 0 and b > 0 and c > 0 and (a ** n + b ** n == c ** n):      # a,b,c shouldn't be zero as well
        print("Holy smokes, Fermat was wrong !")
    else:
        print("The theorem holds good. Fermat wasn't wrong. :)")


def convert_to_int(a,b,c,n):
    '''Take integer input from user'''
    print(__doc__)
    while True:
        try:
            a = int(input("Enter a : "))
            b = int(input("Enter b : "))
            c = int(input("Enter c : "))
            n = int(input("Enter n : "))
        except ValueError:
            print("Please enter integer only ! Let's try again.")
            continue
        else:
            break

    check_fermat(a,b,c,n)


convert_to_int(2,2,2,2)
