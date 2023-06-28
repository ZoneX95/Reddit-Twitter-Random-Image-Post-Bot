# Reddit-Twitter-Random-Image-Post-Bot
The Reddit/Twitter Random Image Post Bot is a Python script that automates the posting of random images to Reddit and Twitter. It allows you to select a folder containing images, specify subreddits to post the images on, and automatically generates titles for the posts. 

Features

    Randomly selects an image from a specified folder
    Posts the image to multiple subreddits on Reddit
    Uploads the image to your Twitter account
    Generates random titles for the Reddit and Twitter posts
    Logs the bot's activities to a file
    Provides confirmation messages in the command prompt (CMD)

    Prerequisites

Before running the script, make sure you have the following:

    Python 3.x installed
    Required Python packages: praw, tweepy
    Reddit API credentials (client ID, client secret, username, password, user agent)
    Twitter API credentials (consumer key, consumer secret, access token, access token secret)
    Image files in a specified folder

    Setup

    Clone the repository or download the script file to your local machine.

    Install the required Python packages by running the following command in your terminal or command prompt:

pip install praw tweepy

Open the script file (RedditTwitterBot.py) in a text editor.

Replace the placeholder values with your actual API credentials and folder paths:

python

# Reddit API credentials
reddit_client_id = '<your_reddit_client_id>'
reddit_client_secret = '<your_reddit_client_secret>'
reddit_username = '<your_reddit_username>'
reddit_password = '<your_reddit_password>'
reddit_user_agent = '<your_reddit_user_agent>'

# Twitter API credentials
consumer_key = '<your_twitter_consumer_key>'
consumer_secret = '<your_twitter_consumer_secret>'
access_token = '<your_twitter_access_token>'
access_token_secret = '<your_twitter_access_token_secret>'

# Path to the folder containing the pictures
folder_path = '<your_folder_path>'
uploaded_path = '<your_uploaded_folder_path>'

Customize the subreddit names, title choices, and other variables according to your preferences.

Save the changes to the script file.

Usage

    Open a terminal or command prompt.

    Navigate to the directory where the script file is located.

    Run the script using the following command:

python RedditTwitterBot.py

The script will start posting random images to the specified subreddits on Reddit and your Twitter account.

Confirmation messages will be displayed in the command prompt indicating the status of each action (posting to Reddit, posting to Twitter, relocation of the image).

Notes

    The bot will select a random image from the specified folder each time it runs. Make sure the folder contains image files.
    To change the posting frequency, adjust the sleep time in seconds (1800 seconds = 30 minutes) in the script.
    The bot logs its activities to a file named bot.log.
    In case of any issues or errors, check the log file for detailed error messages.

    Contributing

Contributions to this project are welcome! If you encounter any issues, have suggestions, or want to add new features, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.
