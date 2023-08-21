#section0_4.반복문(for,while,break,continue)
'''
반복문(for,while)

a=range(10) #range():순차적으로 정수 리스트를 만든다. 
print(list(a)) #츌력:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a=range(1,11)
print(list(a)) #출력:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

'''
for i in range(10): #10번 반복 
    print("hello")
    print(i)

for i in range(1,11): #1~10까지
    print(i)
    
for i in range(10,0): #이렇게 하면 안됨. 아무일도 일어나지 않음.
    print(i)
    
for i in range(10,0,-1): #이렇게 해야 -1 씩 작아짐 
    print(i)
    
'''

'''
i=1
while i<=10:
    print(i)
    i=i+1
    
i=10
while i>=1:
    print(i)
    i=i-1

i=1
while True:
    print(i)
    if i==10 :
        break
    i+=1 #i=i+1

for i in range(1,11):
    if i%2==0:
        continue
    print(i)
'''


for i in range(1,11):
    print(i)
    if i==5:
        break
else: #for문이 정상적으로 종료 되었을때 실행됨. for문 중간에 break로 중지된 경우 else 실행 되지 않음 
    print(11)