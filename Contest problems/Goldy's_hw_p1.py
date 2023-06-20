import math
t=int(input())
sumarr=[]

for index in range(t):
    nA=int(input())
    A=list(map(int, input().strip().split()))
    nB=int(input())
    B=list(map(int, input().strip().split()))
   
    for element in B:
        factors=0
        for i in range(1,element+1):
            if (element%i==0):
                factors=factors+1
        if (factors==2): #if prime
            if (A[element]>=0):
                A[element]=math.floor(A[element]/element)
            else:   
                A[element]=math.ceil(A[element]/element)
        elif (element%2!=0): #if odd
            A[element]=pow(A[element],3)
        elif (element%2==0): #if even
            A[element]=pow(A[element],2)
        else:
            pass
   
    sum=0
    for k in range (nA):
        sum=sum+A[k]
    sumarr.append(sum)
   
for j in sumarr:
    print(j)
