import uvicorn
from fastapi import FastAPI
from modules.model import PostSchema

posts = [
    {
        "id": 1,
        "title": "crocodile",
        "text": "It's me! :🐊",
    },

    {        
        "id": 2,
        "title": "banana",
        "text": "It's me! :🍌",
    },
    {
        "id": 3,
        "title": "gorilla",
        "text": "It's me! :🦍",
    }
]

user = []

app = FastAPI()

#1 Get for testing
@app.get("/", tags=["test!! 🤯"])
def greet():
    return {"Hello":"World!"}

#2 Get all posts
@app.get("/posts", tags=["all posts!! 🔥"])
def get_posts():
    return {"data" : posts}

#3 Get single post
@app.get("/posts/{id}", tags=["single post 💎"])
def get_one_post(id: int):
    if id > len(posts):
        return {
            "error":"Post with this ID does not exist 💣"
        }
    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }

#4 Post a blog post [handler for creating a post]
@app.post("/posts", tags = ["posts"])
def add_post(post : PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "info":"Post added!"
    }


