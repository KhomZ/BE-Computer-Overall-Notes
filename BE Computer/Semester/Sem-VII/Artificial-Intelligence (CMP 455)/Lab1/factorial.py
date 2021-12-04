# @KHOM
# Factorial of a number using while loop
# eg. 5!=5*4*3*2*1

num = int(input("enter a number: "))
 
factorial = 1
i = 1
 
while i <= num:
    factorial = factorial * i
    i = i + 1
 
print("factorial of ", num, " is ", factorial)



# # sir's logic
# num = input('enter a no.')

# fac = 1
# while(num>0):
#     fac = fac*num
#     num -= 1
# print(fac)