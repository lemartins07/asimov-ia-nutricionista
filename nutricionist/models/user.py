from pydantic import BaseModel

class User(BaseModel):
  telegram_id: int
  name: str
  age: str
  sex: str
  height_cm: str
  weight_kg: str
  has_diabetes: str
  goal: str
