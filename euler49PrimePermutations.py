'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

def isPrime(n):
    result = True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            result = False
            break
    return result

def firstPrime(x, y):
    my_number = 0
    for i in range(x, y+1, 2):
        if isPrime(i):
            my_number = i
            break
    return my_number

def lastPrime(x, y, z):
    my_number = 0
    for i in range(y - 2*z, x-1, -2):
        if isPrime(i):
            my_number = i
            break
    return my_number



def PrimePermutations(x, y, z):
    start_number = firstPrime(x, y)
    final_number = lastPrime(x,y, z)
    final_list = []
    for i in range(start_number, final_number+1, 2):
        if set(str(i)) == set(str(i +z)) and set(str(i)) == set(str(i + 2*z)):
            if isPrime(i) and isPrime(i + z) and isPrime(i + 2*z):
                final_list.append(str(i)+str(i+z)+str(i+2*z))
    return final_list
            

final = PrimePermutations(1001,9999,3330)
print(final)