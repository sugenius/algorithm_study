#section2_1.K번째 약수 

#import sys


'''
#sys.stdin=open("input.txt","rt")

#n,k = map(int(input()),sep=' ')
n=6
k=3

result=list()
for i in range(1,n+1):
    if n%i==0:
        result.append(i)

#print(result)
#if k > (result.length+1) :
if k > len(result)+1 :
    print(-1)
else :
    print(result[k-1])

'''

import sys
#sys.stdin=open("input.txt","rt")
n,k=map(int, input().split()) #띄어쓰기로 구분하여 읽는다. 
cnt=0
for i in range(1,n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)