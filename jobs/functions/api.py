import httpx

class GupyAPI:
    def __init__(self):
        self._BASE_URL = "https://employability-portal.gupy.io/api/v1"
        
    def search_jobs(self, city: str, limit: int, page: int = 1):
        
        response = httpx.get(
            f"{self._BASE_URL}/jobs",
            params={
                "city": city,
                "limit": limit
            },
            timeout=20
        )
        response.raise_for_status()
        return response.json()