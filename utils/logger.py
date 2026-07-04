from rich.console import Console

console = Console()


def log_agent_output(agent_name, output):

    console.print(f"\n[bold cyan]{agent_name} OUTPUT[/bold cyan]")
    console.print(output)