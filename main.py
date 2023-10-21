from typing import Optional
from fastapi import FastAPI,Response,status
from pydantic import BaseModel
import random
from fastapi.exceptions import HTTPException

app = FastAPI()
created_post = []
class postparameters(BaseModel):
    title : str
    content : str
    rating : Optional[int] = 50
def find_post(id):
    for post in created_post:
        if post['id']==id:
            return post
    else:
        raise HTTPException(status_code=404,detail=f"data with given id {id} is not available")
def find_index(id):
    for index, post in enumerate(created_post):
        if post['id'] == id:
            return index
        else:
            raise HTTPException(status_code=404,detail=f"data with given id{id} not found")
@app.get("/")
def root():
    return {"message": "Welcome to my api"}
@app.get("/posts")
def get_posts():
    for post in created_post:
        return created_post
@app.post('/post',status_code=status.HTTP_201_CREATED)
def create_post(newpost:postparameters):
    post_dict = newpost.dict()
    post_dict['id'] =  random.randint(1,2000)
    created_post.append(post_dict)
    return {"Createdpost": created_post}
@app.get("/post/{id}")
def get_post(id:int):
    post = find_post(id)
    return post
@app.put("/post/{id}")
def update_post(id:int,update:postparameters):
    updated = update.dict()
    updated['id'] = id
    index = find_index(id)
    created_post[index] = updated
    return updated
@app.delete("/post/{id}")
def delete_post(id:int):
    index = find_index(id)
    created_post.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)




