class School:
    def __init__(self, name, city, students):
        self.name = name.capitalize()
        self.city = city.capitalize()
        self.students = students
        self.students.sort(key=lambda x: x.average, reverse=True)

    # # def print_students_by_min_grade(self, grade):
    #     self.students.sort(key=lambda x: x.grade, reverse=True)
    #     for student in self.students:
    #         if student.grade >= grade:
    #             print(student.name + " " + student.last_name + " - " + str(student.grade))

    def print_students_average(self):
        # for student in self.students:
        #     grades_summary = 0
        #     for subject in student.subjects:
        #         grades_summary = grades_summary + subject.grade
        #     average = grades_summary / len(student.subjects)

        #     print(student.name + " " + student.last_name + " - " + str(average))
        for student in self.students:
            print(student.name + " " + student.last_name + " - " + str(student.average))

    def example_for_git(self):
        return



