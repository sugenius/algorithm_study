#section0_6.중첩반복문(2중for문)
'''
중첩 반복문(2중 for문)
'''


for i in range(5):
    print('i:',i,sep='',end= ' ')
    for j in range(5):
        print('j:',j,sep='', end=' ')
    print()

'''출력
i:0 j:0 j:1 j:2 j:3 j:4
i:1 j:0 j:1 j:2 j:3 j:4
i:2 j:0 j:1 j:2 j:3 j:4
i:3 j:0 j:1 j:2 j:3 j:4
i:4 j:0 j:1 j:2 j:3 j:4
'''

for i in range(5):
    for j in range(5):
        print('*',end=' ')
    print()

'''출력
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''

for i in range(5):
    for j in range(i+1):
        print('*',end=' ')
    print()

'''출력
*
* *
* * *
* * * *
* * * * *
'''

for i in range(5):
    for j in range(5-i):
        print('*',end=' ')
    print()
    
'''출력
* * * * *
* * * *
* * *
* *
*
'''