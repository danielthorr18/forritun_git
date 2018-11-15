class Student:
    def __init__(self, student_id, grades):
        self.__student_id = student_id
        self.__grades = [float(grade) for grade in grades]

    def __str__(self):
        return "Student ID: {}\nGrades: {}".format(self.__student_id, self.__grades)

    def get_average_grade(self):
        average = sum(self.__grades) / len(self.__grades)
        return average

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()

a = Student(1, [3.0, 4.6, 3.4, 5.4])
b = Student(2, [9.5, 9.0, 8.9, 9.8])