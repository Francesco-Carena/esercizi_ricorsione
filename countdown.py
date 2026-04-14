from time import sleep


def countdown(n):
    while n >= 0:
        print(n)
        sleep (1)
        n-=1

def countdownRecursive(n):
    if n==0:
        print("Stop")
    else:
        print(n)
        sleep (1)
        countdownRecursive(n-1)

if __name__ == '__main__':
    N=10
    #countdown(N)
    countdownRecursive(N)
