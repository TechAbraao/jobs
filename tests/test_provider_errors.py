import httpx
import pytest

from jobs.core.providers import GupyAPI, GupyAPIError


def test_search_jobs_maps_timeout_to_safe_message(mocker):
    mocker.patch(
        "jobs.core.providers.httpx.get",
        side_effect=httpx.ReadTimeout("private timeout details"),
    )

    with pytest.raises(GupyAPIError) as error:
        GupyAPI().search_jobs()

    assert str(error.value) == "A busca na Gupy excedeu o tempo limite. Tente novamente."
    assert "private timeout details" not in str(error.value)


def test_search_jobs_maps_connection_error_to_safe_message(mocker):
    mocker.patch(
        "jobs.core.providers.httpx.get",
        side_effect=httpx.ConnectError("private host and request details"),
    )

    with pytest.raises(GupyAPIError) as error:
        GupyAPI().search_jobs()

    assert "Não foi possível conectar à API da Gupy" in str(error.value)
    assert "private host and request details" not in str(error.value)


def test_search_jobs_reports_http_status_without_response_body(mocker):
    response = httpx.Response(
        503,
        json={"error": "sensitive internal server response"},
        request=httpx.Request("GET", "https://example.com/jobs"),
    )
    mocker.patch("jobs.core.providers.httpx.get", return_value=response)

    with pytest.raises(GupyAPIError) as error:
        GupyAPI().search_jobs()

    assert "erro HTTP (503)" in str(error.value)
    assert "sensitive internal server response" not in str(error.value)


def test_search_jobs_reports_invalid_json_safely(mocker):
    response = httpx.Response(
        200,
        text="private malformed response",
        request=httpx.Request("GET", "https://example.com/jobs"),
    )
    mocker.patch("jobs.core.providers.httpx.get", return_value=response)

    with pytest.raises(GupyAPIError) as error:
        GupyAPI().search_jobs()

    assert "resposta inválida" in str(error.value)
    assert "private malformed response" not in str(error.value)