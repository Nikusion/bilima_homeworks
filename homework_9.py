import json


class JsonParser:
    def json_to_python(self):
        return json.loads(self.data)

    def __init__(self, data):
        self.data = data

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def as_tuple(self):
        return (self.x, self.y)


class Rectangle:
    def __init__(self, start_point, end_point):
        self.start_point = start_point.as_tuple()
        self.end_point = end_point.as_tuple()

    def contains(self, point):
        point = point.as_tuple()
        if self.start_point[0] <= point[0] <= self.end_point[0] and \
                self.start_point[1] <= point[1] <= self.end_point[1]:
            return True
        return False

    def __contains__(self, point):
        point = point.as_tuple()
        pass


if __name__ == '__main__':
    with JsonParser('"hello"') as res:
        assert res.json_to_python() == "hello"

    with JsonParser('{"hello": "world", "key": [1,2,3]}') as res:
        assert res.json_to_python() == {"hello": "world", "key": [1, 2, 3]}

    start_point = Point(1, 0)
    end_point = Point(7, 3)

    rect = Rectangle(start_point, end_point)

    rect = Rectangle(start_point, end_point)
    assert rect.contains(start_point)
    assert not rect.contains(Point(-1, 3))

    assert start_point in rect
    assert Point(-1, 3) not in rect
