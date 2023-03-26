class School:
    def __init__(self, name, city, students):
        self.name = name.capitalize()
        self.city = city.capitalize()
        self.students = students
        self.students.sort(key=lambda x: x.average, reverse=True)

    def print_students_average(self):
        for student in self.students:
            grades_summary = 0
            for subject in student.subjects:
                grades_summary = grades_summary + subject.grade
            average = grades_summary / len(student.subjects)

        for student in self.students:
            print(student.name + " " + student.last_name + " - " + str(student.average))


class Student:
    def __init__(self, name, last_name, subjects):
        self.name = name.capitalize()
        self.last_name = last_name.capitalize()
        self.subjects = subjects
        self.average = self.__get_average()

    def __get_average(self):
        grades_summary = 0
        for subject in self.subjects:
            grades_summary += subject.grade
        average = grades_summary / len(self.subjects)
        return round(average, 2)


class Subject:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


eldads_subjects = [
    Subject("math", 70),
    Subject("english", 100),
    Subject("biology", 82)
    ]
shiras_subjects = [
    Subject("math", 85),
    Subject("english", 77),
    Subject("biology", 82)
    ]
alons_subjects = [
    Subject("math", 90),
    Subject("english", 90),
    Subject("biology", 82)
    ]
eyals_subjects = [
    Subject("math", 90),
    Subject("english", 92),
    Subject("biology", 82)
    ]
rotems_subjects = [
    Subject("math", 90),
    Subject("english", 100),
    Subject("biology", 82)
    ]
hartuv_students = [
    Student("ElDad", "LeVinE", eldads_subjects),
    Student("shiRa", "Askal", shiras_subjects),
    Student("Alon", "Frank", alons_subjects),
    Student("eYal", "saKin", eyals_subjects),
    Student("roteM", "levY", rotems_subjects)
]

hartuv = School("hartuv", "tzora", hartuv_students)

hartuv.print_students_average()
