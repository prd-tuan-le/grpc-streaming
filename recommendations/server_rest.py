import uvicorn
from fastapi import FastAPI

from faker import Faker
from faker.providers import DynamicProvider

book_provider = DynamicProvider(
    provider_name="book",
    elements=[
        "The Maltese Falcon",
        "Murder on the Orient Express",
        "The Hound of the Baskervilles",
        "The Hitchhiker's Guide to the Galaxy",
        "Ender's Game",
        "The Dune Chronicles",
        "The 7 Habits of Highly Effective People",
        "How to Win Friends and Influence People",
        "Man's Search for Meaning",
    ],
)

fake = Faker()

app = FastAPI()


@app.get("/rest/{num_of_books}")
def grpc_unary(num_of_books: int = 1, name="World"):
    books_to_recommend = []
    for i in range(num_of_books):
        books_to_recommend.append({"id": i, "title": fake.book()})
    return books_to_recommend


# then add new provider to faker instance
fake.add_provider(book_provider)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=50052)
