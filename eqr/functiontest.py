import praw
import memetext, string

def isMemy(s):
    s.strip()
    allcaps = True
    for c in s:
        if c!=" " and c!='\n':
            allcaps = c in string.ascii_uppercase
        if not allcaps:
            return False
    if s[0]==s[2]==s[4]==" " or s[1]==s[3]==s[5]==" ":
        return True
    return False
def extractStr(s):
    s.strip()
    if s.find('\n')!=-1:
        return s[:s.find('\n')]
    return s.strip()
# reddit = praw.Reddit('bot1')
#  
# subreddit = reddit.subreddit("pythonforengineers")
# with open("ReplyIDs.txt", "r") as f:
#     posts_replied_to = f.read()
#     posts_replied_to = posts_replied_to.split("\n")
#     posts_replied_to = list(filter(None, posts_replied_to))
# for submission in subreddit.hot(limit=5):
#     if submission.id not in posts_replied_to:
#         forest = praw.models.comment_forest.CommentForest(submission)
#         try:
#             forest.replace_more(limit=None)
#             commentList = forest.list()
#         except:
#             print("No comments found in top 5 posts")
#             break
#         for comment in commentList:
comment=" S T A I U M S T A T U S \n S \n T \n A \n D \n I \n U \n M \n S \n T \n A \n T \n U \n S"
if isMemy(comment):
    str = extractStr(comment)
    print(memetext.memeify(str))
    # posts_replied_to.append(submission.id)

# with open("posts_replied_to.txt", "w") as f:
#     for post_id in posts_replied_to:
#         f.write(post_id + "\n")