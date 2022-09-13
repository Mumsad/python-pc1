n=(int(input("Enter the number ")))
sum=0
y=n
while y>0:
    z=y%10
    sum=sum+z**3
    y//=10
if n==sum:
 print("Number is Armstrong")
else:
 print("Number is not Armstrong")
