def f(n):
    ret=1
    while n>1:ret*=n;ret%=p;n-=1
    return ret
p=1000000007;n,k=map(int,input().split())
a=f(n);b=f(k)*f(n-k)%p;an=a*pow(b,p-2,p)%p
print(an)