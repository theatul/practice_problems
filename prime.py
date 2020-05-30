

# Finding square root of an number number ** 0.5 
# ** is an exponent sign

# prime factorization: deviding a number  by prime numbers less than square root of n to get all prime divisibles.
# All non prime numbers are multiple of some prime less than the number itself so iteration can be from 2 to sqaure root of n
# 
# 
# sieve-of-eratosthenes: https://www.geeksforgeeks.org/sieve-of-eratosthenes/  if you need to find all prime numbers up to a limit
# Steps is to create an array of the size N and mark everything prime except one.. then iterate over the array upto N/2 check if the number
# is prime and if yes then all multipliers are marked not prime. time complexity N Log N

def findAllPrimes():
    input = 100
    for i in range (2, input):
        if checkPrime(i) == True:
            print("{}".format(i))

def checkPrime(input):
    sqrt = int(input ** 0.5)
    for i in range(2, sqrt+1):
        if (input % i == 0):
            #print("No {} {}".format(i, input/i))
            return False

    return True

findAllPrimes()