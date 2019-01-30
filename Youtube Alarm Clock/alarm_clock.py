import sys, time

import app_functions as af

if len(sys.argv) == 4:
    # Sets the amount of time before alarm goes off based on values from command line
    alarm = af.set_alarm(int(sys.argv[1]), int(sys.argv[2]), str(sys.argv[3]))

    # Pauses the program for the amount of time from alarm
    time.sleep(alarm)

    # Plays the randomly selected video 
    af.play_vid()
    print('Done.')
