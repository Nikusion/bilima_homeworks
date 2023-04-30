"""Module that provides doing homework 8"""


class Student:
    """This class takes two arguments: firstname and
    lastname and returns data about the student
    in the form of a dictionary."""

    def __init__(self, first_name, last_name):
        """This function allows you to accept
        arguments from outside the class."""
        self.first_name = first_name
        self.last_name = last_name

    def info(self):
        """This function returns data about
        the student in the form of a dictionary."""
        return {'first_name': self.first_name, 'last_name': self.last_name}


class Storage:
    """This class stores the words added by the user
    and can return a sorted list (up to 5 elements long)."""

    storage = []

    def get(self, letter):
        """This function accepts one argument (a word),
        by which we will search. Should return an alphabetically
        sorted list of words that were added by the add method
        and begin with the entered letters (value of the function argument).
        The length of the list should not exceed 5 elements."""
        storage_sort = []
        for thing in self.storage:
            if thing.startswith(letter):
                storage_sort.append(thing)
        storage_sort.sort()
        return storage_sort[:5]

    def add(self, thing):
        """This function takes one argument (a word) which we will store."""
        self.storage.append(thing)


class Course:
    """This class stores the name of the course
    and the students of the course."""
    students = []

    def __init__(self, name):
        """This function allows you to accept
        arguments from outside the class."""
        self.name = name

    def add_student(self, inform):
        """This function takes one argument in the form of objects
        of the Student class (the first one in this homework) and
        adds students to the course."""
        stud = inform.info()
        self.students.append(stud)
        return self.students

    def to_json(self):
        """This function takes no arguments and converts
        the contents of the Student class object
        into a json object (a dictionary of data types
        supported by the json protocol) and contains
        data about the name of the course and all
        students enrolled in the course."""
        return {'name': self.name, 'students': self.students}


if __name__ == '__main__':
    student = Student('John', 'Doe')
    assert student.info() == {'first_name': 'John', 'last_name': 'Doe'}

    fruits_storage = Storage()
    assert not fruits_storage.get('')
    assert not fruits_storage.get('apple')

    fruits_storage.add('plum')
    fruits_storage.add('apple')
    fruits_storage.add('peach')
    fruits_storage.add('apricot')
    fruits_storage.add('pineapple')

    assert fruits_storage.get('') == ['apple', 'apricot',
                                      'peach', 'pineapple', 'plum']
    assert fruits_storage.get('a') == ['apple', 'apricot']
    assert fruits_storage.get('p') == ['peach', 'pineapple', 'plum']
    assert not fruits_storage.get('abc')

    fruits_storage.add('pear')

    assert fruits_storage.get('') == ['apple', 'apricot',
                                      'peach', 'pear', 'pineapple']

    python_basic = Course('Python basic')
    python_basic.add_student(Student('Jane', 'Doe'))
    assert python_basic.to_json() == {
        'name': 'Python basic',
        'students': [{'first_name': 'Jane', 'last_name': 'Doe'}],
    }

    python_basic.add_student(Student('John', 'Doe'))
    assert python_basic.to_json() == {
        'name': 'Python basic',
        'students': [
            {'first_name': 'Jane', 'last_name': 'Doe'},
            {'first_name': 'John', 'last_name': 'Doe'},
        ],
    }
