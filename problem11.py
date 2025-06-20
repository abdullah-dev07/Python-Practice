import copy

class Book:
    def __init__(self, title, author, isbn, availability_status):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability_status = availability_status

class Library:
    def __init__(self, library_data):
        self.library_data = library_data
        self.inventory = []
    
    def add_book_decorator(func):
        def wrapper(self, book):
            func(self, book)
            print(f"Book added: {book.title}")
        return wrapper    
    
    @add_book_decorator
    def add_book(self, book : Book):
        
        file = open(self.library_data, 'a')
        book_details= book.title + "," + book.author + "," + str(book.isbn) + "," + str(book.availability_status)
        self.inventory.append([book_details])
        file.write(book_details.strip() + "\n")
        file.close()

    def show_inventory(self):
        
        file = open(self.library_data, 'r')
        for book in file:
            parsed_book = book.strip().split(',')
            print(f"Title: {parsed_book[0]}, Author: {parsed_book[1]}, Available:  {str(parsed_book[3])}")

         

    def return_copy(self):
        copy_file = copy.deepcopy(self.inventory)
        return copy_file
      

            


class Library_Iterator():
    def __init__(self, lib):
        self.file = open(lib.library_data, 'r')


    def __iter__(self):
        return self 


    def __next__(self):
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration

        parsed_line = line.strip().split(',')
        if parsed_line[3] == 'True':
            return parsed_line[0]
        
        



file = "library_data.txt"

lib = Library(file)
book = Book("Harry Potter", "JK Rowling", 12345, True)
book2 = Book("Harry Potter2", "JK Rowling", 12345, False)
book3 = Book("Harry Potter3", "JK Rowling", 12345, True)

lib.add_book(book)
lib.add_book(book2)
lib.add_book(book3)

print(lib.return_copy())


# lib_iter = Library_Iterator(lib)

# for title in lib_iter:
#     # print(student)
#     if title is not None:
#         print(f"Title: {title}\n")
#     else:
#         continue
