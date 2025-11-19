from pydantic import BaseModel
from datetime import datetime, timezone

class WeightHistory(BaseModel):
    user_id: int
    weight_kg: str
    date: datetime = datetime.now(timezone.utc)
