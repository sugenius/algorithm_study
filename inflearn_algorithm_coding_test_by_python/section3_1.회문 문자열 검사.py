#section3_1.회문 문자열 검사
import sys
sys.stdin = open("/input.txt","rt")

n=int(input())
for i in range(n):
    s=input()
    s=s.upper() #대문자화
    '''
    size=len(s)
    #print(s[-1])#파이썬은 인덱스 뒤에서 부터 접근가능 
    for j in range(size//2) :
        if s[j]!=s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))
    '''
    
    if s==s[::-1] :#s[::-1] 문자열을 뒤집음, 파이썬 만의 방법이기에 위 방법으로 직접 해보는게 좋긴함
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))
    