#section2_5.정다면체
import sys 
sys.stdin = open("input.txt","rt")

n,m=map(int,input().split())
cnt=[0]*(n+m+3) #0으로 초기화, 크기는 (n+m+3)
#결과값과 같은 인덱스 위치에 1을 더해간다.
#예를 들어 결과에서 a[5]=6일 경우 5라는 값이 5번 등장하였다고 봄. 

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
