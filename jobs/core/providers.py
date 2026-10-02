from typing import Optional
import httpx


class GupyAPIError(Exception):
    """Erro seguro e compreensível ao consultar a API da Gupy."""


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
                    model_work: Optional[bool]= None
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
        if model_work:
            params["isRemoteWork"] = model_work

        try:
            response = httpx.get(
                f"{self._BASE_URL}/jobs",
                params=params,
                timeout=20
            )
            response.raise_for_status()
            return response.json()
        except httpx.TimeoutException:
            raise GupyAPIError(
                "A busca na Gupy excedeu o tempo limite. Tente novamente."
            ) from None
        except httpx.HTTPStatusError as error:
            raise GupyAPIError(
                f"A Gupy retornou um erro HTTP ({error.response.status_code}). Tente novamente mais tarde."
            ) from None
        except httpx.RequestError:
            raise GupyAPIError(
                "Não foi possível conectar à API da Gupy. Verifique sua conexão e tente novamente."
            ) from None
        except ValueError:
            raise GupyAPIError(
                "A API da Gupy retornou uma resposta inválida. Tente novamente mais tarde."
            ) from None
    
    def applying_filters(
            self, 
            limit: int,
            type_employee: str,
            city: str,
            keyword: str,
            state: str,
            enterprise: str,
            model_work: bool
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
        if model_work:
            filters["model_work"] = model_work
            
        return filters