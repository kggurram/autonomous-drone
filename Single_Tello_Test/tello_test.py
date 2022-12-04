from tello import Tello
import sys
from datetime import datetime
import time

start_time = str(datetime.now())
command = ''
tello = Tello()
while(1):
    command = input('Enter Command: ')
    if (command=='killl'):
        break
    tello.send_command(command)

log = tello.get_log()

out = open('log/' + start_time + '.txt', 'w')
for stat in log:
    stat.print_stats()
    str = stat.return_stats()
    out.write(str)
