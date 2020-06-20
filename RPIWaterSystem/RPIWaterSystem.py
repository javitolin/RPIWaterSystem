# pip install tweepy

from datetime import datetime
from time import sleep
import logging

import TwitterNotifier
from ConfigurationHelper import GetConfiguration

logging.basicConfig(filename='app.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logging.info("Starting")
sleepBetweenIterations = 2
TimeToSleepIfError = 10

if __name__ == '__main__':
    while(True):
        sleep(sleepBetweenIterations)

        configuration = GetConfiguration()
        if configuration == None:
            # log
            logging.warning("GetConfiguration returned None")
            TwitterNotifier.SendTweet("Error reading configuration!")
            continue
        
        if not configuration.IsActive:
            logging.info("Configuration is not active")
            continue

        now = datetime.now()
        current_hour = now.hour
        current_minute = now.minute
        matched_configuration = None

        for conf in configuration.RunConfigurations:
            if not conf.IsActive:
                continue
            
            conf_date = datetime.strptime(conf.StartTime,'%H:%M:%S')
            if conf_date.hour == current_hour and 0 <= conf_date.minute - current_minute <= 5:
                # found a match
                matched_configuration = conf
                break

        if matched_configuration is None:
            logging.debug("No configuration matched")
            continue

        # Need to run!
        logging.info("Open the Valve!")
        TwitterNotifier.SendTweet("Open the Valve!")
        
        # OPEN THE VALVE
        sleep(int(matched_configuration.DurationInSeconds))
        # CLOSE THE VALVE

        TwitterNotifier.SendTweet("Valve has been closed!")
        logging.info("Valve has been closed!")