"""Module that provides doing homework 9"""
import json


class JsonParser:
    """This class converts JSON objects to Python objects."""
    def json_to_python(self):
        """This function formats objects."""
        return json.loads(self.data)

    def __init__(self, data):
        self.data = data

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class Point:
    """This class accepts the coordinates of a point in a plane."""
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def as_tuple(self):
        """This function converts the coordinates to a tuple."""
        return (self.coord_x, self.coord_y)


class Rectangle:
    """This class accepts two rectangle vertices."""
    def __init__(self, start_p, end_p):
        self.start_point = start_p.as_tuple()
        self.end_point = end_p.as_tuple()

    def contains(self, point):
        """This function determines whether a point is inside a rectangle."""
        point = point.as_tuple()
        if self.start_point[0] <= point[0] <= self.end_point[0] and \
                self.start_point[1] <= point[1] <= self.end_point[1]:
            return True
        return False

    def __contains__(self, point):
        point = point.as_tuple()
        if self.start_point[0] <= point[0] <= self.end_point[0] and \
                self.start_point[1] <= point[1] <= self.end_point[1]:
            return True
        return False


if __name__ == '__main__':
    with JsonParser('"hello"') as res:
        assert res.json_to_python() == "hello"

    with JsonParser('{"hello": "world", "key": [1,2,3]}') as res:
        assert res.json_to_python() == {"hello": "world", "key": [1, 2, 3]}

    start_point = Point(1, 0)
    end_point = Point(7, 3)

    rect = Rectangle(start_point, end_point)

    assert rect.contains(start_point)
    assert not rect.contains(Point(-1, 3))

    assert start_point in rect
    assert Point(-1, 3) not in rect
    assert Point(0, 3) not in rect
    assert Point(4, 2) in rect
    assert Point(4.3, 2.2) in rect
