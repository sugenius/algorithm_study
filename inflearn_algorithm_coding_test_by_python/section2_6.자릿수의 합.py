#section2_6.자릿수의 합
import sys
#sys.stdin = open("/input.txt","rt")

n = int(input())
a = list(map(int,input().split()))

def digit_sum(x):
    sum=0
    '''
    while x>0:
        sum+=x%10 
        x=x//10
    return sum
    ''' 
    for i in str(x): #str():문자열화. x 정수를 문자열화 시킴.
        sum+=int(i)
    return sum 

max=-2147000000
for x in a : #a에 있는 리스트에 x값으로 하나씩 접근
    tot = digit_sum(x)
    if tot>max:
        max=tot
        res=x
print(res)
