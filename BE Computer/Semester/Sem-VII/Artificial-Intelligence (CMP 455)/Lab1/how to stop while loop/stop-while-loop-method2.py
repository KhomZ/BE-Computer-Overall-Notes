# @KhomZ

# terminate while loop 
# method #2 with break

s = 'hello world'

while True:
    # None
    if len(s) > 5:
        s = s[1:]
    else:
        break

print(s)

