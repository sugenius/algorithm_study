#section0_1.변수입력과 연산자
'''
변수입력과 숫자

a=input("숫자를 입력하세요 : ")
print(a)
'''

'''
a,b=input("숫자를 입력하세요 : ").split() #split:띄어쓰기로 숫자를 구분
print(a,b)
print(a+b) #출력:23>문자열로 인식하였기 때문
print(type(a))
c=a+b
print(type(c)) #출력:<class 'str'>
print(c)
'''

'''
a,b = input("숫자를 입력하세요 : ").split()
a=int(a)
#print(type(a))
b=int(b)
print(a+b)

a,b=map(int, input("숫자를 입력하세요 : ").split()) #map() 내장함수 
print(a+b)
print(a-b)
print(a*b)
print(a/b) #나누기
print(a//b) #몫
print(a%b) #나머지
print(a**b) #거듭제곱. a를 b번 곱한다. a의 b승
'''

a=4.3 
b=5
c=a+b #실수+정수형= ? 
print(type(c)) #출력:<class 'float'> 
#실수 > 정수. 범위가 실수가 더 큼. 더 큰 범위로 결과가 나옴 


