from abc import ABC, abstractmethod

# Membuat antarmuka ABC dengan menggunakan Abstract Base Class (ABC)
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Membuat kelas lingkaran yang mengimplementasikan antarmuka Shape
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Membuat kelas segitiga yang mengimplementasikan antarmuka Shape
class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.base + self.height + ((self.base**2 + self.height**2)**0.5)

# Fungsi untuk menghitung dan mencetak area dan keliling dari bentuk
def print_shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

# Membuat objek lingkaran dan segitiga
circle = Circle(5)
triangle = Triangle(3, 4)

# Memanggil fungsi print_shape_info dengan objek lingkaran dan segitiga
print("Informasi Lingkaran:")
print_shape_info(circle)

print("\nInformasi Segitiga:")
print_shape_info(triangle)
