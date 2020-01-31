#Download Python and gecko driver.
#install Selenium
#based on this video --> https://www.youtube.com/watch?v=7ovFudqFB0Q&spfreload=10

#!/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time

class TwitterBot:
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.bot = webdriver.Firefox()
    
  def login(self):
    bot = selt.boy
    bot.get('https://twitter.com/')
    time.sleep(3)
    email = bot.find_element_by_class_name('email-input')
    password = bot.find_element_by_name('session[passwprd]')
    email.clear()
    password.clear()
    email.send_keys(self.username)
    password.send_keys(self.password)
    password.send_keys(Keys.RETURN)
    time.sleep(3)
    
  def like_tweet(self, hastag):
    bot = self.bot
    bot.get('https://twitter.com/serach?q='+hashtag+'&src=typd')
    time.sleep(3)
    for i in range(1,4):
      bot.execute_script('window.scrollTo(0,document.body.scrollheight)
      time.sleep(2)
      tweets = bot.find_elements_by_class_name('tweet')
      links = [elem.get_attribute('data-permalink-path') for elem in tweets]
#-----------------adding in a print to make sure this will work.-----------
      print(links)
      for link in links:
        bot.get('https://twitter.com' + link)
        try:
          bot.find_element_by_class_name('HeartAnimation).click()
          time.sleep(10)
        except Exception as ex:
          time.sleep(60)
    
ed = TwitterBot('<username>', '<Password>')
ed.login()
ed.like_tweet('<hastag>')
