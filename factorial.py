def factorial(n):
    pass

def factorialRecursive(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorialRecursive(n-1)


if __name__ == "__main__":
    n=5
    #factorial(n)
    print(factorialRecursive(n))