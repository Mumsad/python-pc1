nterm=(int(input("How many terms :")))
n1,n2=0,1
count=0
print("FIBONACCI SEQUENCE")
while count<nterm:
 print(n1)
 nth=n1+n2
 n1=n2
 n2=nth
 count+=1
