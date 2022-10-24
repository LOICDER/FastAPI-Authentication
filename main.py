import email
import uvicorn
from fastapi import FastAPI, HTTPException
from modules.model import PostSchema, UserLogInSchema, UserSignUpSchema

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

users = [

    {
        "name": "Admin",
        "email": "admin@admin.com",
        "password": "oui",
    }
]

app = FastAPI()

#1 Get for testing
@app.get("/", tags=["test!! 🤯"])
def greet():
    return {"Hello":"World!"}

#2 Get all posts
@app.post("/posts1", tags=["all posts!! 🔥"])
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

#5 User sign up
@app.post("/user/signup", tags = ["user sign up 🏄"])
def userSignUp(post : UserSignUpSchema):
    users.append(post.dict())
    return {
        "info": "user login created!"
    }

#6 Get all user posts
@app.get("/user/get all posts", tags=["all user posts!! 🔥🔥🔥"])
def get_all_user_posts():
    return {"data" : users}


#7 User log in
@app.post("/user/login", tags=["user login 🐄"])
def user_sign_in(data: UserLogInSchema):

    for user in users:
            if user["email"] == data.email and user["password"] == data.password:
                return {"message" : "You are logged in!"}
    raise HTTPException(status_code=404, detail="Incorrect email")


