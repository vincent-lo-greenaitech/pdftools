import os

import click
import img2pdf
from PIL import Image
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


@cli.command()
@click.argument('image_path', type=click.Path(exists=True))
@click.option('-o', '--output', type=click.Path(), required=False, default=None)
def img_to_pdf(image_path, output):
    """
    Convert an image to a PDF.
    """
    if output is None:
        output = os.path.splitext(image_path)[0] + '.pdf'

    try:
        with Image.open(image_path) as image:
            pdf_bytes = img2pdf.convert(image.filename)

        with open(output, 'wb') as pdf_file:
            pdf_file.write(pdf_bytes)  # type: ignore

        click.echo(f'Successfully converted image to PDF: {output}')

    except Exception as e:
        click.echo(f'Error converting image to PDF: {e}')


if __name__ == '__main__':
    cli()
