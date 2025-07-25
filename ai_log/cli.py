import typer
from rich.console import Console

app = typer.Typer()
console = Console()

@app.command()
def greet(
    name: str = typer.Option("DevOps", help="Whom to greet"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
):
    \"\"\"Friendly hello from the TriLog CLI.\"\"\"
    if verbose:
        console.print(f"[bold green]Verbose mode on[/] → greeting {name}")
    console.print(f"Hey [bold cyan]{name}[/], TriLog bot is alive! 🚀")

if __name__ == "__main__":
    app()
