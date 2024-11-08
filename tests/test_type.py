import click
import pytest

from pdftools._type import PagesType


@pytest.mark.parametrize(
    'value, expected',
    [
        ('1,2,3', [1, 2, 3]),
        ('1-3', [1, 2, 3]),
        ('1-3,5', [1, 2, 3, 5]),
    ],
)
def test_parse_pages(value, expected):
    pages_type = PagesType()

    assert pages_type.convert(value, None, None) == expected


def test_parse_unknown_pages():
    pages_type = PagesType()

    with pytest.raises(click.exceptions.BadParameter):
        pages_type.convert('1-3-5', None, None)
