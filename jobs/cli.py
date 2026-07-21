import typer
from rich.console import Console
from rich.table import Table
from enum import Enum

from jobs.utils.api import GupyAPI

class JobType(str, Enum):
    efetivo = "Efetivo"
    estagiario = "Estágio"
    jovem_aprendiz = "Jovem Aprendiz"
    
TYPE_MAP = {
    JobType.efetivo: "vacancy_type_effective",
    JobType.estagiario: "vacancy_type_internship",
    JobType.jovem_aprendiz: "vacancy_type_apprentice",
}

TYPE_MAP = {
    JobType.efetivo: "vacancy_type_effective",
    JobType.estagiario: "vacancy_type_internship",
    JobType.jovem_aprendiz: "vacancy_type_apprentice",
}


app = typer.Typer()
console = Console()

@app.callback()
def main():
    pass

@app.command()
def search(
    city: str = typer.Option("São Paulo", "--city", help="Filtra vagas por cidade."),
    limit: int = typer.Option(10, "--limit", help="Quantidade de resultados."),
    keyword: str = typer.Option("", "--keyword", help="Palavra-chave para buscar no título e na descrição das vagas."),
    type: JobType = typer.Option(JobType.efetivo, "--type", help="Tipo de vaga a ser filtrada."),
):
    api = GupyAPI()
    type_employee = TYPE_MAP[type]

    data = api.search_jobs(city=city, limit=limit, type=type_employee, keyword=keyword)

    table = Table()
    table.add_column("Empresa")
    table.add_column("Cargo")
    table.add_column("Cidade")
    table.add_column("URL")

    for job in data["data"]:
        table.add_row(
            job["careerPageName"],
            job["name"],
            job["city"],
            f"[link={job['jobUrl']}]Abrir Vaga[/link]"
        )

    console.print(table)

if __name__ == "__main__":
    app()