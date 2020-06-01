import praw
from configparser import ConfigParser
import requests
import time


class CleanseSubredditBot():

    def __init__(self):
        self.user_agent = "CleanseSubredditBot / V1.0 By ScoopJr"
        print('Starting up...', self.user_agent)
        CONFIG = ConfigParser()
        CONFIG.read('config.ini')
        # Retrieving User information from config.ini for PRAW
        self.user = CONFIG.get('main', 'USER')
        self.password = CONFIG.get('main', 'PASSWORD')
        self.client = CONFIG.get('main', 'CLIENT_ID')
        self.secret = CONFIG.get('main', 'SECRET')
        self.subreddit = CONFIG.get('main', 'SUBREDDIT')
        self.token_url = "https://www.reddit.com/api/v1/access_token"
        self.token = ""
        self.t_type = ""
        self.delay = CONFIG.getint('main', 'DELAY')
        self.reddit = praw.Reddit(client_id=self.client,
                             client_secret=self.secret,
                             password=self.password,
                             user_agent=self.user_agent,
                             username=self.user)

    def get_token(self):
        """Gets OAUTH access token for PRAW"""
        client_auth = requests.auth.HTTPBasicAuth(self.client, self.secret)
        post_data = {'grant_type': 'password', 'username': self.user, 'password': self.password}
        headers = {'User-Agent': self.user_agent}
        response = requests.Session()
        response2 = response.post(self.token_url, auth=client_auth, data=post_data, headers=headers)
        self.token = response2.json()['access_token']
        self.t_type = response2.json()['token_type']

    def main(self):
        """Main - handling running of the bot"""
        no_posts_found = 0
        while True:
            print(f"...Searching for posts to cleanse..")
            for post in self.reddit.subreddit(self.subreddit).stream.submissions(pause_after=1):
                if post is None:
                    no_posts_found += 1
                    print(f".....Will run through {self.subreddit} one final time")
                    break
                else:
                    if post.locked:
                        post.mod.remove()
                    else:
                        post.mod.lock()
                        post.mod.remove()
                        print(f"Post removed: {post.id}")
            if no_posts_found == 2:
                print(f"{self.subreddit} has been successfully cleansed.")
                break
            print(f"...Taking a small break!  Be back in {self.delay} seconds")
            time.sleep(self.delay)

if __name__ == "__main__":
    bot = CleanseSubredditBot()
    bot.main()