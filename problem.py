#  Q-1  Sum Of the Number
print("Enter Value For Find Sum Of The Numbers\n")
n = int(input("Enter the Number : \n"))
sum=0
for i in str(n):
    sum += int(i)

print(f" The Sum of {n} Numbers is - {sum} ")



# Q-2 Sum Of Odd Numbers
n = int(input("Enter the Number : \n"))
sum = 0
for i in range(0,n+1):
    if i%2!=0:
       sum +=i
print(f"The sum of {n} Odd range is {sum} ") 



 # Q-3 remove constant from a string
def C_rev(string):
    m=['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 's', 't', 'v', 'x', 'z','h', 'r', 'w', 'y' ]
    result = [string for string in string.lower() if string not in m]
    result = ''.join(result)
    print(result)

print("Enter String For Remove Consonent \n")
string = input("Enter string with your numbers : \n")

print(C_rev(string))




# Q -3    Python program to find LCM of two numbers



def gcd(a,b):
	if a == 0:
		return b
	return gcd(b % a, a)

def lcm(a,b):
	return (a / gcd(a,b))* b
print("Enter Value For Find LCM Of Two Numbers \n")
a = int(input("Enter Number : \n"))
b = int(input("Enter Number : \n"))

print(f"LCM of {a} and {b} is - {int(lcm(a, b))}")


# Q-4 
from cmath import sqrt
def prime(n):
    if n % n == 0 and n%1==0 and n % 2!=0 and n % 3!=0 and n % 4!=0 and n % 5!=0 and n % 6!=0 and n % 8!=0 and n % 9!=0 and n % 10!=0:
        sqrt_pN= sqrt(n)
        return sqrt_pN
    elif n==2 :
        n=2
        sqrt_pN= sqrt(n)
        return sqrt_pN
    elif n==3:
        n=3
        sqrt_pN= sqrt(n)
        return sqrt_pN
    elif n==5:
        n=5
        sqrt_pN= sqrt(n)
        return sqrt_pN
print("Enter Value For Find Square root of Prime Number  \n")

n= int(input("Enter Number : \n"))
print(prime(n))

# Q-5 permutation

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        n= n * fact(n-1)
    return n

def Permutation(No_1,No_2):
    rslt = No_1/No_2
    return rslt
print("Enter Value For Find Permutation \n")
n = int(input("Enter The Value of n: \n"))
k=int(input("Enter The Value of k : \n"))
No_1 =fact(n)
No_2 =fact(n-k)
print(f" The permutation of {n} and {k} is - {Permutation(No_1,No_2)}")


# Combination

def Combination(No_1,No_2,No_3):
    rslt = No_1 / ( (No_2) * (No_3) )
    return rslt
print("Enter Value For Find Combination \n")
n= int(input("Enter The Value of n : \n"))
r= int(input("Enter The Value of r : \n"))

No_1 =fact(n)
No_2 =fact(r)
No_3 =fact(n-r)
print(f" The Combination of {n} and {r} is - {Combination(No_1,No_2,No_3)}")
