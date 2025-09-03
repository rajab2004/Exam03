class Library:
  def __init__(self):
    self.books = {}
  def add_book(self, title, author):
    self.books[title] = {'author': author, 'available': True}
  def borrow_book(self, title):
    if title in self.books and self.books[title]['available']:
      self.books[title]['available'] = False
      return f"You borrowed '{title}'"
    return f"Sorry, '{title}' is not available"
  def return_book(self, title):
    if title in self.books and not self.books[title]['available']:
      self.books[title]['available'] = True
      return f"You returned '{title}'"
    return f"Cannot return '{title}'"
if __name__ == "__main__":
  lib = Library()
  lib.add_book("1984", "George Orwell")
  lib.add_book("Xamsa", "Alisher Navoiy")
  print(lib.borrow_book("1984"))
  print(lib.borrow_book("1984"))
  print(lib.return_book("1984"))
