#section0_8.리스트와 내장함수(1)
'''
리스트와 내장함수(1)
'''

import random as r 


a=[] #빈 리스트 생성 
print(a)
b=list() #빈 리스트 생성 
print(b)

a=[1,2,3,4,5]
print(a) #출력:[1, 2, 3, 4, 5]
print(a[0]) #출력:1

b=list(range(1,11))
print(b) #출력:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

c=a+b #리스트 합침
print(c) #출력:[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(a)
a.append(6) #append(): 리스트 뒤에 추가
print(a) #출력:[1, 2, 3, 4, 5, 6]

a.insert(3,7) #insert(): 특정 인덱스에 추가, 이미 있던 값은 밀림.
print(a)  #출력:[1, 2, 3, 7, 4, 5, 6]

a.pop() #pop(): 리스트 뒤에 하나 제거
print(a) #출력: [1, 2, 3, 7, 4, 5]
a.pop(3) #pop(index) : 입력한 인덱스 값 제거 
print(a) #출력:[1, 2, 3, 4, 5]

a.remove(4) #remove(): 값 제거 
print(a) #출력:[1, 2, 3, 5]

print(a.index(5)) #index() : 값의 인덱스 번호 
#출력: 3

a=list(range(1,11))
print(a) #출력:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(a)) #출력:55. sum():a의 리스트 모든 값을 합함 
print(max(a)) #출력:10. max():a의 리스트 중 최댓값 
print(min(a)) #출력:1. min():a의 리스트 중 최솟값 
print(min(7,5)) #출력:5. min():7,5 중 최솟값
print(min(7,3,5)) #출력:3. min():7,3,5 중 최솟값

print(a)
r.shuffle(a) #shuffle():a리스트를 무작위로 섞어라
print(a) #[3, 1, 7, 9, 8, 4, 6, 10, 2, 5]

a.sort() #sort(): 오름차순 정렬 
print(a) #출력:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a.sort(reverse=True)  #sort(reverse=True): 내림차순 정렬 
print(a) #출력:[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
a.clear() #clear() : 리스트 값 모두 제거
print(a) #출력:[]
