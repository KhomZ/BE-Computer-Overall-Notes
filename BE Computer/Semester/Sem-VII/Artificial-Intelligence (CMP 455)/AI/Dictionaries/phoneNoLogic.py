# Dictionaries: Key value pair data strucure
phoneNumber = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine"
}

phone = input("Enter your phone number")
translated = " "

for i in phone:
    # print(i)
    translated += phoneNumber.get(i)
    # print(phoneNumber.get(i))

print(translated)