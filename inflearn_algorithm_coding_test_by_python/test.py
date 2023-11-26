import sys
sys.stdin = open("C:/work/algorithm_study/inflearn_algorithm_coding_test_by_python/input.txt","rt")
#sys.stdin=open("input.txt","rt")

#n = int(input())
#n,m = map(int, input().split())
#a = list(map(int, input().split()))
#a=[list(map(int,input().split())) for _ in range(n)]

def test(a,b,c,d) :
    arr=[a,b,c,d]
    count = [arr.count(i) for i in arr]
    return print(count)

test(2,2,2,2)