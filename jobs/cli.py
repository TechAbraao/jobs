import typer
from rich.console import Console
from rich.table import Table

from jobs.functions.api import GupyAPI

app = typer.Typer()
console = Console()

@app.callback()
def main():
    pass

@app.command()
def search(
        city: str = typer.Option("São Paulo", "--city", help="Filtra vagas por cidade."),
        limit: int = typer.Option(10, "--limit", help="Quantidade de cesultados."),
        keyword: str = typer.Option("Tecnologia", "--keyword", help="Palavra-chave para buscar no título e na descrição das vagas."),
        type: str = typer.Option("Efetivo","--type", help="Tipo de vaga a ser filtrada. Opções: Efetivo, Estagiário, Jovem Aprendiz.")
    ):
    type_employee = None
    
    api = GupyAPI()

    if type == "Efetivo":
        type_employee = "vacancy_type_effective"
    elif type == "Estágio":
        type_employee = "vacancy_type_internship"
    elif type == "Jovem Aprendiz":
        type_employee = "vacancy_type_apprentice"
    
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