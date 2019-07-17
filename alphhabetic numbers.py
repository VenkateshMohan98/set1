v=list(map(str,input()))
vk=a=0
for i in range(0,len(v)-1):
  b=v[i]
  if int(b)!=0:
    for i in range(i+1,i+2):
      b=b+v[i]
      if int(b)<27 and int(b)>0:
         vk=vk+1
      elif int(b)==0:
         vk=vk-1
      else:
         break
if vk!=1:
   a=vk%2
print(vk+a+1)
