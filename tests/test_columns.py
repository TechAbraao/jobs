from jobs.core.columns import HISTORY_COLUMNS, SEARCH_COLUMNS, MATCH_COLUMNS, OUTPUT_COLUMNS
from jobs.core.types import JobType, TYPE_MAP, KeywordsType


def test_columns_metadata_is_configured():
    assert [column["name"] for column in HISTORY_COLUMNS] == ["Data e Hora", "Comando"]
    assert MATCH_COLUMNS == ["Porcentual", "Empresa", "Cargo", "Cidade", "Estado", "URL", "Palavras"]
    assert SEARCH_COLUMNS == ["Empresa", "Cargo", "Cidade", "Estado", "URL", "Modelo de Trabalho", "Publicado em"]
    assert OUTPUT_COLUMNS == ["Descrição", "Caminho Relativo", "Arquivo"]


def test_job_type_mapping_and_keywords_enum():
    assert TYPE_MAP[JobType.efetivo] == "vacancy_type_effective"
    assert TYPE_MAP[JobType.estagiario] == "vacancy_type_internship"
    assert TYPE_MAP[JobType.jovem_aprendiz] == "vacancy_type_apprentice"
    assert KeywordsType.keywords.value == "KEYWORDS.md"
