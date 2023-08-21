#section2_4.[선수지식] 최솟값 구하기

arr=[5,3,7,9,2,5,2,6]
arrMin=float('inf') #float('inf'):양의무한대. 파이썬에서 가장 큰 값으로 초기화 
for i in range(len(arr)):
    #print(arr[i])
    if(arr[i])<arrMin: #첫번째는 무조건 참이 되게 함.
        arrMin=arr[i]
        
'''또는 
arrMin=float('inf')
for i in arr:
    if x<arrMin:
        arrMin=x
'''

'''또는 
arrMin=a[0] #첫번째 요소로 초기화 하고
for i in range (1,len(arr)) #1부터 돌게 한다. 
'''
print(arrMin)