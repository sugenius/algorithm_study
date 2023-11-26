#section3_5.수 들의 합
import sys
sys.stdin = open("/input.txt","rt")
'''
인덱스 번호를 가리키는 두개의 변수를 사용 lt=0, rt=1 
tot=연속 부분의 합=a[0] (lt~rt 직전의 값들의 합)
tot<m 
tot=m
tot>m
'''
n,m = map(int,input().split())
a=list(map(int,input().split()))
lt=0
rt=1
tot=a[0]
cnt=0
while True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1
print(cnt)