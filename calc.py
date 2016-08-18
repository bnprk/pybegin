
print "\n\n\t\t\t***Hello there ! :) ***"

def menu():

    # Presenting a menu before the user.

    print " "
    print "1. Addition"
    print "2. Subtraction"
    print "3. Multiplication"
    print "4. Division"
    print "5. Quit!"
    print " "
    return input ("Choose your option: ")
 
# Adding two given numbers
def add(a,b):
    print a, "+", b, "=", a + b
    
# Subtracting two given numbers
def sub(a,b):
    print a , "-", b, "=", a - b
    
# Multiplying two given numbers
def mul(a,b):
    print a, "*", b, "=", a * b

# Dividing two given numbers
def div(a,b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero ?! (doesn't make sense) :p")
    else:
        print "Result is: ", result)
       
loop = 1            
choice = 0

while loop == 1:     # While the loop runs..

    choice = menu()  # Calling the menu() here.

    if choice == 1:
        res = add(input("First number: "),input("being added to: "))

    elif choice == 2:
        sub(input("First number: "),input("Number to be subtracted: "))

    elif choice == 3:
        mul(input("First number: "),input("being multiplied to: "))

    elif choice == 4:
        div(float(input("First number: ")),(input("divided by: ")))

    elif choice == 5:
        loop = 0    # Loop terminates.

print "\nThankyou! (and visit again) :)"

