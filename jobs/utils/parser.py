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
                published_at=item["publishedDate"],
                url=item["jobUrl"]
            )
        )
    return jobs

from pathlib import Path

def load_keywords(path: Path) -> list[str]:
    return [
        line.strip().lower()
        for line in path.read_text(encoding="utf8").splitlines()
        if line.strip() and not line.startswith("#")
    ]