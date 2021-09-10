#link to problem: https://leetcode.com/problems/climbing-stairs/

def fibonacci(n,mydict={}):
    if n in mydict:
        return mydict[n]
    if n < 2:
        return 1
    else:
        mydict[n] = fibonacci(n-1, mydict) + fibonacci(n-2, mydict)
    return mydict[n]


print(fibonacci(2)) #2
print(fibonacci(3)) #3
print(fibonacci(4)) #5
