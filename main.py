
# class BookNumber:

#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def info(self):
#         print(f'Name: {self.title}\n'
#               f'Author: {self.author}\n'
#               f'Pages: {self.pages}')
        
#     def size(self):
#         if self.pages > 300:
#             print('The book is large')
#         else:
#             print('The book is ok')
    

# book1 = BookNumber('Bruh', "Slay", 340)
# book1.info()
# book1.size()



#

class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def set_grade(self, grade):
        self.grade = grade

    def get_grade(self):
        if self.grade is None:
            print("Student doesn't have the grade")
        else:
            print(f"Student's grade: {self.grade}")


student1 = Student(99, 'Dariya')
student1.get_grade()
student1.set_grade(99)
student1.get_grade()
        