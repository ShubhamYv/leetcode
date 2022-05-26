def stairs(n):
    if n<=1:
        return 1
    return stairs(n-1)+stairs(n-2)

def main():
    t= int(input())
    while t>0:
        n= int(input())
        print(stairs(n))
        t-=1

if __name__ == '__main__':
    main()

""" same as fib series """