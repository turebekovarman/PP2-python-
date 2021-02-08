   #-5,1,5,0,-7  a=0 ->-5 -5+1 -4+5 1+0 max=?
n=int(input())        #max=0 -5 -5 1 -5<1 1
list=[]
while n!=0:
    n-=1
    g=int(input())
    list.append(g)
print(list)
a=0
maxi=0
for i in list:
    a+=i
    if a>maxi:
        maxi=a
print(maxi)



