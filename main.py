import math
# 1
n = int(input("Please enter  a value of n :"))
x = int(input("Please enter a number of x : "))

result = [(lambda i : n**i/math.factorial(i))(i) for i in range(x+1)]
result2 = sum(result)
result2 +=1
print("e^",n,"=",result2)

#2

sum = 0
first_input = int(input("Please enter a number : "))
def calcSum(n):
    global sum
    if n == 0:
        return
    else:
        sum += (-1)**(n+1)/n
        calcSum(n-1)

calcSum(first_input)
print("Sum is :  " , sum)