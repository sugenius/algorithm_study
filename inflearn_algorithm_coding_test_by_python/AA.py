import sys
#sys.stdin = open("C:/work/algorithm_study/inflearn_algorithm_coding_test_by_python/input.txt","rt")
#sys.stdin = open("/input.txt","rt")

#n,m = (map(int,input().split()))
n = int(input())
result = list()
cnt = 0 

for i in range (2,n+1) : 
    for j in range (2,i) : 
        if (i%j == 0) : 
            break 
    else : 
        cnt +=1
        #result.append(i)
        
print(cnt)

#Time Limit Exceeded 

