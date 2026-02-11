class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def __repr__(self):
        return self.title

    def __str__(self):
        return f"Title:{self.title} Author:{self.author} Price:{self.price}"
    
b1=Book("python","Robert","999")
b2=Book("Saithan","Robber","420")
print(b1,b2)
print(b1)
print([b1,b2])