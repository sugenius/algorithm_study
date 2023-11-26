#section3_2.숫자만 추출
import sys
sys.stdin = open("/input.txt","rt")

s=input()
res=0
for x in s:
    #x.isdecimal() : 0~9까지의 숫자를 찾음 
    #x.isdigit() : 알파벳이 아닌 모든 숫자형태를 찾음 거듭제곱 포함 
    if x.isdecimal() :
        res=res*10+int(x) #숫자화시킴
print(res)
cnt=0
for i in range(1,res+1) :
    if res%i==0 :
        cnt+=1
print(cnt)