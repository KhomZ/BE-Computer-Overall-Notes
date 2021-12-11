# @KhomZ

# terminate while loop 
# method #3 with continue

s = 'hello world'

while len(s) > 5:
    s = s[1:]  # in each iteration we remove one character from the string 
    # but we want the same output world.
    if len(s) > 5:  # check if length > 5 
        continue  # after this goto while 
    # as long as the string len > 5 remove one charater from the string
    # at a certain point we will reach the state that len of string is less then we don't enter the if statement 
    # and then only print statement execute
    
    print(s)