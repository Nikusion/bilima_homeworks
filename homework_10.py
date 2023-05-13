import json


class FileStorage:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = {}

    @staticmethod
    def load_from_file(file_path):
        file_storage = FileStorage(file_path)
        try:
            with open(file_path, 'r') as file:
                file_storage.data = json.load(file)
        except FileNotFoundError:
            pass
        return file_storage

    def save(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file)


class App:
    def __init__(self, file_storage):
        self.file_storage = file_storage

    def run(self):
        while True:
            try:
                print("Menu:")
                print("1 - Add course")
                print("2 - Show courses")
                print("3 - Exit")
                choice = int(input("Choose menu item: "))
                if choice == 1:
                    course_name = input("Enter course name: ")
                    self.file_storage.data[course_name] = {}
                elif choice == 2:
                    print("Courses:")
                    for course_name in self.file_storage.data:
                        print(course_name)
                elif choice == 3:
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
