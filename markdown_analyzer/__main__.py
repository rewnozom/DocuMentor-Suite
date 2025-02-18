# markdown_analyzer/__main__.py
import click
import sys
import logging
from pathlib import Path
from typing import List
from .analyzer import MarkdownAnalyzer
from  .commands.dataset_commands import DatasetCommands


@click.group()
@click.option('--debug/--no-debug', default=False, help='Aktivera debug-läge')
@click.pass_context
def cli(ctx, debug):
    """Markdown Analyzer CLI"""
    # Configure logging
    log_level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=log_level
    )
    ctx.obj = {'debug': debug}

# Lägg till dataset-kommandon
cli.add_command(DatasetCommands.dataset, name="dataset")

# Lägg till generate-kommando direkt i CLI
@cli.command()
@click.option('--input-dir', '-i', required=True, 
              help='Input-katalog med markdown-filer')
@click.option('--output-dir', '-o', default='./output',
              help='Output-katalog för resultat')
@click.option('--commands', '-c', multiple=True, 
              type=click.Choice(['f', 's', 't', 'c', 'p']),
              default=['f', 's', 't', 'c'],
              help='Kommandon att generera data för')
@click.option('--workers', '-w', default=4,
              help='Antal parallella arbetartrådar')
@click.pass_context
def generate(ctx, input_dir: str, output_dir: str, 
           commands: List[str], workers: int):
    """Genererar träningsdata från markdown-filer"""
    try:
        # Validera och skapa kataloger
        input_path = Path(input_dir)
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        if not input_path.exists():
            raise click.BadParameter(f"Input-katalog finns inte: {input_dir}")

        # Initiera analyzer
        analyzer = MarkdownAnalyzer(debug=ctx.obj['debug'])

        # Processera filer med progress indicator
        with click.progressbar(
            length=1, 
            label='Processerar markdown-filer'
        ) as bar:
            analyzer.process_directory(str(input_path), workers)
            bar.update(1)

        # Generera träningsdata
        click.echo("\nGenererar träningsdata...")
        analyzer.generate_training_data(str(output_path), commands)

        # Sammanfattning
        click.echo("\nSammanfattning:")
        analyzer.print_summary()
        click.echo(f"\nData sparad till: {output_path.resolve()}")

    except KeyboardInterrupt:
        click.echo("\nAvbruten av användaren")
        sys.exit(1)
    except Exception as e:
        if ctx.obj['debug']:
            logging.exception("Kritiskt fel:")
        else:
            click.echo(f"\nFel: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    cli()