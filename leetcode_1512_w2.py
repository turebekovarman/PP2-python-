a=int(input())        
nums=[]
while a!=0:
    a-=1
    g=int(input())
    nums.append(g)
print(nums)
n=len(nums)
cnt=0
for i in range(0,n):       
    for j in range(i+1,n):
        if nums[i]==nums[j]:
            cnt+=1
print(cnt)






