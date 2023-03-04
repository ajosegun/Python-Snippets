from instapy import InstaPy
import os
#import config


session = InstaPy(username=os.environ["IG_USERNAME"], password=os.environ["IG_PASSWORD"], 
                  headless_browser=True, want_check_browser=False)
session.login()

session.set_relationship_bounds(enabled=True, max_followers=3000) # Ignore users with >3000 followers
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21) # Sets limit to avoid IG ban 

# session.set_dont_like(["iot", "bot"])
# session.set_do_follow(True, percentage=25)

session.set_do_comment(True, comment_liked_photo=True, percentage=50)

comments = ["The pace of progress in artificial intelligence is incredibly fast.",
"I believe that artificial intelligence we'll augment our intelligence.",
"Machine learning is set to automate jobs that most people thought could only be done by people.",
"Computers are able to see, hear and learn.  Welcome to the future.",
           "As a data scientist, I appreciate how Python's visualization libraries make it easy to create informative charts and graphs.",
           "With Python's natural language processing libraries, you can create powerful text analysis applications that can automate tasks like sentiment analysis.",
           "One of the great things about coding in Python is the community - there are always new libraries and tools being developed to make our lives easier.",
            "Data science in Python allows us to gain insights into complex data sets and make informed decisions based on the results.",
            "AI and machine learning in Python can help automate repetitive tasks and free up time for more strategic decision-making.",
            "Python's simplicity and ease of use make it a great language for beginners learning to code, and there are plenty of resources available to help them get started with data science and AI.",
           ]

session.set_comments(comments)
session.like_by_tags(["coding", "datascience", "ai", "machinelearning"], amount=1, interact=True)

print(session)

session.end()

print("Completed")
