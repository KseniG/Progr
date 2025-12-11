class Student:
    def __init__(self, surname, name):
        self._name = name
        self._surname = surname
        self._marks = [3,3,4,5,5,4,5]
    def get_full_name(self):
        return (self._name," ",self._surname)
    def add_mark(self, mark):
        if int(mark)>0 and int(mark)<=5:
            return self._marks.append(int(mark))
        return(print('Error'))
    def get_average_mark(self):
        return sum(self._marks)/len(self._marks)

student = Student(input('fname: '), input('name:'))
student.add_mark(int(input('mark: ')))
print(student.get_full_name())
print(student.get_average_mark())
