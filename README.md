# Instagram-Bot
An Insta bot that gets followers and following list from your account and find the id's that does not follows you back.

To run the 'bot.py' you should have python 3 or above. 

First of all you should install the necessary modules:

1. Selenium 
  ->to install selenium in your environment you just need to type
   "pip install selenium"(if there is pip package manager)
   
2. Webdriver
  -> If you are using google chrome as your you should install 'chromedriver' and for mozilla firefox the required webdriver
     is 'geckodriver'
  -> Get chrome webdriver from https://chromedriver.chromium.org/
  
  -> Get geckodriver from https://github.com/mozilla/geckodriver/releases
  
3. Instaloader
  -> Instaloader is powerful and intuitive Python API for Instagram, allowing to further customize obtaining media and metadata.
  -> Install Instaloader by typing "pip install instaloader" in your system.


Here we first get loggged in to our account and go to our profiles. Then we get the follower and following id's
and compare them to find the specific id's that does not follows you back.Further modification of bot can be done to get
diffferent functionalities.
Thank you.

Asim Mahat
[April 24,2020]


