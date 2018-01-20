'''
Check06a
Inheritance
'''

# parent class
class Book:
    def __init__(self):
        title = ""
        author = ""
        publication_year = 0

    def prompt_book_info(self):
        self.title = input("Title: ")
        self.author = input("Author: ")
        self.publication_year = input("Publication Year: ")

    def display_book_info(self):
        print("{} ({}) by {}".format(self.title, self.publication_year, self.author))

# child classes
class TextBook(Book):
    def __init__(self):
        subject = ""

    def prompt_subject(self):
        self.subject = input("Subject: ")

    def display_subject(self):
        print("Subject: {}".format(self.subject))

class PictureBook(Book):
    def __init__(self):
        self.illustrator = ""

    def prompt_illustrator(self):
        self.illustrator = input("Illustrator: ")

    def display_illustrator(self):
        print("Illustrator: {}".format(self.illustrator))

def main():
    # using parent class
    book = Book()
    book.prompt_book_info()
    print()
    book.display_book_info()
    print()

    # using child class
    textbook = TextBook()
    textbook.prompt_book_info()
    textbook.prompt_subject()
    print()
    textbook.display_book_info()
    textbook.display_subject()
    print()

    # using child class
    picturebook = PictureBook()
    picturebook.prompt_book_info()
    picturebook.prompt_illustrator()
    print()
    picturebook.display_book_info()
    picturebook.display_illustrator()
    print()

if __name__ == '__main__':
    main()