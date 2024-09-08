#Find the number of digits in the given number
n=abs(int(input("enter number")))
num=n
digit=1
while(num>9):
    num=num//10
    digit=digit+1
print("no. of digit of",n,"is",digit)