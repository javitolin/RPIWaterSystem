# pip install tweepy

import datetime
from time import sleep
import logging

import TwitterNotifier
from IOHelper import WriteToFile
from ConfigurationHelper import GetConfiguration
from Consts import LastTimeOpenFile, DateTimeFormat

logging.basicConfig(filename='app.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logging.info("Starting")
sleepBetweenIterations = 2
TimeToSleepIfError = 10
lastTimeOpen = datetime.datetime.min
seconds_in_day = 24 * 60 * 60

if __name__ == '__main__':
    while(True):
        sleep(sleepBetweenIterations)
        (isActive, minutesBetweenRuns, secondsToOpen) = GetConfiguration()
        if isActive == None or minutesBetweenRuns == None or secondsToOpen == None:
            # log
            logging.warning("GetConfiguration returned None")
            continue

        now = datetime.datetime.now()
        difference = now - lastTimeOpen
        minutesFromLastTime = divmod(difference.days * seconds_in_day + difference.seconds, 60)[0]
        if minutesFromLastTime <= minutesBetweenRuns:
            continue

        # Need to run!
        logging.info("Open the Valve!")
        TwitterNotifier.SendTweet("Open the Valve!")
        # OPEN THE VALVE
        sleep(secondsToOpen)
        # CLOSE THE VALVE
        TwitterNotifier.SendTweet("Valve has been closed!")
        logging.info("Valve has been closed!")
        lastTimeOpen = datetime.datetime.now()
        WriteToFile(LastTimeOpenFile, now.strftime(DateTimeFormat))