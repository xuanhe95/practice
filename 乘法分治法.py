# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.

print('hello')

x=3141592653589793238462643383279502884197169399375105820974944592

y=2718281828459045235360287471352662497757247093699959574966967627

n=len(str(x))

def recursion(x,y,n):

    if n==1:

        return x*y


    a=x//10**(n//2)
    b=x%10**(n//2)
    c=y//10**(n//2)
    d=y%10**(n//2)

    ac=recursion(a,c,n//2)
    bd=recursion(b,d,n//2)

    z=recursion((a+b),(c+d),n//2)-ac-bd

    print((n//2))

    return ac*10**n+z*10**(n//2)+bd

print(int((recursion(x,y,n))))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
