class Book:
    def __init__ (self, title, author):
        self.title = title
        self.author = author

book1 =  Book ("The Wonderful Wizaed of Oz", "L. Frank Baum") 
book2 =  Book ("The Call of the Wild", "Jack London") 

print(f"""
Book 1: {book1.title} by {book1.author}
Book 2: {book2.title} by {book2.author}
""")

del book2.author
print(f"""
Book 1: {book1.title} by {book1.author}
Book 2: {book2.title} by {book2.author}
""")