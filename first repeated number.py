vk=int(input())
a=input("")
a=list(a.split(" "))
b=[]
for c in range(0,len(a)):
  for d in range(c+1,len(a)):
    if a[c]==a[d]:
      b.append(a[c])
if(len(b)==0):
  print("unique")
else:
  print(b[0])
