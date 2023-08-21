#section2_3.K번째 큰 수 
import sys
sys.stdin=open("input.txt","rt")
n,k=map(int,input().split())
a=list(map(int,input().split()))
res=set() #set(): set 자료구조화 (중복이없음) > 중복을 제거한다. 
#중복을 방지하여 3개의 값을 뽑음 
for i in range(n): 
    for j in range(i+1,n):
        for m in range(j+1,n): 
            res.add(a[i]+a[j]+a[m]) #add() : set자료구조에서 더함 / append 아님 

#set 자료구조는 sort()기능이 없음. 
res=list(res)
res.sort(reverse=True) #내림차순 정렬
print(res[k-1])
