year=int(input("enter year:"))
if year%4==0 and year%100!=0:
    print("leap year")
elif year%100!=0:
    print("not a leap year")
else :
    print("leap year")