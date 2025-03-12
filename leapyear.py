year=int(input("enter year :"))
if(year%4==0 and year %100!=0)or(year%400==0):
    print("leap year")
else:
    print("not leap year")
print("----------------")
x='12344321'
if x==x[::-1]:
    print("palindrome")
else:
    print("not a palindrome")
print("----------------")
x=input("enter alphabet:").lower()
if x in('a','e','i','o','u'):
    print("voels")
else:
    print("consonant")
print("--------------")
x=input("enter color  :").lower()
if x in ('red'):
    print('stop')
elif x in('yellow'):
    print('slow')
else:
    print('Go')


