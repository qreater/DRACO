import argparse
from rich.text import Text
from rich.console import Console

from draco.llm import get_ai_suggestion
from draco.options import interactive_mode


console = Console()

draco_ascii = Text(
    """
    .___                           
  __| _/___________    ____  ____  
 / __ |\_  __ \__  \ _/ ___\/  _ \ 
/ /_/ | |  | \// __ \\  \__(  <_> )
\____ | |__|  (____  /\___  >____/ 
     \/            \/     \/      

Developer Resourceful AI Command Operator      
""",
    style="bold cyan",
)


def main():
    console.print(draco_ascii)

    parser = argparse.ArgumentParser(
        description="DRACO - Developer Resourceful AI Command Operator"
    )
    parser.add_argument(
        "query",
        type=str,
        nargs="?",
        help="Describe the command you need (e.g., 'list pods')",
    )
    parser.add_argument(
        "--interactive", action="store_true", help="Run DRACO in interactive mode"
    )

    args = parser.parse_args()

    if args.query:
        query = args.query
        get_ai_suggestion(query)
    elif args.interactive:
        interactive_mode()

    else:
        console.print(
            "[bold yellow]⚠ No command entered! Please type a query.[/bold yellow]"
        )
        console.print("Example: [cyan]python draco.py 'list pods'[/cyan]")
