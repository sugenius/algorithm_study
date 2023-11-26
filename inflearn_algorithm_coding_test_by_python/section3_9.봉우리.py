#section3_9.봉우리
import sys
sys.stdin = open("/input.txt","rt")

dx=[-1,0,1,0] #상하좌우 문제를 풀 경우 리스트를 이와 같이 초기화 하여 사용
dy=[0,1,0,-1]

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
a.insert(0,[0]*n)
a.append([0]*n)
for x in a : 
    x.insert(0,0)
    x.append(0)
cnt=0
for i in range(1,n+1):
    for j in range(1,n+1):
        #all(조건) : 모두 조건일 경우 참 
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)) : #a[i+dx[k]][j+dy[k]] for k in range(4) : a의 상하좌우
            cnt+=1
print(cnt)
