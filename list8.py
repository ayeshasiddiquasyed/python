#1
n=9
count=0
i=1
while i*i<n:
    count+=1
    i+=1
print(count)
print("--------------")
#2
arr=[2,3,4,5,6,7,8,9]
if len(arr)<3:
    print(0)
else:
    result=sum(arr[1:-1])
    print(result)


