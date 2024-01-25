from src.insights.jobs import ProcessJobs
from typing import Union, List, Dict


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salary = float("-inf")
        for job in self.jobs_list:
            salary = job.get("max_salary", "")
            salary = salary.strip()
            if salary.isnumeric():
                max_salary = max(max_salary, int(salary))
        return max_salary

    def get_min_salary(self) -> int:
        min_salary = float("inf")
        for job in self.jobs_list:
            salary = job.get("min_salary", "")
            salary = salary.strip()
            if salary.isnumeric():
                min_salary = min(min_salary, int(salary))
        return min_salary

    @staticmethod
    def simple_error_check(a: int, b: int) -> bool:
        if a > b:
            raise ValueError("min_salary maior que max_salary")
        return True

    @staticmethod
    def int_error_check(a: int, b: int) -> bool:
        if not isinstance(a, Union[int, float]) or not isinstance(
            b, Union[int, float]
        ):
            raise ValueError("min_salary e max_salary devem ser números")
        return True

    @staticmethod
    def salary_numeric_check(salary: Union[str, int]) -> bool:
        if not isinstance(salary, Union[int, float]):
            raise ValueError("salary deve ser número")
        return True

    def matches_salary_range(self, job: Dict, salary: Union[str, int]) -> bool:
        if "min_salary" not in job or "max_salary" not in job:
            raise ValueError("min_salary ou max_salary ausente")

        min_salary, max_salary = job["min_salary"], job["max_salary"]
        self.int_error_check(min_salary, max_salary)
        self.simple_error_check(min_salary, max_salary)
        self.salary_numeric_check(salary)

        return min_salary <= salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass


# inst = ProcessSalaries()
# max_salary = inst.get_max_salary()
# print(max_salary)
