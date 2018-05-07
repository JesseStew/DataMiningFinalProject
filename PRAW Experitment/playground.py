'''
PRAW Documentation located at <http://praw.readthedocs.io/en/latest/index.html>

use <pip install praw> on command prompt/terminal to install praw
'''

import praw

'''If you are only analyzing public comments, entering 
   a username and password is optional when creating the 
   reddit instance.'''
   
'''Create an instance of Reddit'''
reddit = praw.Reddit(user_agent='Comment Extraction (by /u/stewedjesse)',
                     client_id='YJ_ZXLySsgkBZQ', client_secret="mkinsgGvgC9Y3cAgS9s9ZeQUxsw")

''''''

for comment in reddit.redditor('stewedjesse').comments.new(limit=None):
    print(comment.body)
    
'''
submission = reddit.submission(url='https://www.reddit.com/r/funny/comments/3g1jfi/buttons/')

submission.comments.replace_more(limit=0)

for top_level_comment in submission.comments:
    print(top_level_comment.body)
'''