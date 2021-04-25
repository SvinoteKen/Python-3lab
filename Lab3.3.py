class Dict:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value


class Taggable:
    def tag(self):
        raise NotImplementedError


class Book(Taggable):
    name = Dict()
    author = Dict()
    ID = Dict()

    def __init__(self, author_i, name_i=None):
        if name_i is None:
            raise ValueError('Name is requiered')
        else:
            self.name = name_i
            self.author = author_i
            self.ID = 0

    def tag(self):
        return [i for i in self.name.split() if i[0].isupper()]

    def __str__(self):
        return f'[{self.ID}] {self.author} "{self.name}"'


class IterLib:

    def __init__(self, lib):
        self.__limit = lib.len_books_list
        self.__book = 0
        self.__lib = lib

    def __iter__(self):
        return self

    def __next__(self):
        if self.__book >= self.__limit:
            raise StopIteration

        self.__book += 1
        return self.__lib.books_list[self.__book - 1]


class Library:
    ID_book = 0

    number = Dict()
    address = Dict()

    def __init__(self, number_i, address_i):
        self.number = number_i
        self.address = address_i
        self.__books_list = []

    def __iadd__(self, other: Book):
        Library.ID_book += 1
        other.ID = Library.ID_book
        self.__books_list.append(other)
        return self

    @property
    def books_list(self):
        return self.__books_list

    @property
    def len_books_list(self):
        return len(self.__books_list)

    def __iter__(self):
        return IterLib(self)


lib = Library(1, '51 Some str., NY')
lib += Book('Leo Tolstoi', 'War and Peace')
lib += Book('Charles Dickens', 'David Copperfield')
lib += Book('Charles Dickens', 'David Copperfield')
lib += Book('Charles Dickens', 'David Copperfield')

for book in lib:
    print(book)
    print(book.tag())