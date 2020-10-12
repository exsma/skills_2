"""Discussion Questions

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

(replace this with your answer)


containment
polymorphasim
2. What is a class?

(replace this with your answer)


3. What is a method?

(replace this with your answer)


4. What is an instance in object orientation?

(replace this with your answer)


5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

(replace this with your answer)
"""


"""2. Road Class"""
class Road:

    def __init__(self, num_lanes = 2, speed_limit= 25):
        self.num_lanes = num_lanes
        self.speed_limit = speed_limit
        pass

road_1 = Road( 4, 60)
road_2 = Road()


# Update road_1 so that

# num_lanes is 4

# speed_limit is 60
"""3. Update Password"""


class User:
    """A user object."""

    def __init__(self, username, password):
        """Create a user with the given username and password."""

        self.username = username
        self.password = password

    def update_password (self, current_password, new_password) :
        if current_password != self.password:
            print ('Invalid password')
        else:
            self.password = new_password


"""4. Build a Library"""
# 4. Build a Library
# We have given you a class, Book. You’ll use it build a new Library class. Your Library class needs to meet these specifications:

# Each Library object needs an instance attribute called books which starts off as an empty list

# We also need two methods:


# find_books_by_author, which takes in an author’s name (as a string) and returns a list of all books by that author
class Book(object):
    """A Book object."""

    def __init__(self, title, author):
        """Create a book with the given title and author."""

        self.title = title
        self.author = author
class Library():
    #all_books = {}
    def __init__(self, books):
        self.books = []


    def create_and_add_book(self, title, author):

        book_at_hand = Book(title, author)
        self.books.append(book_at_hand)



    def find_books_by_author(self, author):
        all_books = []
        for book in self:
            if self.author == book.author:
                all_books.append(self.title)

            return all_books



"""5. Rectangle"""


class Rectangle:
    """A rectangle."""

    def __init__(self, length, width):
        """Create a rectangle with the given length and width."""

        self.length = float(length)
        self.width = float(width)

    def calculate_area(self):
        """Return the area of the rectangle."""

        return self.length * self.width

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
       

    def calculate_area(self):
        """Return the area of the rectangle."""
        if self.length == self.width:
            return super().calculate_area()
        else:
            print("Invalid square")
            return None
