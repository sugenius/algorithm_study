#section3_10.스도쿠 검사
import sys
sys.stdin = open("/input.txt","rt")

'''
ch=[0]*10 체크리스트 3개 필요 (열/행/3*3그룹)
ch[a[i][j]] = 1 을 넣어 체크
sum(ch) != 9 확인
'''

def check(a):
    for i in range(9):
        ch1=[0]*10 #행 체크
        ch2=[0]*10 #열 체크
        for j in range(9):
            ch1[a[i][j]]=1 
            ch2[a[j][i]]=1
        if sum(ch1)!=9 or sum(ch2)!=9 :
            return False
    
    for i in range(3):
        for j in range(3):
            ch3=[0]*10 #3*3그룹 체크
            for k in range(3):
                for s in range(3): 
                    ch3[a[i*3+k][j*3+s]]=1
                if sum(ch3)!=9 :
                    return False
    return True

a=[list(map(int,input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")