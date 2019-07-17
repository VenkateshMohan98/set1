v=int(input())
v=list(map(int,input().split()))
for i in range(len(v)):
    if((i%2==0)and(v[i]%2!=0)or(i%2!=0)and(v[i]%2==0)):
        print(v[i],end=" ")
