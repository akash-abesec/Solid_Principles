"""
Liskov Substitution Principle (LSP) :- The Liskov substitution principle (LSP) was introduced by Barbara Liskov at an
 OOPSLA conference in 1987.
"""

"""
The principle states that:

Subtypes must be substitutable for their base types.
"""

"""
For example, if you have a piece of code that works with a Shape class, then you should be able to substitute that class
 with any of its subclasses, such as Circle or Rectangle, without breaking the code.
"""


# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):
#         return self.width * self.height


"""
Because a square is a special case of a rectangle with equal sides, you think of deriving a Square class from Rectangle
 in order to reuse the code.
"""


# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
#
#     def __setattr__(self, key, value):
#         super().__setattr__(key, value)
#         if key in ("width", "height"):
#             self.__dict__["width"] = value
#             self.__dict__["height"] = value


"""
In this snippet of code, you’ve defined Square as a subclass of Rectangle. As a user might expect, the class constructor
takes only the side of the square as an argument. Internally, the .__init__() method initializes the parent’s 
attributes, .width and .height, with the side argument.
"""

# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):
#         return self.width * self.height
#
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def calculate_area(self):
#         return self.side ** 2
#


"""
Interface Segregation Principle (ISP) :- The interface segregation principle (ISP) comes from the same mind as the
 single-responsibility principle. Yes, it’s another feather in Uncle Bob’s cap. 
 The principle’s main idea is that:
 
"Clients should not be forced to depend upon methods that they do not use. Interfaces belong to clients, 
not to hierarchies. "
"""

"""
In this case, clients are classes and subclasses, and interfaces consist of methods and attributes. In other words, 
if a class doesn’t use particular methods or attributes, then those methods and attributes should be segregated into
 more specific classes.
"""

# from abc import ABC, abstractmethod
#
#
# class Printer(ABC):
#     @abstractmethod
#     def print(self, document):
#         pass
#
#     @abstractmethod
#     def fax(self, document):
#         pass
#
#     @abstractmethod
#     def scan(self, document):
#         pass
#
#
# class OldPrinter(Printer):
#     def print(self, document):
#         print(f"Printing {document} in black and white...")
#
#     def fax(self, document):
#         raise NotImplementedError("Fax functionality not supported")
#
#     def scan(self, document):
#         raise NotImplementedError("Scan functionality not supported")
#
# 
# class ModernPrinter(Printer):
#     def print(self, document):
#         print(f"Printing {document} in color...")
#
#     def fax(self, document):
#         print(f"Faxing {document}...")
#
#     def scan(self, document):
#         print(f"Scanning {document}...")


"""
In this example, the base class, Printer, provides the interface that its subclasses must implement. OldPrinter inherits
from Printer and must implement the same interface. 
"""

from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")


class NewPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")


"""
Now Printer, Fax, and Scanner are base classes that provide specific interfaces with a single responsibility each.
 To create OldPrinter, you only inherit the Printer interface. 
 """

"""
5.Dependency Inversion Principle (DIP) :- The dependency inversion principle (DIP) is the last principle in the SOLID set.
This principle states that :-
 
Abstractions should not depend upon details. Details should depend upon abstractions.
"""


# class FrontEnd:
#     def __init__(self, back_end):
#         self.back_end = back_end
#
#     def display_data(self):
#         data = self.back_end.get_data_from_database()
#         print("Display data:", data)
#
#
# class BackEnd:
#     def get_data_from_database(self):
#         return "Data from the database"


"""
In this example, the FrontEnd class depends on the BackEnd class and its concrete implementation. You can say that both
 classes are tightly coupled. 
"""

# from abc import ABC, abstractmethod
#

# class FrontEnd:
#     def __init__(self, data_source):
#         self.data_source = data_source
#
#     def display_data(self):
#         data = self.data_source.get_data()
#         print("Display data:", data)
#

# class DataSource(ABC):
#     @abstractmethod
#     def get_data(self):
#         pass
#

# class Database(DataSource):
#     def get_data(self):
#         return "Data from the database"
#

# class API(DataSource):
#     def get_data(self):
#         return "Data from the API"
