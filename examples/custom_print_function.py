import time

from pecho import echo as pecho


def custom_print(*args, **kwargs):
    return print(*args, **kwargs)


def echo(*args, **kwargs):
    kwargs['print_func'] = custom_print
    kwargs.setdefault('print_func_kwargs', {})
    kwargs['print_func_kwargs']['end'] = ''
    return pecho(*args, **kwargs)


echo('1', end='%')
time.sleep(1)
echo('2%')
time.sleep(1)
echo('3%', newline=True)
time.sleep(1)
echo('4%')
time.sleep(1)
echo(newline=True)
time.sleep(1)
print('Done')
