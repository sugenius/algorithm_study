#section2_4.대푯값
import sys
sys.stdin=open("input.txt","rt")

n = int(input())
a = list(map(int,input().split()))
#ave=round(sum(a)/n) #round(): 소수 첫째 자리에서 반올림 , sum(): 리스트를 모두 합함
ave=int((sum(a)/n)+0.5) #round():round_half_up 반올림 방식이므로 0.5를 더하구 int 화  
min=2147000000 #4byte 정수형 가장 큰 값 으로 초기화
for idx, x in enumerate(a):
    tmp=abs(x-ave) #평균과 거리를 구함. abs():절댓값 
    if(tmp<min):
        min=tmp
        score=x
        res=idx+1
    elif tmp==min:
        if x>score:
            score=x
            res=idx+1
print(ave, res)

