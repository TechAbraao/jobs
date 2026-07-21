import pytest

@pytest.fixture
def gupy_response_factory():
    def _make(jobs=None):
        jobs = jobs or []
        return {"data": jobs}
    return _make