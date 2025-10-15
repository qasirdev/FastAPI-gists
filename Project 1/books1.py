from fastapi import FastAPI, Body
app=FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]
@app.get("/books")
async def get_books_by_category(category:str):
  return_books=[]
  for book in BOOKS:
    if book.get("category").casefold() == category.casefold():
      return_books.append(book)
  
  return return_books

@app.get("/books/mybook")
async def get_my_book():
  return {"my_book":"This is my book"}

@app.get("/books/{title}")
def get_all_books(title:str, category:str):
  return_books=[]
  for book in BOOKS:
    if book.get("title").casefold() == title.casefold() and \
      book.get("category").casefold() == category.casefold():
      return_books.append(book)
  return return_books

@app.post("/books/create_book")
async def create_a_book(new_body=Body()):
  BOOKS.append(new_body)

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
            BOOKS[i] = updated_book

# @app.put("/books/update_book")
# async def update_book(updated_book=Body()):
#     for i in range(len(BOOKS)):
#         if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
#             BOOKS[i] = updated_book
