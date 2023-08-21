#section0_9.리스트와 내장함수(2)
'''
리스트와 내장함수(2)
'''
a=[23,12,36,53,19]
print(a[:3]) #출력:[23, 12, 36]. 0~2번까지 슬라이스
print(a[1:4]) #출력:[12, 36, 53]. 1~3번까지 슬라이스
print(len(a)) #출력:5. len():리스트 값 몇개 ? 

for i in range(len(a)):
    print(a[i],end=' ')
#출력:23 12 36 53 19
print()

for x in a:
    print(x,end=' ')
#출력:23 12 36 53 19
print()

for x in a:
    if x%2==1:
        print(x, end=' ')
#출력:23 53 19
print()

for x in enumerate(a):  #enumerate:인덱스 번호, 값 까지 모두 알고 싶을 때. enumerate(a) > x 로 값을 (0,23), (1,12), .. 식으로 값을 넘긴다
    print(x)
'''출력
(0, 23)
(1, 12)
(2, 36)
(3, 53)
(4, 19)
'''

#()으로 묶여진 값은 튜플 자료구조 
b=(1,2,3,4,5)
print(b[0]) #출력:1. 
#리스트와 다른 점은, 튜플은 값을 변경할 수 없다. 
#b[0]=7 에러 발생함. 

for x in enumerate(a): 
    print(x[0],x[1])
'''출력
0 23
1 12
2 36
3 53
4 19
'''
print()

for index,value in enumerate(a): #가장많이 사용됨 
    print(index,value)
'''출력
0 23
1 12
2 36
3 53
4 19
'''
print()

if all(60>x for x in a): #all():모든게 참이여야 True 반환, 하나라도 거짓이면 False
    print("YES")
else:
    print("NO")
#출력:YES


if any(15>x for x in a): #any():하나라도 참이라면 True 반환,모든게 거짓이면 False
    print("YES")
else:
    print("NO")
#출력:YES
if any(11>x for x in a): #any():하나라도 참이라면 True 반환,모든게 거짓이면 False
    print("YES")
else:
    print("NO")
#출력:NO
