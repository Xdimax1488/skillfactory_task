from main import Rectangle, Square, Circle

rect_1 = Rectangle(2, 4)
rect_2 = Rectangle(3, 5)

# print(rect_1.get_area())
# print(rect_2.get_area())


square_1 = Square(3)
square_2 = Square(4)

# print(square_1.get_area_square(),square_2.get_area_square())

circle_1 = Circle(3)
circle_2 = Circle(4)

figurs = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]

for figure in figurs:
    if isinstance(figure, Rectangle):
        print(figure.get_area())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())

    else:
        print(figure.get_area_square())
