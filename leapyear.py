year=int(input("enter year  :"))
if(year%4==0):
  if(year%100!=0):
    if(year%4==0):
      print("leap year")
else:
  print("not a leap year")
