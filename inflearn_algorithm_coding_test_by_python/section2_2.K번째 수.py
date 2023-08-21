#section2_2.K번째 수 
import sys
sys.stdin=open("input.txt","rt")
T=int(input())
for t in range(T):
    n,s,e,k=map(int,input().split())
    a=list(map(int,input().split()))
    #print(a)
    #print(a[1:5]) #1~4인덱스를 추출함.
    a=a[s-1:e]
    a.sort() #오른차순 정렬
    print("#%d %d" %(t+1, a[k-1]) )

