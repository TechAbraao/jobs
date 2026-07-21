from jobs.utils.models import Job

def parse_jobs(data):
    jobs = []
    for item in data["data"]:
        jobs.append(
            Job(
                id=item["id"],
                title=item["name"],
                company=item["careerPageName"],
                city=item["addressCity"],
                state=item["addressStateShortName"],
                url=item["jobUrl"]
            )
        )
    return jobs