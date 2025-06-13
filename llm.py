import os

from together import Together
from dotenv import load_dotenv
from rich.console import Console

load_dotenv()
console = Console()

TOGETHER_API_KEY = os.getenv("API_KEY")

client = Together(api_key=TOGETHER_API_KEY)


def get_ai_suggestion(query: str):
    """
    Queries Together AI Llama 3.3-70B for CLI command suggestions.

    Args:
        query (str): The query for which CLI command is needed.
    """

    query_content = f"What is the CLI command for: {query}? no text. If it doesnt have CLI, say no specific CLI"

    try:
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
            messages=[{"role": "user", "content": f"{query_content}"}],
            max_tokens=50,
        )
        command_suggestion = response.choices[0].message.content.strip()
        console.print("[green]DRACO AI Suggests:[/green]")

        if "No specific CLI" in command_suggestion:
            console.print(f"[red]❌ The given query is not CLI related. [/red]")
        else:
            console.print(f"{command_suggestion}")

    except Exception as e:
        console.print(f"[red]Error contacting Together AI: {e}[/red]")
        console.print(
            "[yellow]Please check your API key or network connection.[/yellow]"
        )
