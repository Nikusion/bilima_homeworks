import unittest
from homework_10 import Pagination, FileStorage, Student, Course, App
import os
from unittest.mock import patch
from io import StringIO


class FileStorageTest(unittest.TestCase):
    FILE_PATH = 'test_file.json'

    def setUp(self):
        self.data = {
            'course1': {
                'students': [
                    {'surname': 'Smith', 'name': 'John'},
                    {'surname': 'Doe', 'name': 'Jane'}
                ]
            },
            'course2': {
                'students': [
                    {'surname': 'Johnson', 'name': 'Michael'},
                    {'surname': 'Brown', 'name': 'Emily'}
                ]
            }
        }
        self.storage = FileStorage(self.data, self.FILE_PATH)

    def tearDown(self):
        if os.path.exists(self.FILE_PATH):
            os.remove(self.FILE_PATH)

    def test_save_and_load_from_file(self):
        self.storage.save()

        self.assertTrue(os.path.exists(self.FILE_PATH))

        loaded_storage = FileStorage.load_from_file(self.FILE_PATH)

        self.assertEqual(loaded_storage.data, self.data)


class PaginationTest(unittest.TestCase):
    def test_pagination_with_4_items(self):
        items = [1, 2, 3, 4]
        pagination = Pagination(items)

        self.assertEqual(next(pagination), [1, 2, 3])
        pagination.next()

        self.assertEqual(next(pagination), [4])
        pagination.next()

        pagination.prev()
        self.assertEqual(next(pagination), [1, 2, 3])

        pagination.prev()
        self.assertEqual(next(pagination), [1, 2, 3])

    def test_pagination_with_empty_list(self):
        items = []
        pagination = Pagination(items)

        self.assertEqual(next(pagination), [])

    def test_pagination_with_multiple_of_3_items(self):
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        pagination = Pagination(items)

        self.assertEqual(next(pagination), [1, 2, 3])
        pagination.next()

        self.assertEqual(next(pagination), [4, 5, 6])
        pagination.next()

        self.assertEqual(next(pagination), [7, 8, 9])

        pagination.prev()
        self.assertEqual(next(pagination), [4, 5, 6])


class TestApp(unittest.TestCase):

    def setUp(self):
        self.file_path = 'test_data.json'
        self.storage = FileStorage.load_from_file(self.file_path)
        self.app = App(self.storage)

    def tearDown(self):
        self.storage.save()

    def test_add_course(self):
        course_name = 'Math'
        self.app.add_course(course_name)
        self.assertIn(course_name, self.storage.data)
        self.assertEqual(self.storage.data[course_name]['students'], [])

    def test_show_courses(self):
        courses = ['Math', 'Physics', 'Chemistry']
        self.storage.data.update({course: {'students': []} for course in courses})
        with patch('builtins.input', side_effect=['2', '3']):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.app.show_courses()
                output = fake_out.getvalue().strip()
                expected_output = 'Courses (page 1):\nMath\nPhysics\nChemistry\nMenu:\n1 ' \
                                  '- Previous page\n2 - Next page\n3 - Back to main menu'
                self.assertIn(expected_output, output)

    def test_add_student(self):
        course_name = 'Math'
        student_surname = 'Smith'
        student_name = 'John'

        with patch('builtins.input', side_effect=[1, student_surname, student_name]):
            self.app.add_student(course_name)

        self.assertEqual(self.storage.data[course_name]['students'][0].surname, student_surname)
        self.assertEqual(self.storage.data[course_name]['students'][0].name, student_name)

    def test_show_students(self):
        course_name = 'Math'
        students = [
            {'surname': 'Smith', 'name': 'John'},
            {'surname': 'Doe', 'name': 'Jane'},
            {'surname': 'Johnson', 'name': 'Michael'},
            {'surname': 'Brown', 'name': 'Emily'},
            {'surname': 'Davis', 'name': 'Jessica'},
            {'surname': 'Taylor', 'name': 'David'}
        ]
        self.storage.data[course_name]['students'] = [Student(s['surname'], s['name']) for s in students]

        with patch('builtins.input', side_effect=['2', '3']):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.app.show_students(course_name)
                output = fake_out.getvalue().strip()
                expected_output = 'Students in Math (page 1):\nSmith John\nDoe Jane\nJohnson Michael\nMenu:\n1 ' \
                                  '- Previous page\n2 - Next page\n3 - Back to main menu'
                self.assertIn(expected_output, output)


if __name__ == '__main__':
    unittest.main()
