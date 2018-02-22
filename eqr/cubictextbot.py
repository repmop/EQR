import praw
import memetext, string

def isMemy(s):
    s.strip()
    allcaps = True
    for c in s:
        if c!=" ":
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
reddit = praw.Reddit('bot1')
 
subreddit = reddit.subreddit("bottesting")
with open("ReplyIDs.txt", "r") as f:
    posts_replied_to = f.read()
    posts_replied_to = posts_replied_to.split("\n")
    posts_replied_to = list(filter(None, posts_replied_to))

for submission in subreddit.hot(limit=15):
    if submission.id not in posts_replied_to:
        submission.comments.replace_more(limit=1300)
        commentList=submission.comments.list()
        # try:
        #     forest.replace_more(limit=None)
        #     # print(type(forest._comments))
        #     commentList = forest.list()
        # except:
        #     print("No comments found in top 5 posts")
        #     break
        for comment in commentList:
            
            if isMemy(comment.body):
                # try:
                str = extractStr(comment.body)
                out = memetext.memeify(str)
                if out!="ERROR" and comment.author!='cubictextbot':    
                    submission.reply(memetext.memeify(str))
                posts_replied_to.append(submission.id)
                # except:
                #     print("Too many post reply attempts")
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")