#section2_9.주사위 게임import sys
import sys
sys.stdin = open("/input.txt","rt")

n=int(input())
res=0
for i in range(n):
    tmp=input().split() #문자 리스트로 받음
    tmp.sort() #정렬
    a,b,c = map(int,tmp)
    if a==b and b==c:
        money=10000+a*1000
    elif a==b or a==c:
        money=1000+a*100 
    elif b==c : 
        money=1000+(b*100)
    else:
        money=c*100
    if money>res : 
        res=money
print(res)
