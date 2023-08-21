#section0_7.문자열과 내장함수
'''
문자열과 내장함수
'''
msg="It is Time"
print(msg.upper()) #출력:IT IS TIME. upper():대문자화
print(msg.lower()) #출력:it is time. lower():소문자화
print(msg) #출력:It is Time

tmp=msg.upper()
print(tmp)
print(tmp.find('T')) #출력:1. find():인덱스 가져오기
print(tmp.count('T')) #출력:2. count():갯수 가져오기

print(msg)
print(msg[:2]) #출력:It. 0~1 인덱스만 가져오기
print(msg[3:5]) #출력:is. 3~4 인덱스만 가져오기

print(len(msg)) #출력:10. len():길이
for i in range(len(msg)):
    print(msg[i],end=' ')
#출력:I t   i s   T i m e
print()

for x in msg:
    print(x,end=' ')
#출력:I t   i s   T i m e
print()

for x in msg:
    if x.isupper(): #isupper() : 대문자인가?
        print(x,end=' ')
#출력:I T
print()

for x in msg:
    if x.islower(): #islower() : 소문자인가?
        print(x,end=' ')
#출력:t i s i m e      
print()

for x in msg:
    if x.isalpha(): #isalpha() : 알파멧인가?
        print(x,end=' ')
#출력:I t i s T i m e
print()

tmp='AZ'
for x in tmp:
    print(ord(x)) #ord():ASCII NUMBER 
'''출력:
65
90
'''

tmp='az'
for x in tmp:
    print(ord(x)) #ord():ASCII NUMBER 
'''출력:
97
122
'''

tmp=65
print(chr(tmp)) #chr():문자
#출력:A