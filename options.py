from rich.console import Console

from draco.llm import get_ai_suggestion

console = Console()


def interactive_mode():
    """
    Runs DRACO in interactive mode.
    """
    console.print("[bold yellow]💬 Welcome to DRACO Interactive Mode![/bold yellow]")
    console.print("Type your query or enter [bold cyan]'exit'[/bold cyan] to quit.")

    while True:
        query = console.input("\n[bold green]DRACO > [/bold green]").strip()

        if query.lower() in ["exit", "quit"]:
            console.print("[bold red]👋 Exiting DRACO. Have a great day![/bold red]")
            break
        elif query:
            get_ai_suggestion(query)
        else:
            console.print(
                "[bold yellow]⚠ Please enter a valid query or type 'exit' to quit.[/bold yellow]"
            )
