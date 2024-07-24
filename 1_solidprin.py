"""
Solid Principle :- SOLID is a set of five object-oriented design principles that can help you write more maintainable,
flexible, and scalable code based on well-designed, cleanly structured classes.  You can follow a series of principles
 that will help you build better object-oriented code. One of the most popular and widely accepted sets of standards for
  object-oriented design (OOD) is known as the SOLID principles.

1. Single-responsibility principle (SRP)
2. Open–closed principle (OCP)
3. Liskov substitution principle (LSP)
4. Interface segregation principle (ISP)
5. Dependency inversion principle (DIP)
"""

# 1. Single-responsibility principle (SRP) :- The single-responsibility principle (SRP) comes from Robert C. Martin,
# more commonly known by his nickname Uncle Bob
"""
The single-responsibility principle states that: "A class should have only one reason to change."
"""

# Ex:-

from pathlib import Path
from zipfile import ZipFile


class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()


"""
In this example, your FileManager class has two different responsibilities. It uses the .read() and .write() methods
to manage the file. It also deals with ZIP archives by providing the .compress() and .decompress() methods.
 """


"""
To fix this issue and make your design more robust, you can split the class into two smaller, more focused classes,
 each with its own specific concern:
 """


from pathlib import Path
from zipfile import ZipFile


class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)


class ZipFileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()


"""
2. Open-Closed Principle (OCP) :- The open-closed principle (OCP) for object-oriented design was originally introduced 
                                   by Bertrand Meyer in 1988 and means that:
                                   Software entities (classes, modules, functions, etc.) should be open for extension, 
                                   but closed for modification.
Ex :-                            
"""
from math import pi


class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius**2
"""
The initializer of Shape takes a shape_type argument that can be either "rectangle" or "circle". It also takes a
 specific set of keyword arguments using the **kwargs syntax. If you set the shape type to "rectangle", then you should
  also pass the width and height keyword arguments so that you can construct a proper rectangle.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side**2

"""
In this code, you completely refactored the Shape class, turning it into an abstract base class (ABC). This class
 provides the required interface (API) for any shape that you’d like to define. That interface consists of a .shape_type
  attribute and a .calculate_area() method that you must override in all the subclasses.
"""
