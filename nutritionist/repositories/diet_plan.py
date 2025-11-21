from typing import Optional, List
from tinydb import Query
from nutritionist.models.diet_plan import DietPlan
from nutritionist.repositories.base_repository import BaseRepository


class DietPlanRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.diet_plan_table = self.get_table("diet_plans")

    def create_diet_plan(self, user_id: int, plan_details: str) -> DietPlan:
        diet_plan = DietPlan(user_id=user_id, plan_details=plan_details)
        self.diet_plan_table.insert(diet_plan.model_dump())
        return diet_plan

    def get_diet_plan_by_id(self, plan_id: int) -> Optional[DietPlan]:
        DietPlanQuery = Query()
        result = self.diet_plan_table.get(DietPlanQuery.id == plan_id)
        return DietPlan(**result) if result else None

    def get_last_diet_plan_for_user(self, user_id: int) -> Optional[DietPlan]:
        DietPlanQuery = Query()
        plans = self.diet_plan_table.get(DietPlanQuery.user_id == user_id)
        if not plans:
            return None

        latest_plan = sorted(plans, key=lambda x: x["created_at"], reverse=True)[0]
        return DietPlan(**latest_plan)

    def update_diet_plan(self, plan_id: int, plan_details: str) -> Optional[DietPlan]:
        update_data = {"plan_details": plan_details}
        DietPlanQuery = Query()
        self.diet_plan_table.update(update_data, DietPlanQuery.id == plan_id)
        updated_plan = self.diet_plan_table.get(DietPlanQuery.id == plan_id)
        return DietPlan(**updated_plan) if updated_plan else None

    def delete_diet_plan(self, plan_id: int) -> None:
        DietPlanQuery = Query()
        self.diet_plan_table.remove(DietPlanQuery.id == plan_id)

    def get_all_diet_plans(self) -> List[DietPlan]:
        results = self.diet_plan_table.all()
        return [DietPlan(**result) for result in results]
