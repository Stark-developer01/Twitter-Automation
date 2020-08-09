from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot 
        bot.get('https://twitter.com/')
        time.sleep(7)
        email = bot.find_element_by_xpath('//input[@name="session[username_or_email]"]')
        password = bot.find_element_by_xpath('//input[@name="session[password]"]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.submit()
        time.sleep(7)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')


        # If you want to search for a user instead then just type this 'https://twitter.com/'+hashtag in bot.get()
        # Remove the 'https://twitter.com/search?q='+hashtag+'&src=typed_query'

        
        time.sleep(7)
        for i in range(1, 4):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_elements_by_class_name('css-1dbjc4n')
            links = [element.get_attribute('data-focusable') for element in tweets]
            time.sleep(2)
            for link in links:
                bot.get('https://twitter.com' + link)
                try:
                    bot.find_element_by_class_name('css-1dbjc4n r-1niwhzg r-sdzlij r-1p0dtai r-xoduu5 r-1d2f490 r-xf4iuw r-u8s1d r-zchlnj r-ipm5af r-o7ynqc r-6461eg').click()
                    time.sleep(20)
                except Exception as ex:
                    time.sleep(60)


ed = TwitterBot('your_username', 'your_password') #Insert in your username and password of your account here
ed.login()
ed.like_tweet('your_search_tag') #The Search Tag or the name which you want to search