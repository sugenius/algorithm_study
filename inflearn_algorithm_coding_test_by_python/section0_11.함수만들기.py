#section0_11.함수만들기
'''
함수 만들기
'''

'''
def add(a,b):
    c=a+b
    print(c)
add(3,2) #출력:5 
add(5,7) #출력:12
#인터프리터라 위에서 아래부터 읽기 때문에 함수는 위쪽에 정의해 둔다. 
#함수 호출은 위에, 함수는 아래에 정의한다면 에러남. 
'''

''''
def add(a,b):
    c=a+b
    return c
#print(add(3,2)) #출력:5
x=add(3,2)
print(x)
'''

'''
def add(a,b):
    c=a+b
    d=a-b
    return c,b #두 개의 값을 반환 가능 > 튜플 자료구조로 리턴됨 
print(add(3,2)) #출력:(5,2)
'''


#소수 판별 함수
def isPrime(x): #나누어 떨어지는 값이 소수 : 1과 자기자신만 존재한다. 
    for i in range(2,x): #x 자기 자신을 포함하지 않음
        if x%i==0:
            return False 
    return True

a=[12,13,7,9,19]
for y in a:
    if isPrime(y):
        print(y, end= ' ')
#출력:13 7 19 


