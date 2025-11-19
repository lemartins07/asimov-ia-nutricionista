from typing import Optional, List
from tinydb import Query
from datetime import datetime
from nutricionist.models.weight_history import WeightHistory
from nutricionist.repositories.base_repository import BaseRepository


class WeightHistory(BaseRepository):
    def __init__(self):
        super().__init__()
        self.weight_history_table = self.get_table("weight_history")

    def add_weight_history(self, user_id: int, weight_kg: str) -> WeightHistory:
        weight_history = WeightHistory(
            user_id=user_id,
            weight_kg=weight_kg,
        )
        self.weight_history_table.insert(weight_history.model_dump())
        return weight_history

    def get_weight_history(self, user_id: int) -> List[WeightHistory]:
        WeightHistoryQuery = Query()
        results = self.weight_history_table.search(
            WeightHistoryQuery.user_id == user_id
        )
        sorted_results = sorted(
            results, key=lambda entry: datetime.fromisoformat(entry["date"])
        )
        return [WeightHistory(**entry) for entry in sorted_results]
