class Review:
    def __init__(self, reviewer: str, text: str, rating: int):
        self.reviewer = reviewer
        self.text = text
        self.rating = rating

    def __str__(self):
        return f"Review by {self.reviewer}: {self.text} (Rating: {self.rating}/5)"

class Book:
    def __init__(self, author: str, title: str, genre: str, publication_year: int):
        self.author = author
        self.title = title
        self.genre = genre
        self.publication_year = publication_year
        self.reviews = []

    def add_review(self, review: Review):
        self.reviews.append(review)

    def __str__(self):
        book_info = f"'{self.title}' by {self.author} ({self.publication_year}) - Genre: {self.genre}"
        reviews_info = "\n".join(str(review) for review in self.reviews)
        return f"{book_info}\nReviews:\n{reviews_info if reviews_info else 'No reviews yet.'}"

# Приклад використання
book1 = Book("Leo Tolstoy", "War and Peace", "Novel, Historical Fiction", 1869)
book1.add_review(Review("Alice", "A masterpiece of literature.", 5))
book1.add_review(Review("Bob", "A bit lengthy, but worth it.", 4))

print(book1)
