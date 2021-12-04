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


# What is the Tower of Hanoi?
# In 1883, the Tower of Hanoi mathematical puzzle was invented by the French mathematician Edour Lucas.
# The inspiration came from a legend that states - In Ancient Hindu temple, this puzzle was presented to the young priest.
# The puzzle is, there are three poles, and 64 disks, and each disk is smaller than the other.
# To solve this problem, move all 64 disks from one of the three poles to another pole without violating the essential constraints.
# The disks can be moved one disk at a time and they should place a smaller disk top of a larger one.
# 
# Other folktale states, when they would solve this puzzle, the temple would smash into dust, and the world would end.
# But it would take a lot of time because to solve this problem 2^64 - 1 moves are necessary 
# i.e. 18,446,744,073,709,551,615 per second that is equal to 5,84,942,417,355 years according to the rules.

# Rules of the game 
# Only one disk can be moved at a time.
# The most upper disk from one of the rod can be stimulated in move.
# The smaller disk cannot be placed at the lower of the largest disk.

# Problem Approach 
# 1. Create a tower_of_hanoi recursive function and pass two arguments: the no. of disks n and the name rods such as source, aux, and target.
# 2. We can define the base case when the number of disks is 1. In this case, simply move the one disk from the source to target and return.
# 3. Now, move the remaining n-1 disks from source to auxiliary using the target as the auxiliary.
# 4. Then, the remaining 1 disk move on the source to target.
# 5. Move the n-1 disks on the auxiliary to the target using the source as the auxiliary.
