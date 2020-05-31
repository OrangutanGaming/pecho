import io
from contextlib import redirect_stdout

from pecho import echo as pecho


def custom_print(*args, **kwargs):
    return print(*args, **kwargs)


def pecho_custom_print(*args, **kwargs):
    kwargs['print_func'] = custom_print
    kwargs.setdefault('print_func_kwargs', {})
    kwargs['print_func_kwargs']['end'] = ''
    return pecho(*args, **kwargs)


def test_custom_print_function():
    f = io.StringIO()
    with redirect_stdout(f):
        pecho_custom_print('1', end='%')
        pecho_custom_print('2%')
        pecho_custom_print('3%', newline=True)
        pecho_custom_print('4%')
        pecho_custom_print(newline=True)
        print('Done')
    out = f.getvalue()
    assert out == '\r\033[K1%\r\033[K2%\r\033[K3%\n\r\033[K4%\r\033[K\nDone\n'
