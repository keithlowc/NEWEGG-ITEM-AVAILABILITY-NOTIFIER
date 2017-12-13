#! /bin/bash

## Created by Keith Low

## Note: This will run every 4 hour. You can change the time by changing the value of sleep
##		 Also the terminal window should remain open

##Script to run newegg gpu finder

while [ : ]
do
	rm newdata.json
	scrapy runspider <'DIRECTORY-OF-SCRAPER-GOES-HERE'>/github-newegg-scraper.py -o newdata.json ## Will run the scraper and save the data into newdata.json
	python <'DIRECTORY-OF-SCRAPER-GOES-HERE'>/github-notifier.py ## Will run the notifier and send message if found
	sleep 14400s
done
