class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

class Ebook(Book):
    def __init__(self, title, author, price):
        super().__init__(title,author,price)
        self.file_size = 0.0

    def get_info(self):
        self.title = input("enter the tittle of the book: " ) 
        self.author = input("enter the name of the author: " )
        self.price = float(input("enter the price of the book: " ))
        self.file_size = float(input("enter the size of the file: " ))


        if self.price > 0 and self.file_size > 0:
            print ("information saved succesfully")
        else :
            print ("false information entered")


my_ebook = Ebook("Sample Title", "Sample Author", 19.99)
my_ebook.get_info()