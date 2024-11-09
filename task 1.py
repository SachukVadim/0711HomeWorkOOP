class Book:
    def __init__(self, author: str, title: str, genre: str, publication: int):
        self.author = author
        self.title = title
        self.genre = genre
        self.publication = publication

    def __repr__(self):
        return f"title {self.title}, author {self.author}, genre {self.genre}, publication {self.publication}"

    def __str__(self):
        return f"Book title: '{self.title}', author: {self.author}, published in {self.publication}, genre: {self.genre}"


list_book = []
book1 = (Book("Leo Tolstoy", "War and Peace", "Novel, Historical Fiction", 1869))
book2 =(Book("Mikhail Bulgakov", "The Master and Margarita", "Novel, Fantasy, Mystery", 1967))
print(repr(book1))
print(str(book2))



