#Convert Binary number to decimal
b_num=list(input("Input a binary number: "))
value = 0
for i in range(len(b_num)):
    digit = b_num.pop()
    if digit == '1':
        value = value + pow(2, i)
print("The decimal value of the number is",value)




#Generate first N number of Fibonacci numbers. Take N value from user
n = int(input("Enter the value of 'n': "))
a=0
b=1
print("Fibonacci Series:")
for i in range(1,n+1):
  print(a,end='\t')
  c=a+b
  a=b
  b=c




#Display multiplication table of K. Take k value from user
num = int(input("Enter a number:"))
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)




#Take 10 integers from keyboard using loop and print their average value on the screen and print the pattern using loop
l1=[]
for i in range(0,10):
    x=int(input("Enter number:"))
    l1.append(x)
suml=sum(l1)/10
print("average=",suml)
for j in range(5):
    for k in range(j):
        print("*",end=' ')
    print('\n')