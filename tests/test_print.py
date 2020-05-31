import io
from contextlib import redirect_stdout

from pecho import echo as pecho


def test_print_function():
    f = io.StringIO()
    with redirect_stdout(f):
        pecho('1', end='%')
        pecho('2%')
        pecho('3%', newline=True)
        pecho('4%')
        pecho(newline=True)
        print('Done')
    out = f.getvalue()
    assert out == '\r\033[K1%\r\033[K2%\r\033[K3%\n\r\033[K4%\r\033[K\nDone\n'
