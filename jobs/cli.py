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
def search(city: str = "São Paulo", limit: int = 10):

    api = GupyAPI()

    data = api.search_jobs(city, limit)

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
            job["jobUrl"]
        )

    console.print(table)


if __name__ == "__main__":
    app()