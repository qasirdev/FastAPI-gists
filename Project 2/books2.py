from typing import Optional
from fastapi import FastAPI,Body,Path, Query,HTTPException
from pydantic import BaseModel,Field
from starlette import status

app=FastAPI()

class Book:
  id:int
  title: str
  author: str
  description:str
  rating: int
  published_date:int

  def __init__(self, id,title,author,description,rating,published_date):
    self.id = id
    self.title=title
    self.author=author
    self.description=description
    self.rating=rating
    self.published_date=published_date

class BookRequest(BaseModel):
    id:Optional[int] = Field(description="Id is not required at the time of create", default=None)
    title: str = Field(min_length=3, max_length=100)
    author: str
    description:str
    rating: int = Field(gt=0, lt=6)
    published_date:int

    model_config = {
       'json_schema_extra': {
          "example": {
            "title": "a new book",
            "author": "qasirdev",
            "description": "a new description of book",
            "rating": 5,
            "published_date": 2025
          }
       }
    }

BOOKS = [
  Book(1, 'Computer Science Pro1', 'codingwithroby1', 'A very nice book1!', 1, 2001),
  Book(2, 'Computer Science Pro2', 'codingwithroby2', 'A very nice book2!', 2, 2002),
  Book(3, 'Computer Science Pro3', 'codingwithroby3', 'A very nice book3!', 3, 2003),
  Book(4, 'Computer Science Pro4', 'codingwithroby4', 'A very nice book4!', 4, 2004),
  Book(5, 'Computer Science Pro5', 'codingwithroby5', 'A very nice book5!', 5, 2030),
]

@app.get("/books", status_code=status.HTTP_200_OK)
async def get_all_books():
  return BOOKS

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id:int):
    for book in BOOKS:
        if book.id == book_id:
             return book
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/books/")
async def get_books_by_rating(book_rating:int = Query(gt=0, lt=6)):
   book_rating_result = []
   for book in BOOKS:
      if book.rating == int(book_rating):
         book_rating_result.append(book)

   return book_rating_result

@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(request_body:BookRequest):
    new_book=Book(**request_body.model_dump())
    BOOKS.append(find_book_id(new_book))

@app.put("/books/update_book",status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book:BookRequest):
   book_changed = False
   for i in range(len(BOOKS)):
      if BOOKS[i].id == book.id:
         BOOKS[i] = book
         book_changed=True
   if not book_changed:
  		raise HTTPException(status_code=404, detail="Item not found.")

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0, description='Delete id should be greater than zero')):
   for i in range(len(BOOKS)):
      if BOOKS[i].id == book_id:
        BOOKS.pop(i)
        break

def find_book_id(book: Book):
   book.id = 0 if len(BOOKS) == 0 else BOOKS[-1].id + 1
#    if len(BOOKS) > 0:
#       book.id = BOOKS[-1].id + 1
#    else:
#      book.id = 0
     
   return book
