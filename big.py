a=int(input("enter a number  :"))
b=int(input("enter a number  :"))
t=a
if a>b:
  t=a
else:
  t=b
print(t,"is big")
a=int(input("enter a number  :"))
b=int(input("enter a number  :"))
t=(a>b)and a or b
print(t,"is big")
