# Creating Library class
class Library:
    book_list = []
    
    def __init__(self):
        pass

    def entry_book(self, book):
        self.book_list.append(book)

# Creating Book class
class Book:
    def __init__(self, book_id, title, author, availability, *args, **kargs):
        # Initializing attributes
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability

    def borrow_book(self, book_id):
        lib = Library()
        for book in lib.book_list:
            if(book.__book_id==book_id):
                if book.__availability:
                    book.__availability=False
                    print('Book borrowed succesfully!')
                else:
                    print('The book id ', book_id, ' is not available.')
                return
        print('Invalid book ID!')
    
    def return_book(self, book_id):
        lib = Library()
        for book in lib.book_list:
            if(book.__book_id==book_id):
                if not book.__availability:
                    book.__availability=True
                    print('Book returned succesfully!')
                else:
                    print('Book is already returned')
                return
        print('Invalid Book ID!')

    def view_book_info(self):
        lib = Library()
        print('<<<<<<<< Book List >>>>>>>>')
        for book in lib.book_list:
            print(f'{book.__book_id}) Title: {book.__title}, Author: {book.__author}, Availability: {book.__availability}')


book1 = Book(101, 'On the Origin of Species', 'Charles Darwin', True)
book2 = Book(102, 'War and Peace', 'Leo Tolstoy', True)
book3 = Book(103, 'Great Expectations', 'Charles Dickens', True)
book4 = Book(104, 'TO KILL A MOCKINGBIRD', 'HARPER LEE', True)
book5 = Book(105, 'Crime and Punishment', 'Fyodor Dostoyevsky', True)

lib = Library()
lib.entry_book(book1)
lib.entry_book(book2)
lib.entry_book(book3)
lib.entry_book(book4)
lib.entry_book(book5)

while True:
    print('---------****** Welcome to the Library ******----------')
    print('1. View All Books')
    print('2. Borrow Book')
    print('3. Return Book')
    print('4. Exit')
    op = int(input('Please Select an Option from above: '))
    if op==1:
        book1.view_book_info()
    elif op==2: 
        id = int(input('Please enter book id: '))
        book1.borrow_book(id)
    elif op==3:
        id = int(input('Please enter book id: '))
        book1.return_book(id)
    else: break
