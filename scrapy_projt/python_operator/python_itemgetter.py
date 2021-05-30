from operator import itemgetter
from operator import attrgetter

data = [('abc', 121),('abc', 231),('abc', 148), ('abc',221),('abc', 111)]
sorted_item = sorted(data, key=itemgetter(1))
print(sorted_item)


class Student:
        def __init__(self, name, grade, age):
                self.name = name
                self.grade = grade
                self.age = age
        def __repr__(self):
                return repr((self.name, self.grade, self.age))
        def weighted_grade(self):
                return 'CBA'.index(self.grade) / float(self.age)

student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
        Student('davex', 'Bx', 7),
        Student('davey', 'By', 9),
]

sorted(student_objects, key=lambda student: student.age)


sorted_item2 = sorted(student_objects, key=attrgetter("grade"))
print(sorted_item2)

x= max(['ran', 'rana', 'sharmin'], key=len)
print(x)
