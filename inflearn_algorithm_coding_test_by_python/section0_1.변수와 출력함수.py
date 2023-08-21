#section0_1.변수와 출력함수 
'''
변수명 정하기
1)영문과 숫자, _ 로 이루어진다.
2) 대소문자를 구분한다.
3) 문자나, _로 시작한다.
4) 특수문자를 사용하면 안된다. (&,% 등)
5) 키워드를 사용하면 안된다. (if,for 등)
'''

a=1
A=2
A1=3
#2b=4 #주석처리 (한줄) # 
print(a,A,A1)

a,b,c=3,2,1
print(a,b,c)

#값 교환
a,b=10,20
print(a,b)
a,b=b,a
print(a,b)

#변수 타입
a=12345
print(type(a))
a=12.123456789123456789
print(a) #실수형 8byte까지만 저장되어 출력됨
print(type(a))
a='student' # ', " 따옴표 둘 다 가능
print(a)
print(type(a))


#출력방식
print("number")
a,b,c=1,2,3
print(a,b,c) #한줄로 한번에, 사이에 자동으로 띄워쓰기 됨
print("number : ", a,b,c)
print(a,b,c, sep='') #각 변수 사이에 띄워쓰기 제거. seperator 가 각 변수 사이를 지정하라
print(a,b,c, sep=',') #각 변수 사이에 , 기호
print(a,b,c, sep='\n') #각 변수 개행
print(a) #print()는 자동으로 줄바꿈이 있음
print(b)
print(c)
print(a, end=' ')
print(b, end=' ')
print(c)


