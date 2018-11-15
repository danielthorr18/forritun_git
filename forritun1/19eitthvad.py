# Write the class "Student". The class has the attributes student_id which is an integer and a list of 4 grades. 
# The class has the following methods:
# A constructor that takes two parameters: the student‘s ID (an integer), the student's grades 
# (as a list of strings). 
# The constructor uses the parameters to initializes the attributes and convert the grades to a list of floats.
# You need to implement functionality so that a Student instance can be printed using the print() function. 
# When printed the Student shoud be printed as follows:
#                 Student ID: 173
#                 Grades: [5.37, 4.65, 9.85, 10.00]
# you should override the < operator which checks whether an instance of the class is less than another 
#  instance of the class. The comparison is made using the average grade of the instances.
# Here is a main function that should work. Read in thoroughly to figure out how you implement the Student class.
# def main():
#     student_id = input("Enter student ID: ")
#     grades = input("Enter 4 grades seperated by a comma").split(",")
#     john = Student(student_id, grades)
#     student_id = input("Enter student ID: ")
#     grades = input("Enter 4 grades seperated by a comma").split(",")
#     alice = Student(student_id, grades)
#     print("John's info")
#     print(john)
#     if (john < alice):
#         print("John has a lower average grade than Alice")
#     else:
#         print("Alice has a lower average grade than John")



# You should only hand in the code for the class
class Student:
    def __init__(self, student_id=0, grades=[]):
        self.__student_id = student_id
        self.grades = [float(x) for x in grades]

    def __str__(self):
        return "Student ID: {}\nGrades: {}".format(self.__student_id, self.grades)
    
    def average_grade(self):
        the_sum = sum(self.grades)
        the_length = len(self.grades)
        return the_sum/the_length
    
    def __lt__(self, new_student):
        av1 = self.average_grade()
        av2 = new_student.average_grade()
        if av1 < av2:
            return True
        else:
            return False



def main():
    student_id = input("Enter student ID: ")
    grades = input("Enter 4 grades seperated by a comma").split(",")
    john = Student(student_id, grades)

    student_id = input("Enter student ID: ")
    grades = input("Enter 4 grades seperated by a comma").split(",")
    alice = Student(student_id, grades)

    print("John's info")
    print(john)

    if (john < alice):
        print("John has a lower average grade than Alice")
    else:
        print("Alice has a lower average grade than John")

main()