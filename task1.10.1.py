class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_attribute(self):
        return str(self.x), str(self.y), str(self.width), str(self.height)


new_rectangle = Rectangle(12, 21, 22, 22)

print('Rectangle',new_rectangle.get_attribute())

