# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
import math
x=int(input('x:'))
y=int(input('y:'))
n=len(str(x))
def recursion(x,y,n):

    if n==1:
        sign = x * y

        return sign
    else:
        a=x//math.pow(10,n/2)
        b=x%math.pow(10,n/2)
        c=y//math.pow(10,n/2)
        d=y%math.pow(10,n/2)
        ac=recursion(a,c,n/2)
        bd=recursion(b,d,n/2)
        abcd=recursion((a-b),(d-c),n/2)+ac+bd

        return ac*math.pow(10,n)+abcd*math.pow(10,n/2)+bd


print(recursion(x,y,n))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
