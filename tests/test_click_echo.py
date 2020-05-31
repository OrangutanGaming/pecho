import io
from contextlib import redirect_stdout

import click
import click._compat

from pecho import echo as pecho

click._compat.isatty = lambda _: True


def test_click_echo():
    f = io.StringIO()
    with redirect_stdout(f):
        pecho('1', end='%', print_func=click.echo)
        pecho('2%', print_func=click.echo)
        pecho('3%', newline=True, print_func=click.echo)
        pecho('4%', print_func=click.echo)
        pecho('', newline=True, print_func=click.echo)
        print('Done')
    out = f.getvalue()
    assert out == '\r\033[K1%\r\033[K2%\r\033[K3%\n\r\033[K4%\r\033[K\nDone\n'
