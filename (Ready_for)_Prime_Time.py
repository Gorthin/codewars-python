'''
We need prime numbers and we need them now!

Write a method that takes a maximum bound and returns all primes up to and including the maximum bound.

For example,

11 => [2, 3, 5, 7, 11]
'''


def prime(n):
    candidat = [1 for x in range(n+1)]
    prime = []
    for i in range(2,n+1):
        if candidat[i] != 0:
            prime.append(i)
            for j in range(i+i,n+1,i):
                candidat[j]=0
    return prime