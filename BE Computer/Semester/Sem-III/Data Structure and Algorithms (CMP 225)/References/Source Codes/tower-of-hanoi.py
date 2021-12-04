# @author : Khom

# Python Program to solve the Tower of Hanoi.
# Recursive Python function to solve the tower of hanoi

# def TowerOfHanoi(n, source, destination, auxiliary):
#     if n == 1:
#         print("Move disk 1 from source", source, "to destination", destination)
#         return

#     else:
#         TowerOfHanoi(n-1, source, auxiliary, destination)
#         print("Move disk",n,"from source", source, "to destination", destination)
#         TowerOfHanoi(n-1, auxiliary, destination, source)

# # Driver Code
# # n = 4
# n = int(input('Pick a number for Tower of Hanoi!'))
# TowerOfHanoi(n,'A','B','C')
# # A, C, B are the name of rods



# # outputs
# for n = 4
# Move disk 4 from source A to destination B
# Move disk 1 from source C to destination B
# Move disk 2 from source C to destination A
# Move disk 1 from source B to destination A
# Move disk 3 from source C to destination B
# Move disk 1 from source A to destination C
# Move disk 2 from source A to destination B
# Move disk 1 from source C to destination B

# this is wrong


# refer: https://www.geeksforgeeks.org/python-program-for-tower-of-hanoi/





# Creating a recursive function
def tower_of_hanoi(disks, source, auxiliary, target):
    if(disks == 1):
        
        print('Move disk 1 from rod {} to rod {}.'.format(source, target))

        return

    # function call itself
    tower_of_hanoi(disks - 1, source, target, auxiliary)
    print('Move disk {} from rod {} to rod {}.'.format(disks, source, target))
    tower_of_hanoi(disks - 1, auxiliary, source, target)

disks = int(input('Enter the number of disks:'))
# We are referring source as A, auxiliary as B, and target as C.

tower_of_hanoi(disks, 'A', 'B', 'C')  # Calling the function


# outputs
#  for n = 4
# Move disk 1 from rod A to rod B.
# Move disk 4 from rod A to rod C.
# Move disk 1 from rod B to rod C.
# Move disk 2 from rod B to rod A.
# Move disk 1 from rod C to rod A.
# Move disk 3 from rod B to rod C.
# Move disk 1 from rod A to rod B.
# Move disk 2 from rod A to rod C.
# Move disk 1 from rod B to rod C.