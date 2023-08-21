#section0_12.람다함수
'''
람다 함수

def plus_one(x):
    return x+1 

print(plus_one(1))
'''

'''
plus_two = lambda x: x+2 #람다 함수 정의. x를 넣으면 x+2를 리턴한다. plus_two 변수에 할당. 
print(plus_two(1)) #출력:3
'''

def plus_one(x):
    return x+1 

a=[1,2,3]
print(list(map(plus_one,a))) #츌력:[2, 3, 4]. map(함수/자료형,자료). a에 있는 값들이 plus_one 함수의 적용을 받는다. 

print(list(map(lambda x:x+1,a))) #츌력:[2, 3, 4]
