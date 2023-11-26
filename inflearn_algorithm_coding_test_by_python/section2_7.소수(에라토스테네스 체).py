#section2_7.소수(에라토스테네스 체)
import sys
sys.stdin = open("/input.txt","rt")

#소수 : 1과 자기 자신 만을 약수로 가지는 수
#1은 소수의 대상이 아님 2~ 

n = int(input()) 
ch=[0]*(n+1)
cnt=0
for i in range (2,n+1):
    if ch[i] == 0:
        cnt+=1
        for j in range(i,n+1,i): #i의 배수를 제거한다. 
            ch[j]=1
print(cnt)