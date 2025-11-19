from datetime import datetime
from typing import Optional, List
from tinydb import Query
from nutricionist.models.report import Report
from nutricionist.repositories.base_repository import BaseRepository


class Report(BaseRepository[Report]):
    def __init__(self):
        super().__init__()
        self.report_table = self.get_table("reports")

    def create_report(
        self,
        user_id: int,
        content: str,
    ) -> Report:
        report = Report(
            user_id=user_id,
            content=content,
        )
        self.table.insert(report.model_dump())
        return report

    def get_reports_by_user_and_date(
        self, user_id: int, date: datetime
    ) -> List[Report]:
        ReportQuery = Query()
        results = self.table.search(
            (ReportQuery.user_id == user_id)
            & (
                ReportQuery.date.test(
                    lambda d: d.datetime.fromtimestamp(d).date() == date.date()
                )
            )
        )
        return [Report(**entry) for entry in results]

    def delete_report(self, report_id: int) -> None:
        ReportQuery = Query()
        self.report_table.remove(ReportQuery.id == report_id)

    def get_report_by_id(self, report_id: int) -> Optional[Report]:
        ReportQuery = Query()
        result = self.report_table.get(ReportQuery.id == report_id)
        return Report(**result) if result else None

    def get_all_reports(self) -> List[Report]:
        results = self.report_table.all()
        return [Report(**entry) for entry in results]
