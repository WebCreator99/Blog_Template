class Book:
    def __init__(self, title, author="Unknow"):
        self.title = title
        self.author = author

    def show_book(self):
        print(f"Title: {self.title}, Author: {self.author}")

book1 = Book("Python Program")
book2 = Book("Machine Learning", "Andrew Ng")

book1.show_book()
book2.show_book()
