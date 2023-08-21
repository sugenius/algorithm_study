#section2_5.정다면체
import sys 
sys.stdin = open("input.txt","rt")

n,m=map(int,input().split())
cnt=[0]*(n+m+3) #0으로 초기화, 크기는 (n+m+3) 

a=list()
for i in range (1,n+1):
    for j in range (1,m+1):
        cnt[i+j] +=1 

max=-2147000
for i in range(n+m+1) :
    if cnt[i] > max:
        max=cnt[i]
        
for i in range(n+m+1) :
    if cnt[i] == max :
        print(i, end=' ')
