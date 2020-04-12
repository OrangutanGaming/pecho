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
        pecho()
        print()
    out = f.getvalue()
    assert out == '\r1%\x1b[K\r2%\x1b[K\r3%\x1b[K\n\r4%\x1b[K\r\x1b[K\n'


def custom_print(*args, **kwargs):
    return print(*args, **kwargs)


def echo(*args, **kwargs):
    kwargs['print_func'] = custom_print
    kwargs.setdefault('_', {})
    kwargs['_']['end'] = ''
    return pecho(*args, **kwargs)


def test_custom_print_function():
    f = io.StringIO()
    with redirect_stdout(f):
        echo('1', end='%')
        echo('2%')
        echo('3%', newline=True)
        echo('4%')
        echo()
        print()
    out = f.getvalue()
    assert out == '\r1%\x1b[K\r2%\x1b[K\r3%\x1b[K\n\r4%\x1b[K\r\x1b[K\n'
