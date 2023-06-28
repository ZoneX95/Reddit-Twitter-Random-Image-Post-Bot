import os
import random
import praw
import tweepy
import time
import shutil
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

# Set up logging
log_file = "bot.log"
log_handler = TimedRotatingFileHandler(log_file, when="midnight", interval=1, backupCount=7)
log_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
log_handler.setFormatter(log_formatter)
logger = logging.getLogger()
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)

# Reddit API credentials
reddit_client_id = ''
reddit_client_secret = ''
reddit_username = ''
reddit_password = ''
reddit_user_agent = ''

# Twitter API credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Path to the folder containing the pictures
folder_path = r''
uploaded_path = r''

# Subreddits to post the pictures
subreddit_names = ['']

# Choices for Reddit post titles
reddit_title_choices = ['Title 1', 'Title 2', 'Title 3']

# Choices for Twitter post titles
twitter_title_choices = ['Tweet 1', 'Tweet 2', 'Tweet 3']

# Create a Reddit instance
reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     username=reddit_username,
                     password=reddit_password,
                     user_agent=reddit_user_agent)

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_api = tweepy.API(auth)

# Counter for the number of images posted
image_counter = 0

def post_image_to_reddit(subreddit_name, title, image_path):
    try:
        # Submit the picture to the subreddit
        subreddit = reddit.subreddit(subreddit_name)
        subreddit.submit_image(title=title, image_path=image_path)
        logger.info("Image posted to Reddit.")
        print(f"[{datetime.now()}] Image posted to Reddit.")
        return True
    except Exception as e:
        logger.error(f"Failed to post image to Reddit: {str(e)}")
        print(f"[{datetime.now()}] Failed to post image to Reddit: {str(e)}")
        return False

def post_image_to_twitter(title, image_path):
    try:
        # Upload the image to Twitter
        media = twitter_api.media_upload(image_path)
        twitter_api.update_status(status=title, media_ids=[media.media_id])
        logger.info("Image posted to Twitter.")
        print(f"[{datetime.now()}] Image posted to Twitter.")
        return True
    except Exception as e:
        logger.error(f"Failed to post image to Twitter: {str(e)}")
        print(f"[{datetime.now()}] Failed to post image to Twitter: {str(e)}")
        return False

def main():
    global image_counter

    # Get a random picture file from the folder
    picture_files = os.listdir(folder_path)

    if len(picture_files) == 0:
        logger.warning("No picture files found in the folder.")
        print(f"[{datetime.now()}] No picture files found in the folder.")
        return

    # Choose a random picture file
    picture_file = random.choice(picture_files)
    picture_path = os.path.join(folder_path, picture_file)

    # Choose random titles for Reddit and Twitter
    reddit_title = random.choice(reddit_title_choices)
    twitter_title = random.choice(twitter_title_choices)

    # Submit the initial picture to the subreddits
    for subreddit_name in subreddit_names:
        reddit_success = post_image_to_reddit(subreddit_name, title=reddit_title, image_path=picture_path)

        if reddit_success:
            # Upload the initial picture to Twitter if Reddit posting is successful
            twitter_success = post_image_to_twitter(title=twitter_title, image_path=picture_path)
            if twitter_success:
                # Relocate the uploaded image to the uploaded folder
                shutil.move(picture_path, os.path.join(uploaded_path, picture_file))
                logger.info("Image relocated.")
                print(f"[{datetime.now()}] Image relocated.")
                image_counter += 1
                print(f"Images posted: {image_counter}")
            else:
                logger.warning("Skipping relocation. Image was not posted on Twitter.")
                print(f"[{datetime.now()}] Skipping relocation. Image was not posted on Twitter.")
                return

    # Wait for 30 minutes before posting the next picture
    time.sleep(1800)

    while True:
        # Get a new random picture file from the folder
        picture_files = os.listdir(folder_path)

        if len(picture_files) == 0:
            logger.warning("No picture files found in the folder.")
            print(f"[{datetime.now()}] No picture files found in the folder.")
            break

        picture_file = random.choice(picture_files)
        picture_path = os.path.join(folder_path, picture_file)

        # Choose random titles for Reddit and Twitter
        reddit_title = random.choice(reddit_title_choices)
        twitter_title = random.choice(twitter_title_choices)

        # Submit the picture to the subreddits
        for subreddit_name in subreddit_names:
            reddit_success = post_image_to_reddit(subreddit_name, title=reddit_title, image_path=picture_path)

            if reddit_success:
                # Upload the picture to Twitter if Reddit posting is successful
                twitter_success = post_image_to_twitter(title=twitter_title, image_path=picture_path)
                if twitter_success:
                    # Relocate the uploaded image to the uploaded folder
                    shutil.move(picture_path, os.path.join(uploaded_path, picture_file))
                    logger.info("Image relocated.")
                    print(f"[{datetime.now()}] Image relocated.")
                    image_counter += 1
                    print(f"Images posted: {image_counter}")
                else:
                    logger.warning("Skipping relocation. Image was not posted on Twitter.")
                    print(f"[{datetime.now()}] Skipping relocation. Image was not posted on Twitter.")
                    return

        # Wait for 30 minutes before posting the next picture
        time.sleep(1800)

if __name__ == "__main__":
    main()
