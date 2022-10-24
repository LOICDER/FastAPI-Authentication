from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id : int = Field(default = None)
    title : str = Field(default = None)
    content : str = Field(default = None)
    class Config: #this is a subclass
        schema_extra = {
             "post_demo" : {
             "title" : "some title about animals",
             "content" : "some content about animals"
             }
         }

class UserSignUpSchema(BaseModel):
    nom : str = Field(default = None)
    email : EmailStr = Field(...)
    password : str = Field(default = None)


class UserLogInSchema(BaseModel):
    email : str
    password : str
