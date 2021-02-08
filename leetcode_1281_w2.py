n=int(input())
sum=0
product=1 
last=0 #234%10=4 234//10=23  till n=0
while n!=0:
    last=n%10
    sum+=last
    product=product*last
    n=n//10
print(product-sum)
    
