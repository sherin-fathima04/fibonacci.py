def fibon(n):
  if n<=1:
    return n
  else:
    return (fibon(n-1)+fibon(n-2))
n=int(input())
l=[]
for i in range(n):
  l.append(fibon(i))
print(*l)
