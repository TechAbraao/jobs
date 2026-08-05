from typing import Optional
import httpx

class GupyAPI:
    def __init__(self):
        self._BASE_URL = "https://employability-portal.gupy.io/api/v1"
        
    def search_jobs(self, 
                    city: Optional[str] = None,
                    limit: int = 10,
                    type: Optional[str] = None,
                    keyword: Optional[str] = None,
                    state: Optional[str] = None,
                    enterprise: Optional[str] = None,
                ):
        
        params = {"limit": limit}

        if city:
            params["city"] = city
        if state:
            params["state"] = state
        if type:
            params["type"] = type
        if keyword:
            params["term"] = keyword
        if enterprise:
            params["careerPageName"] = enterprise

        response = httpx.get(
            f"{self._BASE_URL}/jobs",
            params=params,
            timeout=20
        )
        response.raise_for_status()
        return response.json()
    
    def applying_filters(
            self, 
            limit: int,
            type_employee: str,
            city: str,
            keyword: str,
            state: str,
            enterprise: str
        ):
        filters = {"limit": limit, "type": type_employee}
        
        if city:
            filters["city"] = city
        if keyword:
            filters["keyword"] = keyword
        if state:
            filters["state"] = state
        if enterprise:
            filters["enterprise"] = enterprise
            
        return filters