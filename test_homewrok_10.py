import unittest
import json
from homework_10 import FileStorage
from tempfile import NamedTemporaryFile
import os


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.temp_file = NamedTemporaryFile(delete=False)
        self.file_path = self.temp_file.name

    def tearDown(self):
        self.temp_file.close()
        os.remove(self.file_path)

    def test_load_from_file(self):
        # Перевірка, чи коректно завантажуються дані з файлу
        data = {
            'course1': {'students': [{'surname': 'Smith', 'name': 'John'}, {'surname': 'Doe', 'name': 'Jane'}]},
            'course2': {'students': [{'surname': 'Johnson', 'name': 'Robert'}, {'surname': 'Brown', 'name': 'Emily'}]}
        }
        # Запис даних у тимчасовий файл
        with open(self.file_path, 'w') as file:
            file.write(json.dumps(data))
        # Завантаження даних з файлу
        storage = FileStorage.load_from_file(self.file_path)
        # Перевірка, чи збережені дані відповідають очікуваним
        self.assertEqual(storage.data, data)

    def test_save(self):
        # Перевірка, чи коректно зберігаються дані у файл
        data = {
            'course1': {'students': [{'surname': 'Smith', 'name': 'John'}, {'surname': 'Doe', 'name': 'Jane'}]},
            'course2': {'students': [{'surname': 'Johnson', 'name': 'Robert'}, {'surname': 'Brown', 'name': 'Emily'}]}
        }
        storage = FileStorage(data, self.file_path)
        storage.save()
        with open(self.file_path, 'r') as file:
            saved_data = json.load(file)
        self.assertEqual(saved_data, data)


if __name__ == '__main__':
    unittest.main()
