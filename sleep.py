import subprocess
from datetime import datetime, timedelta, time
from time import sleep
from threading import Thread


# play noise at night - cron schedule for 10:00:00 PM
# turn off at 7:00am

def is_quiet_time():    
    morning_time = time(7, 0)
    evening_time = time(21, 30)    
    current_time = datetime.now().time()
    
    # return true if it is quiet time (between 7AM and 9PM)
    if current_time >= morning_time and current_time <= evening_time:
        print("It's quiet time, sound will not play.")
        return True

    # else return false and allow sound to play
    else:
        return False

def start_sleep():
    command = 'exec play -n synth brownnoise'    
    sound = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    timecheck = False
    while is_quiet_time() == False:
        sleep(1)
      
    sound.kill()

start_sleep()
