def binomialRecursive(n,m):
    if m==0 or m==n:
        return 1
    else:
        return binomialRecursive(n-1,m-1)+binomialRecursive(n-1,m)

if __name__ == '__main__':
    n=6
    m=3
    print(binomialRecursive(n,m))