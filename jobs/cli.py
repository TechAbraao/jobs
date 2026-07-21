from jobs.utils.types import JobType, TYPE_MAP
from jobs.utils.providers import GupyAPI
from rich.console import Console
from rich.table import Table
from datetime import datetime
from pathlib import Path
import typer

app = typer.Typer()
console = Console()
DATA_DIR = Path(__file__).resolve().parent / "data"

@app.callback()
def main():
    pass

@app.command()
def search(
    city: str = typer.Option(None, "--city", "-c", help="Filtra vagas por cidade."),
    limit: int = typer.Option(10, "--limit", "-l", help="Quantidade de resultados."),
    keyword: str = typer.Option(None, "--keyword", "-k", help="Palavra-chave para buscar no título e na descrição das vagas."),
    state: str = typer.Option(None, "--state", "-s", help="Filtra vagas por estado."),
    type: JobType = typer.Option(JobType.efetivo, "--type", "-t", help="Tipo de vaga a ser filtrada."),
    output: str = typer.Option(None, "--output", "-o", help="Nome do arquivo .txt para salvar os resultados (salvo em jobs/data/)."),
    enterprise: str = typer.Option(None, "--enterprise", "-e", help="Filtra vagas por empresa."),
):
    api = GupyAPI()
    type_employee = TYPE_MAP[type]
    filters = {"limit": limit, "type": type_employee}
    if city:
        filters["city"] = city
    if keyword:
        filters["keyword"] = keyword
    if state:
        filters["state"] = state
    if enterprise:
        filters["enterprise"] = enterprise
    data = api.search_jobs(**filters)
    all_jobs = data["data"]

    table = Table()
    table.add_column("Empresa")
    table.add_column("Cargo")
    table.add_column("Cidade")
    table.add_column("Estado")
    table.add_column("URL")
    table.add_column("Publicado em")

    for job in all_jobs:
        raw_date = job.get("publishedDate")
        if raw_date:
            published = datetime.fromisoformat(raw_date.replace("Z", "+00:00"))
            data_formatada = published.strftime("%Y-%m-%d às %H:%M:%S")
        else:
            data_formatada = "N/A"

        table.add_row(
            job["careerPageName"],
            job["name"],
            job["city"],
            job["state"],
            f"[link={job['jobUrl']}]Abrir Vaga[/link]",
            data_formatada,
        )
    console.print(table)
    
    if output:
        saved_path = _save_to_txt(all_jobs, output)
        tableOutput = Table()

        tableOutput.add_column("Descrição")
        tableOutput.add_column("Caminho Relativo")
        tableOutput.add_column("Arquivo")

        tableOutput.add_row(
            "Resultados salvos com sucesso",
            str(saved_path.relative_to(Path.cwd())) if saved_path.is_relative_to(Path.cwd()) else str(saved_path),
            saved_path.name,
        )

        console.print(tableOutput)

def _save_to_txt(jobs: list[dict], filename: str) -> Path:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    lines = []
    for job in jobs:
        lines.append(
            f"Empresa: {job['careerPageName']}\n"
            f"Cargo: {job['name']}\n"
            f"Cidade: {job['city']}\n"
            f"URL: {job['jobUrl']}\n"
            + "-" * 40
        )

    content = "\n".join(lines) if lines else "Nenhuma vaga encontrada."

    file_path = DATA_DIR / filename
    file_path.write_text(content, encoding="utf-8")
    return file_path


if __name__ == "__main__":
    app()