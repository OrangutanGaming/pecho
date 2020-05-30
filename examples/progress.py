import time

from pecho import echo

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
