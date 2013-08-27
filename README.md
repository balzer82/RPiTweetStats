RPiTweetStats
=============

Python Script to Tweet Stats of your RaspberryPi to a Twitter Account

    [Bot]: CPU 48.2`C, 0.5% Load. Uptime: 0:25:56.970000

* CPU Temperature
* CPU Load
* Uptime since last Reboot

You have to get OAuth Access to your Twitter Account (as a [https://dev.twitter.com/](developer)) and have to enter your keys to the Python script.

## Dependencies

You need [Tweepy](https://github.com/tweepy/tweepy) to Tweet.

## Auto Tweet

You need to make the Python file executable

    sudo chmod 755 rpitweetstats.py

And then one can simply use a Cronjob to tweet every 10 minutes

    sudo crontab -e
    
and add

    */10 * * * * python /home/pi/rpitweetstats.py
    
## Thanks to

* [morphics](http://planzero.org/blog/2012/01/26/system_uptime_in_python,_a_better_way)
* [Orer2ddo456](http://c-mobberley.com/wordpress/index.php/2013/04/26/raspberry-pi-connect-to-twitter-account-using-tweepy-installation-and-tweet-cpu-temperature-example/)
* [jerome bettis](http://ubuntuforums.org/showthread.php?t=148781)
