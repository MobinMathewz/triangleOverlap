'''This function finds the area of the triangle.'''
def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)


'''Given coordinates A(x1, y1), B(x2, y2) and C(x3, y3) of a triangle, 
this function checks if the pint P(x, y) lies inside the triangle'''
def CheckIfInside(A, x, y):

    x1, y1, x2, y2, x3, y3=A[0][0], A[0][1], A[1][0], A[1][1], A[2][0], A[2][1]
    # Calculate area of triangle ABC
    A = area(x1, y1, x2, y2, x3, y3)

    # Calculate area of triangle PBC
    A1 = area(x, y, x2, y2, x3, y3)

    # Calculate area of triangle PAC
    A2 = area(x1, y1, x, y, x3, y3)

    # Calculate area of triangle PAB
    A3 = area(x1, y1, x2, y2, x, y)

    # Check if sum of A1, A2 and A3
    # is same as A
    if (A == A1 + A2 + A3):
        return True
    else:
        return False


def main(A, B):

     for i in range(3):
         x, y=B[i][0], B[i][1]
         if (CheckIfInside(A, x, y)):
             answer='Intersecting'
             return('Intersecting')
             return 0
     return('Not Intersecting')


A= []
B= []

for i in range(3):
    j=str(i)
    print('Enter x'+j+','+' y'+j+' of the first triangle:')
    x=float(input())
    y=float(input())
    A.append([x, y])

for i in range(3):
    j=str(i)
    print('Enter x'+j+','+' y'+j+' of the second triangle:')
    x=float(input())
    y=float(input())
    B.append([x, y])

output='Invalid input'
output=main(A, B)

if(output!='Intersecting'):
    output = main(B, A)

print(output)
