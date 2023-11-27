#section2_4.대푯값 오류수정
'''
대푯값 문제 오류 수정
round는 round_half_even 방식을 택한다. 

보통 round_half_up 반올림 방식을 택한다. 
4.500 > 5 라고 함. 
하지만 파이썬에서는 round_half_even 방식이라 
가까운 근삿값중 짝수를 택함 
'''

a=4.500
print(round(a)) #출력:4 


a=4.5111
print(round(a)) #출력:5 

#따라서 반올림을 위해 파이썬의 round() 를 쓰지 않도록 한다. 

#아래로 대체한다. +0.5 후 int 화 
a=66.5 
a=a+0.5 
a=int(a)
print(a)
