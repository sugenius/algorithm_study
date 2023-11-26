#section3_6.격자판 최대합
import sys
sys.stdin = open("/input.txt","rt")

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)] #한줄을 읽어 리스트화 n번 받아 이차원 리스트를 생성한다.
'''
print(a)
for x in a :
    print(x) 
'''
largest=-2147000000 #max명은 함수와 겹치기 때문에 지양

for i in range(n):
    sum1=sum2=0 #sum1 행의 합, sum2 열의 합
    for j in range(n) :
        sum1+=a[i][j] #행의 합
        sum2+=a[j][i] #행의 합
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2
        
#대각선값 찾아보기 
sum1=sum2=0
for i in range(n):
    sum1+=a[i][i] #\ 대각선 합
    sum2+=a[i][n-i-1] #/ 대각선 합
if sum1>largest:
        largest=sum1
if sum2>largest:
    largest=sum2
print(largest)