def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n > 1:
        return fib(n-1)+fib(n-2)

if __name__=="__main__":

    mx = 10;

    with open("out.txt","w") as f:
        for x in range(0,mx+1):
            f.write(str(fib(x))+" ")
