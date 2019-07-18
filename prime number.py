v,k=map(int,input().split())
for i in range (v+1,k):
  for j in range (2,i):
    if (i%j==0):
      break
  else:
      print(i,end=" ")
