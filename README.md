# Innomatics_Internship_APR_21
#Question no.1=Print Hello, World! to stdout.
#answer
print("Hello, World!")
#Question no.2=Given an integer,n , perform the following conditional actions:

#If n  is odd, print Weird
#If n is even and in the inclusive range of 2  to 5, print Not Weird
#If n is even and in the inclusive range of  6 to 20 , print Weird
#If n is even and greater than 20 , print Not Weird

num = int(input("Enter the number"))
if num % 2 == 1:
    print("Weird")
elif (num % 2 == 0 & 2<=num<=5):
    print("Not weird")
elif (num % 2 == 0 & 6<=num<=20):
    print("weird")
else:
    print("not weird")
#Question no.3 # The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

#he first line contains the sum of the two numbers.
#he second line contains the difference of the two numbers (first - second).
#he third line contains the product of the two numbers.
    if __name__ == '__main__':
        a = int(input())
        b = int(input())
        print(a + b)
        print(a - b)
        print(a * b)
#Questionn0.4=#The provided code stub reads two integers, a and b, from STDIN.

#Add logic to print two lines. The first line should contain the result of integer division,  a//b . The second line should contain the result of float division, a / b.
#No rounding or formatting is necessary.
#Answer=
    if __name__ == '__main__':
        a = int(input())
        b = int(input())

    print(a // b)
    print(a / b)

# Question no.5=The provided code stub reads and integer,n, from STDIN. For all non-negative integers i<n , printi**2

 #Answer
    n=int(input("Enter the number"))
    for i in range(1,n):
        square=i**2
        print(square)
#Question no.6= Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

#Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.
def is_leap(year):
    leap = False

    # Write your logic here
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

    return leap


year = int(input())
print(is_leap(year))

#Question no.7==Print the list in lexicographic increasing order.
x = int(input())
y = int(input())
z = int(input())
n = int(input())
ans = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(ans)
