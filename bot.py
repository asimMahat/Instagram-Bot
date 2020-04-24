#importing necessary modules

from selenium import webdriver
from time import sleep
import instaloader
import os

class instagrambot:

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.instagram.com/accounts/login/?hl=en")
        sleep(3)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
                    .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
                    .send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(5)
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        sleep(2)
        # self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            # .click()
        # sleep(2)

       

insta_bot = instagrambot('your_username','your_password')

insta_stalker_bot = instaloader.Instaloader()
insta_stalker_bot.login("your_username","your_password")
my_profile = instaloader.Profile.from_username(insta_stalker_bot.context, "your_username") 

follow_list = []
count=0
for follower in my_profile.get_followers():
    follow_list.append(follower.username)
    file = open("my_followers.csv","a+")# to get the id that follows me
    file.write(follow_list[count])
    file.write("\n")
    file.close()
    print(follow_list[count])
    count=count+1

for follower in my_profile.get_followees():
    follow_list.append(follower.username)
    file = open("my_following.csv","a+") #to get the people that I follow
    file.write(follow_list[count])
    file.write("\n")
    file.close()
    print(follow_list[count])
    count=count+1


i_follow= open('my_following.csv','r')
i_get_followed = open('my_followers.csv','r')

#finding id's that do not follow me
noobs = set(i_follow)- set(i_get_followed)

# printing out the id's that do not follows me
print(noobs)


#writing the noobs id's which do not follows me in the different csv file

with open ('noob_haru.csv','w') as file_out:

    for line in noobs:
        file_out.write(line)

