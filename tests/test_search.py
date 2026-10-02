import jobs.cli as cli_module
from typer.testing import CliRunner
from jobs.cli import app
from jobs.core.providers import GupyAPI

runner = CliRunner()


def test_search_returns_job(mocker):
    fake_data = {
        "data": [
            {
                "careerPageName": "Acme Corp",
                "name": "Python Developer",
                "city": "São Paulo",
                "state": "São Paulo",
                "jobUrl": "https://example.com/employee/1",
                "publishedDate": "2023-01-01T00:00:00Z",
            }
        ]
    }

    mocker.patch.object(GupyAPI, "search_jobs", return_value=fake_data)

    result = runner.invoke(app, ["search", "--limit", "1"])

    assert result.exit_code == 0
    assert "Acme" in result.stdout
    assert "Python" in result.stdout
    assert "São" in result.stdout


def test_search_saves_output_file(mocker, monkeypatch, tmp_path):
    fake_data = {
        "data": [
            {
                "careerPageName": "Acme Corp",
                "name": "Python Developer",
                "city": "São Paulo",
                "state": "São Paulo",
                "jobUrl": "https://example.com/employee/1",
                "publishedDate": "2023-01-01T00:00:00Z",
            }
        ]
    }

    archive_dir = tmp_path / "archives"
    monkeypatch.setattr(cli_module, "DATA_DIR", archive_dir)
    mocker.patch.object(GupyAPI, "search_jobs", return_value=fake_data)

    result = runner.invoke(app, ["search", "--output", "resultados.txt"])

    assert result.exit_code == 0
    assert (archive_dir / "resultados.txt").exists()
    assert "Resultados salvos com" in result.stdout
    assert "resultados.txt" in result.stdout