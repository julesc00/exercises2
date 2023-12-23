"""
This is a built-in function, it calls the base class implicitly and the benefit of
super function is that we don't need to define the base class name at the time of calling.
"""


class PlanDetail:
    def __init__(self, data_speed, usage_limit):
        self.data_speed = data_speed
        self.usage_limit = usage_limit


class BroadBandABC(PlanDetail):
    def __init__(self, data_speed, usage_limit, model_name):
        # Using super() in place of class names.
        super().__init__(data_speed, usage_limit)
        self.model_name = model_name


internet_obj = BroadBandABC("50kb/s", "100GB", "Broadband01234")
print(f"This plan data speed limit is {internet_obj.data_speed}")
print(f"This plan has a usage limit of {internet_obj.usage_limit}")
print(f"Broad band model name is {internet_obj.model_name}")


"""
Single inheritance with super()
Source: https://realpython.com/python-super/
"""


class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


# Here we declare that the Square class inherits from
# the Rectangle class
class Square(Rectangle):
    def __init__(self, length, **kwargs):
        """
        In Python 3, the super(Square, self) call is equivalent to the parameterless
        super() call. The first parameter refers to the subclass Square, while the
        second parameter refers to a Square object which, in this case, is self.
        You can call super() with other classes as well.

        Caution: While we are doing a lot of fiddling with the parameters to super() in
        order to explore how it works under the hood, I’d caution against doing this regularly.

        The parameterless call to super() is recommended and sufficient for most use cases,
        and needing to change the search hierarchy regularly could be indicative of a
        larger design issue.
        :param length:
        """
        super(Square, self).__init__(length=length, width=length, **kwargs)


class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super(Square, self).area()
        return face_area * self.length


"""
Multiple inheritance

When you’re using super() with multiple inheritance, it’s imperative to design your classes 
to cooperate. Part of this is ensuring that your methods are unique so that they get 
resolved in the MRO, by making sure method signatures are unique—whether by using method 
names or method parameters.

In this case, to avoid a complete overhaul of your code, you can rename the Triangle 
class’s .area() method to .tri_area(). This way, the area methods can continue using class 
properties rather than taking external parameters.
"""


class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)

    def tri_area(self):
        return 0.5 * self.base * self.height


class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(base=base, **kwargs)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area
