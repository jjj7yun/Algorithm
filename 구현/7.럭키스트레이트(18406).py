n=str(input())
a=n[:len(n)//2]
b=n[len(n)//2:]
aa=0
bb=0
for i in a:
    aa +=int(i)
for j in b:
    bb += int(j)
if aa == bb:
    print("LUCKY")
else:
    print("READY")
