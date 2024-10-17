import click
from pypdf import PdfReader, PdfWriter

from ._type import PagesType


@click.group()
def cli():
    pass


@cli.command()
@click.argument('input_pdf', type=click.Path(exists=True))
@click.option('-p', '--pages', type=PagesType(), required=True)
@click.option('-o', '--output', type=click.Path(), required=False, default=None)
def split(input_pdf, output, pages: list[int]):
    output_pdf_path = (
        str(input_pdf).replace('.pdf', '_split.pdf') if output is None else output
    )

    input_pdf = PdfReader(input_pdf)
    output_pdf = PdfWriter()

    for page in pages:
        output_pdf.add_page(input_pdf.pages[int(page) - 1])

    output_pdf.write(output_pdf_path)


if __name__ == '__main__':
    cli()
