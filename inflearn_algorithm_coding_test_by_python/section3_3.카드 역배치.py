#section3_3.카드 역배치
import sys
sys.stdin = open("/input.txt","rt")
'''
a,b=map(int,input().split())
print(a,b)
a,b = b,a #변수 스왑 방법 
print(a,b) 
'''

a=list(range(21))
for _ in range(10): #_언더바 사용시 변수 할당 없이 단순 반복함
    s, e=map(int, input().split())
    for i in range((e-s+1)//2) : #(e-s+1)//2 교환 반복 하는 횟수 (예를들어 2~7 구간 스왑 시 3번 필요)
        a[s+i], a[e-i] = a[e-i], a[s+i]
a.pop(0) #0번 인덱스를 제거하라
for x in a :
    print(x,end=' ')