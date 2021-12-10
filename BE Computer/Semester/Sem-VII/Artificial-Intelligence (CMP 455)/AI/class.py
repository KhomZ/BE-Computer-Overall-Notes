# @ai lab
class Student:
    name = "Khom"
    faculty = "Computer"
    address = "Pokhara"

    def printer(self):
        def assign(self, name, faculty, address):
            self.name1 = name
            self.faculty = faculty
            self.address = address


        print(self.name, self.faculty, self.address)
        #self represents the instance of the class. 
        # By using the “self” keyword we can access the attributes and methods of the class in python. 
        # It binds the attributes with the given arguments. 
        # The reason you need to use self. is because Python does not use the @ syntax to refer to instance attributes.
# print(name)  #NameError since class is for data encapsulation

s = Student()  # s is an objecgt of Student
# print(s.name)
s.assign("Khom", "Computer", "Pkr")