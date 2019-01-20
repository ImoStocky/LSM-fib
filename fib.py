import argparse

def main(val):
    p = argparse.ArgumentParser(description='Fib sequence.')
    p.add_argument('int', metavar='n', type=int)
    args = p.parse_args(val)
    with open("out.txt","w") as f:
        for x in range(0,args.int+1):
            f.write(str(fib(x))+" ")

def fib(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    elif n > 1:
        return fib(n-1)+fib(n-2)
    else:
        raise(ValueError)

if __name__=="__main__":
    import sys
    main(sys.argv[1:])
