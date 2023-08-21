#section0_5.반복문을 이용한 문제 풀이
'''
반복문을 이용한 문제풀이
1) 1부터 N까지 홀수출력하기
2) 1부터 N까지의 합 구하기
3) N의 약수 출력하기


n=int(input())
for i in range(1,n+1):
    print(i)
'''

#1) 1부터 N까지 홀수출력하기
n=int(input())
for i in range(1,n+1):
    if i%2==1:
        print(i)

#2) 1부터 N까지의 합 구하기
n=int(input())
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)


#3) N의 약수 출력하기
#약수 어떤 수를 나누어떨어지게 하는 수 
n=int(input())
for i in range(1,n+1): #n 자신 까지 
    if n%i==0:
        print(i, end= ' ')

