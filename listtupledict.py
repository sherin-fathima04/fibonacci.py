n=int(input())
l=[]
for i in range(n):
  l.append(int(input()))
print(l)
l2=[1,2,3]
l2=l+l2
print(l2)
l2.pop(len(l2)-1)
l2.insert(1,1)
print(l2)
t=tuple(l2)
print(t[3:])
d=dict()
for i in t:
  d[i]=d.get(i,0)+1
print(d)
del d[1]
print(d)
