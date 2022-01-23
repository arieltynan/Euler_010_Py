#Problem 10
# Using Sieve of Eratosthenes
MAX_PRIME = 2000000
A = [True]*(MAX_PRIME+1)

for i in range(2, int(MAX_PRIME**(1/2)+1)):
    if A[i]:
        j = i**2
        while j <= MAX_PRIME:
            A[j] = False
            j += i

result = sum([i for i in range(2, MAX_PRIME+1) if A[i]])
print(result)  

