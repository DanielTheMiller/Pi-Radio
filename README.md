# Pi-Radio

An automated MPEG-DASH audio streaming server, streaming pre-recorded audio 24/7 accessible via HTTP.
The motive: I want a radio program made BY me, FOR me.

The program should be lightweight in terms of storage and processing need as it will be running on a raspberry pi.
The greatest problem is generating enough content to broadcast 24/7.

#The Listener's Experience
- On the hour, every hour, the most recent headlines should be read via a voice synthesiser 
	- preferably a custom voice synthesiser
	- The headline reading should last 5 minutes.
- The most recent episodes of my favourite podcasts should play throughout the day.
	- Podcasts should run against a timetable, each podcast should run 2 hours apart (i.e. 6pm, 8pm, 10pm - etc.)
	- I should be able to load the radio application at the same time every day and hear different episodes of the same podcast.
	- Podcasts are often longer than an hour
		- After the first hour of the podcast, the episode should be interrupted so the news can play. The podcast should resume after the news
	- Podcasts are not standardised, and will often massively underrun their allocated timeslot of 2 hours.
- Filler content of a dynamic length should keep the radio on schedule.
	- Any time left after podcast completion and before the news should be dynamically filled.
	- Preferably this would be filled with a playlist of royalty free music

#Tools/Languages utilised:
-FFMPEG
-BASH shell scripting
-Python
	Python Libraries:
		requests
		beautifulsoup4
-NGINX



