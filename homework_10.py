'''Поки можу тільки записувати курси і студентів у файл, переключатись між сторінками,
але коли звертаюсь до вже існуючого файлу, викидає помилку, працюю над вирішенням проблеми.'''

import json


class Pagination:
    def __init__(self, items, page_size=3):
        self.items = items
        self.page_size = page_size
        self.current_page = 0
        length = len(self.items)
        if length == 0:
            self.total_pages = 0
        else:
            self.total_pages = (length - 1) // self.page_size + 1

    def __iter__(self):
        return self

    def __next__(self):
        start_index = self.current_page * self.page_size
        end_index = start_index + self.page_size
        page_items = self.items[start_index:end_index]
        if not page_items:
            raise StopIteration
        self.current_page += 1
        return page_items

    def prev(self):
        if self.current_page > 0:
            self.current_page -= 1

    def next(self):
        if self.current_page < len(self.items) // self.page_size:
            self.current_page += 1


class FileStorage:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = {}

    @staticmethod
    def load_from_file(file_path):
        file_storage = FileStorage(file_path)
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                courses = data.get('courses', {})
                for course_name, course_data in courses.items():
                    students = set(course_data.get('students', []))
                    course_data['students'] = students
                    file_storage.data[course_name] = course_data
        except FileNotFoundError:
            pass
        return file_storage

    def save(self):
        data = {'courses': self.data}
        with open(self.file_path, 'w') as file:
            json.dump(data, file)


class App:
    def __init__(self, file_storage):
        self.file_storage = file_storage

    def add_student(self, course_name):
        course = self.file_storage.data[course_name]
        surname = input("Enter student's surname: ")
        name = input("Enter student's name: ")
        if 'students' not in course:
            course['students'] = []
        course['students'].append({'surname': surname, 'name': name})

    def show_courses(self):
        print("Courses:")
        for course_name in self.file_storage.data:
            print(course_name)

    def show_students(self, course_name):
        course = self.file_storage.data[course_name]
        students = course.get('students', [])
        student_list = [(student['surname'], student['name']) for student in students]
        paginator = Pagination(student_list)
        while True:
            try:
                print(f"Students in {course_name} (page {paginator.current_page + 1}):")
                for surname, name in next(paginator):
                    print(f"{surname} {name}")
                print("Menu:")
                print("1 - Previous page")
                print("2 - Next page")
                print("3 - Back to main menu")
                choice = int(input("Choose menu item: "))
                if choice == 1:
                    paginator.prev()
                elif choice == 2:
                    paginator.next()
                elif choice == 3:
                    break
                else:
                    print("No such menu item. Try again!")
            except StopIteration:
                print('No such pages!')

    def run(self):
        while True:
            try:
                print("Menu:")
                print("1 - Add course")
                print("2 - Show courses")
                print("3 - Add student to course")
                print("4 - Show students in course")
                print("5 - Exit")
                choice = int(input("Choose menu item: "))
                if choice == 1:
                    course_name = input("Enter course name: ")
                    self.file_storage.data[course_name] = {}
                elif choice == 2:
                    self.show_courses()
                elif choice == 3:
                    course_name = input("Enter course name: ")
                    if course_name not in self.file_storage.data:
                        print(f"Error: Course '{course_name}' not found!")
                    else:
                        self.add_student(course_name)
                        self.file_storage.save()
                elif choice == 4:
                    course_name = input("Enter course name: ")
                    if course_name not in self.file_storage.data:
                        print(f"Error: Course '{course_name}' not found!")
                    else:
                        self.show_students(course_name)
                elif choice == 5:
                    print("Exiting...")
                    break
                else:
                    print("No such menu item. Try again!")
            except ValueError:
                print("Invalid input. Try again!")


if __name__ == '__main__':
    file_path = input('Enter storage path: ')
    app = App(FileStorage.load_from_file(file_path))
    app.run()
