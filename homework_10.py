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
    def __init__(self, data, file_path):
        self.data = data
        self.file_path = file_path

    @staticmethod
    def load_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        for course_data in data.values():
            course_data['students'] = list(course_data.get('students', []))
        return FileStorage(data, file_path)

    def save(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, default=lambda x: list(x) if isinstance(x, set) else x)



class App:
    def __init__(self, file_storage):
        self.file_storage = file_storage

    def add_course(self, course_name):
        self.file_storage.data[course_name] = {}
        self.file_storage.save()

    def add_student(self, course_name):
        course = self.file_storage.data[course_name]
        if 'students' not in course.keys():
            course['students'] = []
        surname = input("Enter student's surname: ")
        name = input("Enter student's name: ")
        course['students'].append({'surname': surname, 'name': name})
        self.file_storage.save()

    def show_courses(self):
        course_list = list(self.file_storage.data.keys())
        paginator = Pagination(course_list)
        while True:
            try:
                print(f"Courses (page {paginator.current_page + 1}):")
                for course_name in next(paginator):
                    print(course_name)
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
                break

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
                break

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
                    self.add_course(course_name)
                elif choice == 2:
                    self.show_courses()
                elif choice == 3:
                    course_name = input("Enter course name: ")
                    if course_name not in self.file_storage.data:
                        print(f"Error: Course '{course_name}' not found!")
                        continue
                    self.add_student(course_name)
                elif choice == 4:
                    course_name = input("Enter course name: ")
                    if course_name not in self.file_storage.data:
                        print(f"Error: Course '{course_name}' not found!")
                        continue
                    self.show_students(course_name)
                elif choice == 5:
                    break
                else:
                    print("No such menu item. Try again!")
            except ValueError:
                print("Invalid input. Try again!")


if __name__ == '__main__':
    file_path = input('Enter storage path: ')
    app = App(FileStorage.load_from_file(file_path))
    app.run()
