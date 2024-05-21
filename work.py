class Point:
    name = 'some_class'

    def __init__(self, color):
        self.color = color


red = Point('red')
del red.color
print(hasattr(red, 'name'))
print(hasattr(red, 'color'))

