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
    
'''
메모
result=''.join(l) #에러남. 각 요소가 문자열이 아니라서.
result = ''.join(map(str,l)) #1234109871312115614151617181920
result = ' '.join(map(str,l)) #출력:1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20
'''