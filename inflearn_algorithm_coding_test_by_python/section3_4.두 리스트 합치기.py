#section3_4.두 리스트 합치기
import sys
sys.stdin = open("/input.txt","rt")

'''
a+b 로 리스트를 합치고 sort() 함수 사용 하라는 의도가 아님.
sort()의 함수 속도는 8Log8 (NlogN)
문제 보기는 이미 정렬된 리스트이기때문에 8번만 돌면됨 

각 리스트의 첫번째를 가르키는 포인터 변수가 필요
각 포인터들의 값을 비교하고 새로운 리스트에 넣고, 다음 포인터를 가리킨다.
if a[p1] <= b[p2] : 
else : 
'''

n=int(input())
a = list(map(int,input().split()))
m=int(input())
b = list(map(int,input().split()))

p1=p2=0
c=[]
while p1<n and p2<m : 
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1+=1
    else :
        c.append(b[p2])
        p2+=1
#남은 리스트를 더한다. 
if p1<n:
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]

for x in c :
    print(x, end=' ')
