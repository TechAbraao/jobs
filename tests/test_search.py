from typer.testing import CliRunner
from jobs.cli import app
from jobs.utils.api import GupyAPI

runner = CliRunner()

def test_search_returns_job(mocker):
    fake_data = {
        "data": [
            {
                "careerPageName": "Acme Corp",
                "name": "Python Developr",
                "city": "São Paulo",
                "jobUrl": "https://example.com/employee/1",
            }
        ]
    }

    mocker.patch.object(GupyAPI, "search_jobs", return_value=fake_data)

    result = runner.invoke(app, ["search"])

    assert result.exit_code == 0
    assert "Acme Corp" in result.stdout