Count numer of didgit in integer
import math
num = int(input())
ans = int(math.log(num,10)+1)
print(ans)

# Armstrong number
num = int(input())
num2 = str(num)
n = len(num2)

temp_num = num
sum_num = 0
while temp_num!=0:
    digit = temp_num%10
    sum_num += digit**n
    temp_num //= 10

print(sum_num == num)


#Prime or Not
num = int(input())
if num <= 1:
    print("Not Prime")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

# all factor
num = int(input())
factor = []
for i in range(1, int(num**0.5) + 1):
  if(num%i==0):
        factor.append(i)
        if i != num // i:
            factor.append(num // i)
print(factor)
