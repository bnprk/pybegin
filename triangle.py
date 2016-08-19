def is_triangle(a, b, c):
    '''Check whether a triangle can be formed with given sides - a, b, c.'''

    while a > 0 and b > 0 and c > 0:
   
        if (a + b + c) > 2 * max(a, b, c):  
        # largest side of a triangle is always less than or equal to half of its perimeter. 
            print("Yes, it is possible to construct a trianlge with these sides.")
            break
        elif (a + b + c) == 2 * max(a, b, c):
            print("Yay ! Its a degenerate triangle")
            break
        else:
            print("Nope, it isn't possible. :( ")
            break
    else:
        print("No side can be zero for a triangle !")


is_triangle(23,32,12)
is_triangle(2, 23, 76)
is_triangle(0,12,24)
