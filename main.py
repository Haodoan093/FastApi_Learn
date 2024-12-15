from http.client import HTTPException

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None



items_db = []



@app.post("/items/")
def create_item(item: Item):
    items_db.append(item)
    return {"name": item.name, "price": item.price, "is_offer": item.is_offer}



@app.get("/items/")
def get_items():
    return items_db



@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):

    if item_id >= len(items_db) or item_id < 0:
        raise HTTPException(status_code=404, detail="Item not found")


    items_db[item_id] = item
    return {"name": item.name, "price": item.price, "is_offer": item.is_offer}



@app.delete("/items/{item_id}")
def delete_item(item_id: int):

    if item_id >= len(items_db) or item_id < 0:
        raise HTTPException(status_code=404, detail="Item not found")


    deleted_item = items_db.pop(item_id)
    return {"message": "Item deleted", "deleted_item": deleted_item}