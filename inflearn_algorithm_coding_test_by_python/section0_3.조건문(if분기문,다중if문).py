#section0_3.조건문(if분기문, 다중if문)
'''
조건문 if(분기, 중첩)
'''

'''
x=7
if x==7: #if x!=7 
    #파이썬 문법 특징! 기본 공백4칸:이 문장은 if문에 속한 문장이다. 
    print("Lucky")
    print("ㅋㅋ")
'''

'''
x=15
if x>=10: 
    if x%2==1:
        print("10이상의 홀수")

x=9
if x>0:
    if x<10:
        print("10보다 작은 자연수")

x=7
if x>0 and x<10:
    print("10보다 작은 자연수")

if 0<x<10: #파이썬만 본 구문 가능
    print("10보다 작은 자연수")
'''


x=10
if x>0:
    print("양수")
else :
    print("음수")
        

x=93
if x>=93:
    print('A') #쌍따옴표 "" , 따옴표'' 상관없음. 
elif x>=80:
    print('B')
elif x>=70:
    print("C")
elif x>=60:
    print("D")
else:
    print("F")
    

if x>=93:
    print('A') #쌍따옴표 "" , 따옴표'' 상관없음. 
if x>=80:
    print('B')
if x>=70:
    print("C")
    