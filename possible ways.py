v=int(input())
k=list(map(int,input().split()))[:v]
for i in range(len(k)):
    for j in range(len(k)):
         for vk in range(len(k)):
               a=k[i]+k[j]
                    if((a==k[vk]) and (i<j<vk)):
                           print(k[i],k[j],k[vk])
