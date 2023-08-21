import sys
sys.stdin=open("input.txt","rt")

n = int(input())
a = map(int,input().split())

b = 0 
for i in range(a) :
    b +=i
avg = b/n
print(avg)