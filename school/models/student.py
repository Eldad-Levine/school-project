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








