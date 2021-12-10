# # @khom

# def printer(a):
#     print("Hello World!", a) #code reusability

# printer(5)



# function that calculates max no.

def maximum(num1, num2):
    if num1 > num2:
        print(num1, "is greater")

    else:
        print(num2, "is greater")


    # if num1 > num2:
    #     return num1
    
    # else:
    #     return num2


number1 = int(input("enter the first number:"))
number2 = int(input("Enter the second number:"))
# maximum(3,4)
maximum(number1,number2)