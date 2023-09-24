print("type in two positive integers and I will find its GCF, Greatest Common factor")
num1=int(input("Type in the first number: "))
num2=int(input("Type in the second number: "))
x=num1
y=num2
z=0
if num1>=num2:
 a=num2
 while z==0:
    if (a==1):
        print("the numbers, " + str(num1) + " and " + str(num2) + ", do not have a GCF")
        exit()
    else:
        if(num1%y==0):
         if(num2%y==0):
             GCF=y 
             break      
    y=y-1
    a=a-1
else:
 #num2>num1
  a=num1
  while z==0:
    if (a==1):
        print("the numbers, " + str(num1) + " and " + str(num2) + ", do not have a GCF")
        exit()
    else:
        if(num1%x==0):
         if(num2%x==0):
             GCF=x 
             break       
    x=x-1
    a=a-1
#num1=str(num1)
#num2=str(num2)

# if GCF==1:
#     print("the numbers, " + str(num1) + " and " + str(num2) + ", do not have a GCF")
# else: 
#     print("the numbers, " + str(num1) + " and " + str(num2) + ", have a GCF of " + str(GCF))
if GCF!=1:
    print("the numbers, " + str(num1) + " and " + str(num2) + ", have a GCF of " + str(GCF))