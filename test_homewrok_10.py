import unittest
import json
from homework_10 import Pagination
from tempfile import NamedTemporaryFile
import os


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

# class TestFileStorage(unittest.TestCase):
#     def setUp(self):
#         self.temp_file = NamedTemporaryFile(delete=False)
#         self.file_path = self.temp_file.name
#
#     def tearDown(self):
#         self.temp_file.close()
#         os.remove(self.file_path)
#
#     def test_load_from_file(self):
#         # Перевірка, чи коректно завантажуються дані з файлу
#         data = {
#             'course1': {'students': [{'surname': 'Smith', 'name': 'John'}, {'surname': 'Doe', 'name': 'Jane'}]},
#             'course2': {'students': [{'surname': 'Johnson', 'name': 'Robert'}, {'surname': 'Brown', 'name': 'Emily'}]}
#         }
#         # Запис даних у тимчасовий файл
#         with open(self.file_path, 'w') as file:
#             file.write(json.dumps(data))
#         # Завантаження даних з файлу
#         storage = FileStorage.load_from_file(self.file_path)
#         # Перевірка, чи збережені дані відповідають очікуваним
#         self.assertEqual(storage.data, data)


if __name__ == '__main__':
    unittest.main()
