from bisect import bisect_left, bisect_right
from sys import stdin
r=stdin.readline
n,c = map(int,r().split())
graph=[0]*(n+1)
array=[]
for _ in range(n):
    data = int(r())
    array.append(data)
    graph[data]=data
start=1
end=array[-1]-array[0]
answer=0

def binary_research(array,start,end):

    while start<=end:
        mid = (start + mid) // 2
        count = 1
        now = array[0]
        for i in range(1,len(array)):
            if array[i] >= mid + now:
                count+=1
                


