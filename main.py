from instabot import Bot
from time import sleep
from random import randint

bot = Bot()

getUsername = input("Enter the account Username:")
getPassword = input("Enter the account Password:")

bot.login(username = getUsername, password = getPassword)


non_followers = set(bot.following) - set(bot.followers)

for non_followers in non_followers:
    try:
        bot.unfollow(non_followers)
        sleep(randint(6,12))
    except Exception as e:
        print(e)
        sleep(randint(30,300))