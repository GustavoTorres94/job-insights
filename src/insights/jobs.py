import csv
from typing import List, Dict


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        job_data = []
        with open(path, "r") as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            job_data = list(reader)
            # for row in reader:
            #     job_data.append(
            #         {
            #             "job_title": row["job_title"],
            #             "company": row["company"],
            #             "state": row["state"],
            #             "city": row["city"],
            #             "min_salary": row["min_salary"],
            #             "max_salary": row["max_salary"],
            #             "job_desc": row["job_desc"],
            #             "industry": row["industry"],
            #             "rating": row["rating"],
            #             "date_posted": row["date_posted"],
            #             "valid_until": row["valid_until"],
            #             "job_type": row["job_type"],
            #             "id": row["id"],
            #         }
            #     )
        self.jobs_list = job_data
        return job_data

    def get_unique_job_types(self) -> List[str]:
        job_types = set()
        for job in self.jobs_list:
            job_type = job.get("job_type")
            if job_type:
                job_types.add(job_type)
        return list(job_types)

    def filter_by_multiple_criteria(
        self, jobs: List[Dict], filter_criteria: Dict
    ) -> List[Dict]:
        if not isinstance(filter_criteria, dict):
            raise TypeError("error")
        filtered_jobs = []
        for job in jobs:
            if all(
                job.get(key) == value for key, value in filter_criteria.items()
            ):
                filtered_jobs.append(job)
        return filtered_jobs
