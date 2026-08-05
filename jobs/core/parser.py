from jobs.core.models import Job

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

def save_to_txt(jobs: list[dict], filename: str, DATA_DIR) -> Path:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    lines = []
    for job in jobs:
        lines.append(
            f"Empresa: {job['careerPageName']}\n"
            f"Cargo: {job['name']}\n"
            f"Cidade: {job['city']}\n"
            f"URL: {job['jobUrl']}\n"
            + "-" * 40
        )

    content = "\n".join(lines) if lines else "Nenhuma vaga encontrada."

    file_path = DATA_DIR / filename
    file_path.write_text(content, encoding="utf-8")
    return file_path