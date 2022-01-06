from sys import stdin
from bisect import bisect_left, bisect_right
r=stdin.readline
n=int(r())
array = list(map(int,r().split()))
index=None
for i in array:
    if bisect_right(array,i) == i or bisect_left(array,i) == i:
        index=i
        break
if index == None:
    print(-1)
else:
    print(index)
