class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:

    all = []
    
    def __init__(self, title):
        self.title = title
        self.author = None
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book ==self]

class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.book = book
        self.date = date
        self.royalties = royalties
        self.author = author
        book.author = author
        author.book = book
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Invalid Author Type!")
        self._author = value

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Invalid Book Type!")
        self._book = value

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Invalid Date Type!")
        self._date = value

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("Invalid Royalties Type!")
        self._royalties = value
    
    @classmethod
    def contracts_by_date(cls, filter_date=None):
        sorted_contracts = sorted(cls.all, key=lambda contract: contract.date)
        if filter_date:
            return [contract for contract in sorted_contracts if contract.date == filter_date]
        return sorted_contracts