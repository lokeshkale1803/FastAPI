# -----------------------------------------
# SIMPLE BOOK API USING FASTAPI
# -----------------------------------------

# Import FastAPI
from fastapi import FastAPI

# Create the FastAPI application
app = FastAPI()


# -----------------------------------------
# SAMPLE BOOK DATA
# -----------------------------------------

books = [
{
"id": 1,
"title": "Python Basics",
"author": "Amit",
"price": 500
},
{
"id": 2,
"title": "Learning AI",
"author": "Neha",
"price": 700
}
]


# -----------------------------------------
# 1. GET - GET ALL BOOKS
# -----------------------------------------

@app.get("/books")
def get_books():

# Return all books
return books


# -----------------------------------------
# 2. GET - GET ONE BOOK
# -----------------------------------------

@app.get("/books/{book_id}")
def get_book(book_id: int):

# Search for the book
for book in books:

# Check whether the ID matches
if book["id"] == book_id:

# Return the matching book
return book

# If book is not found
return {"message": "Book not found"}


# -----------------------------------------
# 3. POST - ADD A NEW BOOK
# -----------------------------------------

@app.post("/books")
def add_book(title: str, author: str, price: int):

# Create a new book
new_book = {
"id": len(books) + 1,
"title": title,
"author": author,
"price": price
}

# Add the book to the list
books.append(new_book)

# Return the newly added book
return new_book


# -----------------------------------------
# 4. PUT - UPDATE BOOK PRICE
# -----------------------------------------

@app.put("/books/{book_id}")
def update_book(book_id: int, price: int):

# Search for the book
for book in books:

# Check the book ID
if book["id"] == book_id:

# Update the price
book["price"] = price

# Return updated book
return book

return {"message": "Book not found"}


# -----------------------------------------
# 5. DELETE - DELETE A BOOK
# -----------------------------------------

@app.delete("/books/{book_id}")
def delete_book(book_id: int):

# Search for the book
for book in books:

# Check the ID
if book["id"] == book_id:

# Remove the book
books.remove(book)

# Return confirmation
return {"message": "Book deleted successfully"}

return {"message": "Book not found"}