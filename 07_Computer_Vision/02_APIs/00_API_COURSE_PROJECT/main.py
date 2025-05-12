from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published : bool = True
    rating: Optional[int] = None



# request Get method url : "http://127.0.0.1:8000/items/5?q=somequery"
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = 'mariam'):
    return {"item_id": item_id, "q": q}

@app.post("/createposts")
def create_post():
    return {"message" : "Successfully created a post"}


@app.post("/createposts")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"new post": f"title {payload['title']} content: {payload['content']}"}


# use pedantic 

@app.post("/createpostsclass")
def create_post(new_post: Post):
    print(new_post.published)
    print(new_post.rating)    
    print(new_post.dict())
    return {"date": new_post}

##################################################################################################
from random import randrange
## Best practice fo naming convention
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
             {"title": "fav food", "content": "pizza", "id": 2}]
@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
# @app.get("/posts/latest")
# def get_lateset_post():
#     if len(my_posts) == 0:
#         return {"message": "No posts found"}
#     return {"data": my_posts[-1]}

@app.get("/posts/{id}")
def get_posts(id : int):
    post = find_post(id)
    return {"post detail": post}
        
