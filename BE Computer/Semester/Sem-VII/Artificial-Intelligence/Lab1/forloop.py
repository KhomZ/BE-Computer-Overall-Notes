# @Khom
# for loop in python

# for(i=0; i<10; i++)  CPP code
# for i in range(10): #0 to 9
# for i in range(2,10): # 2 to 9
# for i in range(10,2,-1): # printing no. 10 to 3
#     print(i)

num = int(input("Enter a number "))

fac = 1
for i in range(num):
    fac = fac*num
    num -= 1

# # or use this code
# for i in range(0,num,-1):
#     fac = fac * num

print(fac)



# # source: TheCrazyProgrammer
# num = int(input("enter a number: "))
 
# fact1 = 1
 
# for i in range(1, num + 1):
#     fact1 = fact1 * i


 
# print("factorial of ", num, " is ", fact1)
