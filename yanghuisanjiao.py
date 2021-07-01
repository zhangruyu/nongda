#杨辉三角
import datetime


def sanjiao(n=10):
    a = [[0 for j in range(0, 2 * n - 1)] for i in range(0, n)];
    for i in range(0, n):
        for j in range(0, 2 * n - 1):
            a[i][n - 1 - i] = 1;
            a[i][n - 1 + i] = 1;
            if j > (n - 1 - i) and j < (n - 1 + i):
                if (a[i - 1][j - 1] != 0) and (a[i - 1][j + 1] != 0):
                    a[i][j] = a[i - 1][j - 1] + a[i - 1][j + 1];

    for i in range(0, n):
        z = "";
        for j in range(0, 2 * n - 1):
            if a[i][j] == 0:
                x = " ";
            else:
                x = str(a[i][j]);
            z = z + x;
        print(z)

sanjiao(8)

print('success', datetime.datetime.now())

'''
n=10
for i in range (1,n+1):
    b=""
    c=""
    for a in range(0,n-i):
        b+=" "
    for j in range(0,2*i-1):
        c+="*"
    print(b+c)
'''
'''
i=1
n=5
while i<=n:
    s=0
    while s<n-i:
        print(" ",end="")
        s+=1
    p=0
    while p<2*i-1:
        print("*",end="")
        p+=1
    print("")
    i+=1
'''