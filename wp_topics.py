#!/usr/bin/python

## This script uses the Reddit API to collect post titles and scores in a particular subreddit

# Import libraries
import praw

# Generate Reddit praw object
user_agent = "Writing prompts topic analysis 1.0"
reddit = praw.Reddit(user_agent=user_agent)

# Save hot ~1000 post information
subreddit_name = "TwoXChromosomes" 
post_count = 1000

subreddit = reddit.get_subreddit(subreddit_name)
output_file = open("subreddit_output.txt", "w")

for submission in subreddit.get_top_from_all(limit=post_count):
    output_file.write(submission.title.encode('ascii', 'ignore') + "|" + str(submission.score) + "|" + str(submission.id) + "\n")

output_file.close()

