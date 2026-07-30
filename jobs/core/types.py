from enum import Enum

class JobType(str, Enum):
    efetivo = "Efetivo"
    estagiario = "Estágio"
    jovem_aprendiz = "Jovem Aprendiz"

class KeywordsType(str, Enum):
    keywords = "KEYWORDS.md"
    
TYPE_MAP = {
    JobType.efetivo: "vacancy_type_effective",
    JobType.estagiario: "vacancy_type_internship",
    JobType.jovem_aprendiz: "vacancy_type_apprentice",
}