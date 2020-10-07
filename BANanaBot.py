import praw
import os

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
USER_AGENT = os.environ['USER_AGENT']
USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']


reddit = praw.Reddit(client_id = CLIENT_ID,
                     client_secret = CLIENT_SECRET,
                     user_agent = USER_AGENT,
                     username = USERNAME,
                     password = PASSWORD)

subreddit = reddit.subreddit("sacrosaurio")

for submission in subreddit.new(limit = 25):

    for comment in subreddit.stream.comments(skip_existing=True):
        print("Searching...")
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if "ban" in comment_lower:
                parent = "/u/" + comment.parent().author.name
                print(parent)
                comment.reply(" \n\n. \u3000\u3000\u3000\u3002\u3000\u3000\u3000\u3000\u2022\u3000 \u3000\uff9f\u3000\u3000\u3002 \u3000\u3000.\n\n\u3000\u3000\u3000.\u3000\u3000\u3000 \u3000\u3000.\u3000\u3000\u3000\u3000\u3000\u3002\u3000\u3000 \u3002\u3000. \u3000\n\n.\u3000\u3000 \u3002\u3000\u3000\u3000\u3000\u3000 \u0d9e \u3002 . \u3000\u3000 \u2022 \u3000\u3000\u3000\u3000\u2022\n\n\u3000\u3000\uff9f\u3000\u3000" + parent + " was not An Impostor.\u3000 \u3002\u3000.\n\n\u3000\u3000'\u3000\u3000\u3000 1 Impostor remains \u3000 \u3000\u3000\u3002\n\n\u3000\u3000\uff9f\u3000\u3000\u3000.\u3000\u3000\u3000. ,\u3000\u3000\u3000\u3000.\u3000 .")