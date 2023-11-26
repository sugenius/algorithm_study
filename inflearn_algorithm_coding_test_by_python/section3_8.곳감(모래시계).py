#section3_8.곳감(모래시계)
import sys
sys.stdin = open("/input.txt","rt")

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
m=int(input())
for i in range(m):
    h,t,k = map(int,input().split()) #행번호, 방향 0왼쪽 1오른쪽, 회전 격자 수 
    if t==0 : #왼쪽 회전
        for _ in range(k) :
            a[h-1].append(a[h-1].pop(0)) 
            #a[h-1].pop(0)를 하는 경우 앞에 하나가 제거 되고 뒤에 존재하는 값들이 앞으로 당겨짐
            #이 값을 가장 뒤에 append 시켜준다.
    else :#오른쪽 회전
        for _ in range(k) :
            a[h-1].insert(0,(a[h-1] .pop())) 
'''
for x in a :
    print(x) 
'''

res=0
s=0
e=n-1
for i in range(n):
    for j in range(s,e+1):
        res+=a[i][j]
    if i < n//2:
        s+=1
        e-=1
    else :
        s-=1
        e+=1
print(res)