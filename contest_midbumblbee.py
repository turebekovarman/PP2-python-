#r=x+1 l=x-1 u=y+1 d=y-1
a=input()
x=int(input())
y=int(input())
coor_x=0
coor_y=0
passed=False
for i in a:
    if i=="L":
        coor_x-=1
    elif i=="R":
        coor_x+=1
    elif i=="U":
        coor_y+=1
    elif i=="D":
        coor_y-=1
    if coor_x==x and coor_y==y:
        passed=True
        break
if passed==True:
    print("Passed")
else:
    print("No")
        
    
        
    



