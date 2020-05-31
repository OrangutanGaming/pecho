import time

import click

from pecho import echo

echo('1', end='%', print_func=click.echo)
time.sleep(1)
echo('2%', print_func=click.echo)
time.sleep(1)
echo('3%', newline=True, print_func=click.echo)
time.sleep(1)
echo('4%', print_func=click.echo)
time.sleep(1)
echo('', newline=True, print_func=click.echo)
time.sleep(1)
print('Done')
