# Creating Library class
class Library:
    book_list = []
    
    def __init__(self):
        pass

    def entry_book(self, book):
        self.book_list.append(book)

# Creating Book class
class Book(Library):
    def __init__(self, book_id, title, author, availability):
        # Initializing attributes
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability
        self.entry_book(self)

    @classmethod
    def borrow_book(self, book_id):
        for book in self.book_list:
            if(book.__book_id==book_id):
                if book.__availability:
                    book.__availability=False
                    print('Book borrowed succesfully!')
                else:
                    print('The Book ID ', book_id, ' is not available.')
                return
        print('Invalid Book ID!')
    @classmethod
    def return_book(self, book_id):
        for book in self.book_list:
            if(book.__book_id==book_id):
                if not book.__availability:
                    book.__availability=True
                    print('Book returned succesfully!')
                else:
                    print('The Book not yet borrowed!')
                return
        print('Invalid Book ID!')
    @classmethod
    def view_book_info(self):
        print('<<<<<<<< Book List >>>>>>>>')
        for book in self.book_list:
            print(f'{book.__book_id}) Title: {book.__title}, Author: {book.__author}, Availability: {book.__availability}')


book1 = Book(101, 'On the Origin of Species', 'Charles Darwin', True)
book2 = Book(102, 'War and Peace', 'Leo Tolstoy', True)
book3 = Book(103, 'Great Expectations', 'Charles Dickens', True)
book4 = Book(104, 'TO KILL A MOCKINGBIRD', 'HARPER LEE', True)
book5 = Book(105, 'Crime and Punishment', 'Fyodor Dostoyevsky', True)

while True:
    print('---------****** Welcome to the Library ******----------')
    print('1. View All Books')
    print('2. Borrow Book')
    print('3. Return Book')
    print('4. Exit')
    op = int(input('Please Select an Option from above: '))
    if op==1:
        Book.view_book_info()
    elif op==2: 
        id = int(input('Please enter Book ID: '))
        Book.borrow_book(id)
    elif op==3:
        id = int(input('Please enter Book ID: '))
        Book.return_book(id)
    else: break
