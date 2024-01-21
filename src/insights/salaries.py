from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salary = float("-inf")
        for job in self.jobs_list:
            salary = job.get("max_salary")
            if salary and isinstance(salary, (int, float)):
                max_salary = max(max_salary, salary)
        return int(max_salary) if max_salary != float("-inf") else 0

    def get_min_salary(self) -> int:
        min_salary = float("inf")
        for job in self.jobs_list:
            salary = job.get("min_salary")
            if salary and isinstance(salary, (int, float)):
                min_salary = min(min_salary, salary)
        return int(min_salary) if min_salary != float("inf") else 0

    def matches_salary_range(self, job: Dict, salary: Union[str, int]) -> bool:
        if "min_salary" not in job or "max_salary" not in job:
            raise ValueError("min_salary ou max_salary ausente")

        try:
            min_salary = float(job["min_salary"])
            max_salary = float(job["max_salary"])
        except ValueError:
            raise ValueError("min_salary e max_salary devem ser números")

        if min_salary > max_salary:
            raise ValueError("min_salary maior que max_salary")

        try:
            salary = float(salary)
        except ValueError:
            raise ValueError("O salary deve ser numéro")

        return min_salary <= salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
