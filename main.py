from fastapi import Body, FastAPI
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    rating: int

my_posts = [{"title": "title of the post 1", "content": "content of the post 1", "id": 1}, {"title": "favorite foods", "content": "I like pizza", "id": 2}]
@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_post():
    return {"message": my_posts}

@app.post("/posts")
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

