# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)

#     def perimeter(self):
#         return 2 * math.pi * self.radius

# c = Circle(9)
# print("Area:", c.area())
# print("Perimeter:", c.perimeter())



class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price:.2f}")

    def apply_discount(self, percentage):
        discount_amount = self.price * (percentage / 100)
        self.price -= discount_amount

# (a) 
book1 = Book("November 9", "Colleen Hoover", 599)
book2 = Book("It Ends with Us", "Colleen Hoover", 399)
print("Book 1 Details:")
book1.display_details()
print("\nBook 2 Details:")
book2.display_details()

# (b) 
book1.apply_discount(10)
print("\nBook 1 Details after 10% discount:")
book1.display_details()
