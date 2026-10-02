import pytest

from jobs.core.matcher import calculate_match
from jobs.core.models import Job
from jobs.core.parser import load_keywords, parse_jobs, save_to_txt


def test_calculate_match_counts_matches_and_returns_percentage():
    job = {
        "name": "Senior Python Developer",
        "description": "Precisa de Python, Docker e AWS para atuar em arquitetura cloud.",
    }

    score, found = calculate_match(job, ["python", "java", "docker"])

    assert score == pytest.approx(66.67, rel=1e-2)
    assert found == ["python", "docker"]


def test_calculate_match_returns_zero_when_keywords_is_empty():
    score, found = calculate_match({"name": "Dev", "description": "Sem stack"}, [])

    assert score == 0
    assert found == []


def test_parse_jobs_transforms_api_payload_into_job_objects():
    data = {
        "data": [
            {
                "id": 10,
                "name": "Python Developer",
                "careerPageName": "Acme Corp",
                "addressCity": "São Paulo",
                "addressStateShortName": "SP",
                "publishedDate": "2026-10-02T10:00:00Z",
                "jobUrl": "https://example.com/vaga/10",
            }
        ]
    }

    jobs = parse_jobs(data)

    assert len(jobs) == 1
    assert isinstance(jobs[0], Job)
    assert jobs[0].id == 10
    assert jobs[0].title == "Python Developer"
    assert jobs[0].company == "Acme Corp"
    assert jobs[0].city == "São Paulo"
    assert jobs[0].state == "SP"
    assert jobs[0].url == "https://example.com/vaga/10"


def test_load_keywords_ignores_blank_lines_and_comments(tmp_path):
    keywords_file = tmp_path / "KEYWORDS.md"
    keywords_file.write_text("# comentario\nPython\n\nJava\nFlask\n", encoding="utf-8")

    keywords = load_keywords(keywords_file)

    assert keywords == ["python", "java", "flask"]


def test_save_to_txt_creates_file_with_job_data(tmp_path):
    jobs = [{
        "careerPageName": "Acme Corp",
        "name": "Python Developer",
        "city": "São Paulo",
        "jobUrl": "https://example.com/vaga/10",
    }]

    file_path = save_to_txt(jobs, "resultados.txt", tmp_path)
    content = file_path.read_text(encoding="utf-8")

    assert file_path.name == "resultados.txt"
    assert "Empresa: Acme Corp" in content
    assert "Cargo: Python Developer" in content
    assert "Cidade: São Paulo" in content
    assert "URL: https://example.com/vaga/10" in content
