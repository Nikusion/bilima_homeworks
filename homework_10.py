import json


class Pagination:
    def __init__(self, items, page_size=3):
        self.items = items
        self.page_size = page_size
        self.current_page = 0

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
                file_storage.data = data.get('courses', {})
                for course_name, course_data in file_storage.data.items():
                    course_data['students'] = set(course_data.get('students', []))
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
        course[surname] = name

    def show_courses(self):
        print("Courses:")
        for course_name in self.file_storage.data:
            print(course_name)

    def show_students(self, course_name):
        course = self.file_storage.data[course_name]
        print(f"Students in {course_name}:")
        for surname, name in course.items():
            print(f"{surname} {name}")

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
                    if course_name in self.file_storage.data:
                        self.add_student(course_name)
                    else:
                        print(f"Course {course_name} does not exist!")
                elif choice == 4:
                    course_name = input("Enter course name: ")
                    if course_name in self.file_storage.data:
                        self.show_students(course_name)
                    else:
                        print(f"Course {course_name} does not exist!")
                elif choice == 5:
                    self.file_storage.save()
                    break
                else:
                    print('No such a menu item. Try again!')
            except ValueError:
                print('Input must be integer!')


if __name__ == '__main__':
    file_path = input('Enter storage path: ')
    app = App(FileStorage.load_from_file(file_path))
    app.run()
