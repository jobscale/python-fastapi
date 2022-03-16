from datetime import datetime
from fastapi import FastAPI, Response
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
  name: str
  price: float

class FindItem(BaseModel):
  id: Optional[int] = None
  name: Optional[str] = None

app = FastAPI()

@app.get('/')
async def home():
  date = datetime.now()
  d_str = date.isoformat()
  return Response(content='<h3>Hello World - ' + d_str + '</h3>', media_type="text/html")

@app.get('/item/{item_id}')
def read_item(item_id: int, q: str = None):
  if q:
    return { 'item_id': item_id, 'q': q }
  return { 'item_id': item_id }

@app.post('/item')
def find_item(item: FindItem):
  return { 'item.id': item.id, 'item.name': item.name }

@app.post('/items')
def update_item(item: Item):
  return { 'item.name': item.name, 'twice price': item.price * 2 }
