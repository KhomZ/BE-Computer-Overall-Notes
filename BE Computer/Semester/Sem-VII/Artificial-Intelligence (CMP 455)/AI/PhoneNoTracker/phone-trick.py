# @List in dictionaries

# @Dictionaries = curly braces used in here

# hello: greeting word 


phoneDict = {
    'name' : ['khom', 'Sanjay', 'Princ', 'Gorebox', 'Ohmm'],
    'phoneNo' : 9825120461,
    'address' : 'Pokhara'
}

q1 = int(input('enter phone no.'))
if q1 == phoneDict["phoneNo"]:
    print(phoneDict["name"][0])











# studentDict = {
#     "name" : "Khom",
#     "faculty" : "Computer",
#     "rollNo" : 171347,
#     "address" : "Pokhara",
#     "girlfriend" : ["rita", "gita", "sita", "etc"]  
# }

# print(studentDict["girlfriend"][0])
# print(studentDict)
# output
# {'name': 'Khom', 'faculty': 'Computer', 'rollNo': 171347, 'address': 'Pokhara'}


# print(studentDict["faculty"])
# print(studentDict["facultyyyy"]) # error 

# print(studentDict.get("facultyy", "Key nai payena")) #get key error is not found

